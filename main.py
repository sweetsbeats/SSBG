import cv2

img = cv2.imread("totoro.jpg")
print img.size
print img.dtype

cv2.namedWindow('Totoro', cv2.WINDOW_NORMAL)
cv2.resizeWindow("Totoro", 1280, 720) 

cv2.imshow("Totoro", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
