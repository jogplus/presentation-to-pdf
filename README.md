# Presentation To PDF

Extract a PDF file out of a video presentation.
PDF file is searchable

## How it works
1. Captures an image from the video every 10s and compares to previous capture.
2. If the image is different, it saves the image and performs OCR on it.
3. Saves all images into a single searchable PDF.

## How to use it
### MacOS
1. Download this code by clicking the green code button on Github and then "Download ZIP"
2. Unzip the downloaded folder and open it
3. Click on file `run.command`
4. Let everything install (may take some time)
5. Follow the instruction in the window "Drag video file into this window and press Enter: "

## Manual Installation
1. Create and activate a Python virtual env
```
$ python3 -m venv env
$ source env/bin/activate
```
2. Install dependencies
```
$ pip3 install -r requirements.txt
```

## Usage
`python3 extract.py` or `python3 extract.py {video_path}`

