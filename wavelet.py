import pywt
import numpy as np
import cv2

def w2d(img,mode='haar',level=1):
    imArray=img
    #DataType Converstion
    # convert to gyroscope
    imArray=cv2.cvtColor(imArray,cv2.COLOR_RGB2GRAY)
    #convert to floa
    imArray=np.float32(imArray)
    imArray /= 255

    #compute coefficent
    coeff=pywt.wavedec2(imArray, mode, level=level)

    #Process Coffecient
    coeffs_M=list(coeff)
    coeffs_M[0] *= 0
    

    imArray_H=pywt.waverec2(coeffs_M, mode)
    imArray_H  *=255
    imArray_H= np.uint8(imArray_H)

    return imArray_H