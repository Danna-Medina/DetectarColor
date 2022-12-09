
import cv2 as cv
import numpy as np

imagenOriginal=cv.imread('C:\\Users\\GabrielAsus\\Pictures\\yane_garcia2.jpg')
imagenPlaya=cv.imread('C:\\Users\\GabrielAsus\\Pictures\\playa.jpg')
cv.imshow('original',imagenOriginal)
cv.imshow('fondo',imagenPlaya)
cv.waitKey()

bgr = [55,200,55]
thresh = 70

minBGR = np.array([bgr[0] - thresh, bgr[1] - thresh, bgr[2] - thresh])
maxBGR = np.array([bgr[0] + thresh, bgr[1] + thresh, bgr[2] + thresh])
minBGR=np.array([0,0,200])
maxBGR=np.array([100,70,255])


maskBGR = cv.inRange(imagenOriginal,minBGR,maxBGR)
mask_inv = cv.bitwise_not(maskBGR)
cv.imshow('mascara',maskBGR)
cv.imshow('mascara_inv',mask_inv)

# kernel = np.ones((5, 5), np.uint8)
# maskBGR=cv.erode(maskBGR,(1,1,1,1,1,1,1,1,1),30)

# cv.imshow('mascara con erode',maskBGR)
resultBGR = cv.bitwise_and(imagenOriginal,imagenOriginal, mask=mask_inv)

result_inv = cv.bitwise_and(imagenPlaya, imagenPlaya, mask = maskBGR)


cv.imshow('resultado',resultBGR)
cv.imshow('resultado_inv',result_inv)

total=cv.add(resultBGR,result_inv)

cv.imshow('resultado total',total)

cv.imwrite('resultado.jpg',total)
cv.waitKey()
cv.destroyAllWindows()
