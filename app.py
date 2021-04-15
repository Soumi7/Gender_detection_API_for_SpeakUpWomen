from flask import Flask, request, jsonify, render_template, url_for, make_response
from werkzeug.utils import secure_filename
import os
import json
import numpy as np
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "./imgdir"
import numpy as np
import cv2
import pandas as pd
import pytesseract
import io
from keras.preprocessing.image import img_to_array
from keras.models import load_model
from keras.utils import get_file
import numpy as np
import os
import cvlib as cv

model_path = "./pretrained/gender_detection.model"
model = load_model(model_path)
classes = ['man','woman']


# Disable scientific notation for clarity
# Load the model
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict_api',methods=['POST','GET'])
def predict():
    #for HTML GUI rendering
    file = request.files['file']
    print(file.filename)
    if file.filename.split(".")[-1]!="png":
        return render_template('Wrong_file_type.html')

    image = cv2.imread(args.image)

    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
