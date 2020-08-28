import cv2
import sys
def pencil(img):
    image = cv2.imread(img)
    grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grayimageinv = 255-grayimage
    grayimageinv = cv2.GaussianBlur(grayimageinv,(21,21),0)
    output = cv2.divide(grayimage,255-grayimageinv,scale = 256.0)
    cv2.namedWindow("image",cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow("pencilsketch",cv2.WINDOW_AUTOSIZE)
    cv2.imshow("image",image)
    cv2.imshow("pencilsketch",output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = input()
print(pencil(img))
