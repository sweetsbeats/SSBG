
import cv2
import numpy
import imutils
from skimage.measure import compare_ssim

img1 = cv2.imread("totoro.jpg")
img2 = cv2.imread("totoropng.png");

print "debug info:"
print "Image 1"
print img1.size
print img1.dtype

print "\n"

print "Image 2"
print img2.size
print img2.dtype

diff = cv2.subtract(img1, img2)

if numpy.any(diff):

    grayA = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    
    (score, imDiff) = compare_ssim(grayA, grayB, full=True)

    imDiff = (imDiff * 255).astype("uint8")
    
    thresh = cv2.threshold(imDiff, 0, 255,
                           cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    conts = cv2.findContours( thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE )
    conts =  conts[0] if imutils.is_cv2() else conts[1]

    for c in conts:
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(img1, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.rectangle(img2, (x, y), (x+w, y+h), (0, 0, 255), 2)
    
        

    img1S = cv2.resize(img1, (600,400))
    img2S = cv2.resize(img2, (600,400))
    
    # hoz. concat.
    final = numpy.concatenate((img1S, img2S), axis = 1)

    cv2.imshow("Differences", final)

    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print "Images are the same"
