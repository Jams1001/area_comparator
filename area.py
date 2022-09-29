import cv2
import numpy as np

def areaF(imagePointer):

    gray = cv2.cvtColor(imagePointer, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY)[1]

    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    for c in cnts:
        cv2.drawContours(imagePointer,[c], 0, (255,255,0), 2)

    area = cv2.countNonZero(thresh)
    cv2.putText(imagePointer, "Area de la firma = {}".format(area), (700, 600), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 1)

    cv2.imshow('imagePointer', imagePointer)
    cv2.imwrite('imagePointer.png', imagePointer)
    cv2.waitKey()
    return area

# Declaración de punteros
image0 = cv2.imread('firmaN.jpg')
image1 = cv2.imread('firma3N.jpg')
image2 = cv2.imread('firmaccRN.jpg')
area0 = areaF(image0)
print('El área de la  primera firma es:', area0)
#area1 = areaF(image1)
area1 = areaF(image2)
print('El área de la  segunda firma es:', area1)
similaridad = np.absolute(((area1-area0)/area0)*100)
print('las imágenes son %f distintas' % (similaridad))



