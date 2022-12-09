import cv2 as cv
import numpy as np

cap =cv.VideoCapture(0)
obtener = cv.VideoWriter('VideoFinal.avi', cv.VideoWriter_fourcc(*'XVID'), 30.0,(1300,800))

bgr = [240,240,240]
thresh = 150

minbgr = np.array([bgr[0] - thresh, bgr[1] - thresh, bgr[2] - thresh])
maxbgr = np.array([bgr[0] + thresh, bgr[1] + thresh, bgr[2] + thresh])

image = cv.imread('fondo.jpg')
fondo = cv.resize(image, (1300,800), interpolation = cv.INTER_AREA)

while (cap.isOpened()):
    ret, imagen = cap.read()
    if ret == True:
        frame = cv.resize(imagen, (1300,800), interpolation = cv.INTER_AREA)
        obtener.write(frame)
        
        atras = np.uint8(bgr)
        maskBGR = cv.inRange(frame, minbgr, maxbgr)
        mask_inv = cv.bitwise_not(maskBGR)

        resultBGR = cv.bitwise_and(frame, frame, mask = mask_inv)
        result_inv = cv.bitwise_and(fondo, fondo, mask = maskBGR)

        fin = cv.add(resultBGR, result_inv)

        cv.imshow('VIDEO FINAL.avi', fin)
        obtener.write(fin)

        if cv.waitKey(1) & 0xFF == ord('a'):
            break 


cap.release()
obtener.release()
cv.destroyAllWindows()
