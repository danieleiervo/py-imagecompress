import os
import sys
from PIL import Image

#Configuration for compression quality, resolution and path
config = {
    "maxWidth": 1280,
    "maxHeight": 720,
    "quality": 75,
    "imgDir": "src/IMG/",
    "compDir": "src/Compressed/"
}

def compress(img):
    #Getting the size before compression from the file path
    filepath = os.path.join(config["imgDir"], img)
    oldsize = os.stat(filepath).st_size
    
    #Opening and setting the picture for compression
    picture = Image.open(filepath)
    imgWidth = picture.width 
    imgHeight = picture.height
    ratio = min(config["maxWidth"]/imgWidth, config["maxHeight"]/imgHeight)
    imgWidth = int(imgWidth * ratio)
    imgHeight = int(imgHeight * ratio)
    resolution = imgWidth, imgHeight

    #Saving the picture compressed
    picture.thumbnail(resolution, Image.BICUBIC)
    picture.save(config["compDir"] + img, 
    "JPEG", optimize = True, quality = config["quality"])

    #Return percentage of size compressed
    newsize = os.stat(os.path.join(os.getcwd(),config["compDir"]+img)).st_size
    percent = (oldsize-newsize)/float(oldsize)*100
    return percent


def main():
    totalImages = 0
    totalPercentage = 0

    print("STARTING...")

    for img in os.listdir(config["imgDir"]):
        if os.path.splitext(img)[1].lower() in ('.jpg', '.jpeg'):
            totalImages += 1
            totalPercentage += compress(img)

    averageComp = int(totalPercentage/totalImages)
    print("- Images processed: ", totalImages)
    print("- Average compression: ", averageComp)
    print("FINISH!")


if __name__ == "__main__":
    main()
