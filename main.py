
import cv2
import numpy

img1 = cv2.imread("totoro.jpg")
img2 = cv2.imread("totworo.jpg");

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
    cv2.namedWindow('Differences', cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Differences", 1280, 720) 

    cv2.imshow("Differences", diff)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print "Images are the same"
