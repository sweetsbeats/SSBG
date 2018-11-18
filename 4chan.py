import basc_py4chan
import argparse
import urllib

import cv2
import numpy
import imutils
from skimage.measure import compare_ssim
import glob

import main

image = urllib

parser = argparse.ArgumentParser()
parser.add_argument("thread", help="Thread to grab images from" )
args = parser.parse_args()

# Get URL to thread
threadURL = args.thread

URL_MATCH = "https://boards.4chan.org"

# Break down the URL
threadURL = threadURL[len(URL_MATCH) : ]

boardChar = threadURL[ : -len(threadURL)+2]
threadNum = threadURL[9 : ]

print "DEBUG: "
print "threadURL",threadURL
print "boardChar",boardChar
print "threadNum",threadNum
print "\n\n"

w = basc_py4chan.Board(boardChar)

thread = w.get_thread(threadNum)

print thread

if thread.sticky:
    print "Thread is stickied"

for post in thread.posts:
    print "Subject: ", post.subject
    print "Has File: ",post.has_file
    print "Comment: ",post.text_comment



for f in thread.file_objects():
    print "file URL",f.file_url
    image.urlretrieve(f.file_url, "images/"+f.filename)



images = [cv2.imread(file) for file in glob.glob("images/*.png")]
#main.getImagesFromFolder("images/")
print type(images)


if main.compareAllImages(images):
    print "Test works"
