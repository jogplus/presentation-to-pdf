import cv2
import imagehash
import PIL
import numpy
import pytesseract
import PyPDF2
import io
import os
import sys


class PresenationToPdf:

    msec_screen_cap_interval = 10000

    def __init__(self, video_path):
        self.vid_obj = cv2.VideoCapture(video_path)
        self.output_filename = (
            f"{os.path.splitext(os.path.basename(video_path))[0]}.pdf"
        )
        print(f"Creating file: {self.output_filename}")
        total_frames = self.vid_obj.get(cv2.CAP_PROP_FRAME_COUNT)
        fps = self.vid_obj.get(cv2.CAP_PROP_FPS)
        self.total_mseconds = (total_frames / fps) * 1000
        self.count = 0
        self.pdf_writer = PyPDF2.PdfFileWriter()

    def _append_pdf_page(self, image):
        # Convert screen cap into correct color space
        img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # Generate OCR pdf from image
        pdf = pytesseract.image_to_pdf_or_hocr(
            img_rgb, lang="eng", extension="pdf", nice=0
        )
        self.pdf_writer.appendPagesFromReader(PyPDF2.PdfFileReader(io.BytesIO(pdf)))

    def extract(self):
        success, image = self.vid_obj.read()
        old_image_hash = imagehash.average_hash(PIL.Image.fromarray(numpy.uint8(image)))
        self._append_pdf_page(image)
        # cv2.imwrite("frame%d.jpg" % count, image)
        self.count += 1

        while success:
            msec_timestamp = self.count * self.msec_screen_cap_interval
            # Skip to part in video
            self.vid_obj.set(cv2.CAP_PROP_POS_MSEC, msec_timestamp)

            # Extract the current frame
            success, image = self.vid_obj.read()

            if not success:
                break

            # Generate hash from screen cap
            new_image_hash = imagehash.average_hash(
                PIL.Image.fromarray(numpy.uint8(image))
            )

            # Compare new and old screen cap
            if abs(old_image_hash - new_image_hash) > 0:
                # Report percentage complete
                print(f"{msec_timestamp / self.total_mseconds:.0%}")
                self._append_pdf_page(image)
                # cv2.imwrite("frame%d.jpg" % count, image)

            old_image_hash = new_image_hash
            self.count += 1

        # Save all images into single pdf
        with open(self.output_filename, "w+b") as f:
            self.pdf_writer.write(f)
        print("Extraction complete!")
        # Open Finder if on MacOS
        if sys.platform == "darwin":
            os.popen(f"open -R {self.output_filename}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        video_path = sys.argv[1]
    else:
        video_path = input("Drag video file into this window and press Enter: ")
    PresenationToPdf(video_path.strip()).extract()
