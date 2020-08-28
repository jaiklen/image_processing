import cv2 

# This is a magic command to display in an external window 

image = cv2.imread("C:/Users/jaiklen/Pictures/jaiklen.png", 0) 
# Loading the image 

double = cv2.resize(image, (0, 0), fx = 2, fy = 2)
half = cv2.resize(image, (0, 0), fx = 0.5, fy = 0.5) 
#bigger = cv2.resize(image, (1050, 1610),interpolation = cv2.INTER_LINEAR) 

#stretch_near = cv2.resize(image, (780, 540), interpolation = cv2.INTER_LINEAR) 

cv2.namedWindow("original",cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("double",cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("half",cv2.WINDOW_AUTOSIZE)
cv2.imshow("original",image)
cv2.imshow("double",double)
cv2.imshow("half",half)
cv2.waitKey(0)
cv2.destroyAllWindows()
