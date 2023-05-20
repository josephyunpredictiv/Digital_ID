import sys
from encode import *
import cv2

if __name__ == '__main__':
    digitalObject = cv2.imread(sys.argv[1])
    fileType='jpeg'
    byteEncodedDigitalObject=imgToByte(digitalObject, fileType)

    digital_ID, byteEncodedDigitalID = modelv2(byteEncodedDigitalObject)
    QR(digital_ID).save(sys.argv[2])