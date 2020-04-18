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
      
      res = os.popen("python gcp.py images/lastimage.jpg 573370690633 ICN724477007634628608").read()

      # print(res)

      fire = 'Fire' in res

      # print(fire)

      # flask doesn't like this :(
      # with open("images/lastimage.jpg", 'rb') as ff:
      #    content = ff.read()
      #    prediction = get_prediction(content, "573370690633", "ICN724477007634628608")
      
      #    fire = request.payload[0].display_name == 'Fire'

      time.sleep(5)

@app.route('/status/fire', methods=['GET'])
def getStatus():
   return jsonify({ 'status': fire })

thread = threading.Thread(target=checkFireThread, args=())
thread.start()
