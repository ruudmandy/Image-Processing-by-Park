# GrayScale Image Convertor
"""
import cv2
image = cv2.imread('reg_error.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_image.png',gray_image)
cv2.imshow('color_image',image)
cv2.imshow('gray_image',gray_image) 
cv2.waitKey(0)                 # Waits forever for user to press any key
cv2.destroyAllWindows()        # Closes displayed windows
"""

#End of Code

def rgb_to_gray(image_name):
    import cv2
    file_name,file_surname=image_name.split(".")
    bef_image=cv2.imread(image_name)
    gray_image=cv2.cvtColor(bef_image,cv2.COLOR_BGR2GRAY)
    cv2.imwrite(file_name+"-gray_image."+file_surname,gray_image)
    cv2.imshow("color_image",bef_image)
    cv2.imshow("gray_image",gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


image_name=input()
try:
    rgb_to_gray(image_name)
except:
    print("Error with unknow reason")
else:
    print("The image was converted.")
    print("Please check it on rgb-to-gray folder.")

