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
  print("")
  timeStamp=timestamp()
  byteEncodedTimestamp=timeStamp.encode()
  print("timestamp: " + str(timeStamp))
  print("byteEncodedTimestamp: " + str(byteEncodedTimestamp))
  print("byteEncodedDigitalObject: " + str(byteEncodedDigitalObject))

  #step 2 timestamp+byteEncodedDO
  print("")
  byteEncodedDigitalID=byteEncodedTimestamp+byteEncodedDigitalObject
  print("byteEncodedDigitalID: " + str(byteEncodedDigitalID))

  #step 3 hash byteEncodedDigitalID
  print("")
  hashEncodedDigitalID=hashEncode(byteEncodedDigitalID)
  print("hashEncodedDigitalID: " + str(hashEncodedDigitalID))
  
  #output
  return hashEncodedDigitalID, byteEncodedDigitalID