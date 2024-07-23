# There are 3 parameters to read an image - 
#cv2.IMREAD_COLOR (1) => Specify to load the image in color
#cv2.IMREAD_GRAYSCALE (0) => Specify to load the image in grayscale / black & white
#cv2.IMREAD_UNCHANGED (-1) => Specify to load the image unchanged
import cv2,os
img=cv2.imread("pickachu.png",1)
cv2.imshow('pika',img)
cv2.waitKey(0)

img2=cv2.imread("pickachu.png",0)
cv2.imshow('pika vika',img2)
cv2.waitKey(0)

img3=cv2.imread("pickachu.png",-1)
cv2.imshow('pika vika chu',img3)
cv2.waitKey(0)

path=r"C:\\Users\\codin\\Desktop\\2022\\Coding Class\\OpenCV\\pickachu.png"
path2=r"C:\\Users\\codin\\Desktop"
os.chdir(path2)
print("before saving image")
print(os.listdir(path2))

filename="Pickachu.png"

n=cv2.imread(path)
cv2.imwrite(filename,n)


print("after saving image")
print(os.listdir(path2))










cv2.destroyAllWindows()