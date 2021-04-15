from flask import Flask, request, jsonify, render_template, url_for, make_response
import os
import numpy as np
app = Flask(__name__)
import numpy as np
import cv2
import pandas as pd
import io
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import cvlib as cv

model_path = "./pre-trained/gender_detection.model"
model = load_model(model_path)
classes = ['man','woman']


@app.route('/')
def home():
    return "Gender Detection API working perfectly!"

@app.route('/predict_api',methods=['POST','GET'])
def predict():
    #for HTML GUI rendering
    file = request.files['file']
    print(file.filename)
    file.save(file.filename)
    image = cv2.imread(file.filename)

    if image is None:
        print("Could not read input image")     
    face, confidence = cv.detect_face(image)
    count = 0
    for idx, f in enumerate(face):
        (startX, startY) = f[0], f[1]
        (endX, endY) = f[2], f[3]
        cv2.rectangle(image, (startX,startY), (endX,endY), (0,255,0), 2)
        face_crop = np.copy(image[startY:endY,startX:endX])
        face_crop = cv2.resize(face_crop, (96,96))
        face_crop = face_crop.astype("float") / 255.0
        face_crop = img_to_array(face_crop)
        face_crop = np.expand_dims(face_crop, axis=0)
        conf = model.predict(face_crop)[0]
        idx = np.argmax(conf)
        label = classes[idx]
        if count>1:
            break
        count+=1
    return jsonify(label = label,count = count)

if __name__ == '__main__':
    #web: python myApp.py runserver 0.0.0.0:$PORT
    app.run(host='0.0.0.0',port=5000,threaded=False)
    #app.run(host='0.0.0.0',port=5000)
