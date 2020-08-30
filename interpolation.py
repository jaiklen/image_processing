import cv2

img = cv2.imread("C:/Users/jaiklen/Desktop/apple.jpg")
nearest = cv2.resize(img,None,fx = 20,fy = 20, interpolation = cv2.INTER_NEAREST)
bilinear = cv2.resize(img,None,fx = 20,fy = 20, interpolation = cv2.INTER_LINEAR)
cubic = cv2.resize(img,None,fx = 20,fy = 20, interpolation = cv2.INTER_CUBIC)
cv2.namedWindow("nearest",cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("bilinear",cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("cubic",cv2.WINDOW_AUTOSIZE)
cv2.imshow("nearest",nearest)
cv2.imshow("bilinear",bilinear)
cv2.imshow("cubic",cubic)
cv2.waitKey(0)
cv2.destroyAllWindows()
