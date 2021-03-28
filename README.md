# py-imagecompress
A quick script in Python to handle multiple images compression using Pillow library. 


## Usage

 - This script features a **basic compression** usage of the [Pillow library](https://github.com/python-pillow/Pillow), so first thing is to install Pillow:

>     python3 -m pip install --upgrade pip
>     python3 -m pip install --upgrade Pillow

 - Set configuration variables as needed:
 **maxWidth** and **maxHeight** handle the *max resolution* the images will have after compression;
 **quality** handles the *quality of the compression*: keep this between 70 and 90 for best results;
 **imgDir** and **compDir** are the *relative paths* for the directory which contains images and the directory which will contain compressed images.
 
 - **Start the script** and watch for results on selected compression directory!

## Who is this for?
With this script you can handle multiple images compression in a simple way, so this may help if you were looking to learn image compression with Python. That's just a start, to learn more have a look at the [Pillow documentation](https://pillow.readthedocs.io/en/stable/index.html).
Could be a base to add JPEG compression on a Telegram bot, server and so on!
