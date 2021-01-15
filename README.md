# Presentation To PDF

Extract a PDF file out of a video presentation.
PDF file is searchable

## How it works
1. Captures an image from the video every 10s and compares to previous capture.
2. If the image is different, it saves the image and performs OCR on it.
3. Saves all images into a single searchable PDF.

## Usage
`python3 extract.py {video_path} {output_filename}`
