# Presentation To PDF

Extract a PDF file out of a video presentation.
PDF file is searchable

## How it works
1. Captures an image from the video every 10s and compares to previous capture.
2. If the image is different, it saves the image and performs OCR on it.
3. Saves all images into a single searchable PDF.

## How to use it
### MacOS
1. Download Python3 at https://www.python.org/downloads/
1. Download this code by clicking the green code button on Github and then "Download ZIP"
2. Unzip the downloaded folder and open it
4. Open Terminal.app and type `pip3 install -r ` and then drag in `requirements.txt` into the window. It should look something like `pip3 install -r /../requirements.txt`. (Make sure you have a space after the `-r`). Then hit enter.
5. In Terminal.app, install `brew` by pasting in the command `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
6. In Terminal.app, install `tesseract` by pasting in the command `brew install tesseract`
7. In Terminal.app, type `python3` and then drag in `extract.py` into the window. It should look something like `python3 /../extract.py`. (Make sure you have a space after `python3`). Then hit enter.
8. Follow the instruction in the window "Drag video file into this window and press Enter: "

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

