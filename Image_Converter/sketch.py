import numpy as np
import imageio
import scipy.ndimage
import cv2

img = "girl-2.jpg"


def rgb2gray(rgb):
    # it is 2-dimensional array formula to convert image to gray scale
    return np.dot(rgb[...,:3],[0.2989,0.5870,0.1140])

def dodge(front,back):
    final_sketch = front*255/(255-back)
    final_sketch[final_sketch>255]=255
    final_sketch[back==255]=255
    return final_sketch.astype('uint8')




# to read the given image
ss = imageio.imread(img)  
# first we will change image to black and white that means gray scale 
gray = rgb2gray(ss)

i= 255-gray

blur = scipy.ndimage.filters.gaussian_filter(i,sigma =15)

r = dodge(blur,gray)

cv2.imwrite('girl-2-sketch.png',r)