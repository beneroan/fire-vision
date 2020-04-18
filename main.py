from cv2 import VideoCapture, imwrite
import os
from flask import jsonify
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import sched, time
import threading
import random

app = Flask(__name__)

fire = False

cam = VideoCapture(0)

def checkFireThread():
   while True:
      global fire
      print('checking fire')
      success, image = cam.read()
      if not success:
         return
      
      imwrite("images/lastimage.jpg", image)

      # @anay do something with the saved image
      # if gcp says fire, set fire to true
      # if gcp says no fire, set fire to false
      fire = random.randint(0, 1) == 0

      time.sleep(5)

thread = threading.Thread(target=checkFireThread, args=())
thread.start()

@app.route('/status/fire', methods=['GET'])
def getStatus():
   return jsonify({ 'status': fire })
