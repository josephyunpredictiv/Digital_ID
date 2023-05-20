'''
Author: @josephyunpredictiv
'''

import datetime
import cv2
import numpy as np
from PIL import Image
import io
import hashlib
import qrcode
import pandas as pd
import time

def QR(string):
  qrCode = qrcode.make(string)
  return qrCode

def hashEncode(byteString):
  h = hashlib.new('sha256')
  h.update(byteString)
  hash=h.hexdigest()
  return hash

def timestamp():
  timestamp = datetime.datetime.now()
  timestamp = "%04d%02d%02d%02d%02d%02d%06d" % (timestamp.year, timestamp.month, timestamp.day, timestamp.hour, timestamp.minute, timestamp.second, timestamp.microsecond)
  return timestamp

def imgToByte(image, fileType):
  fileType='.' + fileType
  imgEncode = cv2.imencode(fileType, image)[1]
  imgEncode = np.array(imgEncode)
  byteEncode = imgEncode.tobytes()
  return byteEncode

def modelv2(byteEncodedDigitalObject):
  
  #step 1 byte encode timestamp
  timeStamp=timestamp()
  byteEncodedTimestamp=timeStamp.encode()

  #step 2 timestamp+byteEncodedDO
  byteEncodedDigitalID=byteEncodedTimestamp+byteEncodedDigitalObject

  #step 3 hash byteEncodedDigitalID
  hashEncodedDigitalID=hashEncode(byteEncodedDigitalID)
  
  #output
  return hashEncodedDigitalID, byteEncodedDigitalID