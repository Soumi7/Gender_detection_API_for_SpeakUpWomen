# Gender_detection_API_for_SpeakUpWomen

## API endpoint usage :

```curl -X POST https://speakupgenderapi.herokuapp.com/predict_api -F "file=@IMAGE_NAME"```

For example :

```curl -X POST https://speakupgenderapi.herokuapp.com/predict_api -F "file=@soumi.jpeg"```

## Instructions to run

This model classifies an input image into either of the two classes - man or woman. To run :

```git clone https://github.com/Soumi7/Gender_detection_API_for_SpeakUpWomen```
 Change CWD to the cloned repo folder :
 
 ```cd Gender_detection_API_for_SpeakUpWomen```
 
 Run flask app :
 
 ```python3 app.py```
 
 Now check API results locally :
 
 ```curl -X POST http://127.0.0.1:5000/predict_api -F "file=@soumi.jpeg"```

 
 
