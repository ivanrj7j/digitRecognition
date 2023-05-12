from flask import Flask, render_template, request
import torch
import numpy as np
import json
import pickle
import numpy as np
from PIL import Image
from base64 import b64decode
from io import BytesIO
# importing packages 

with open('model.mdl', 'rb') as f:
    model = pickle.load(f)
    # loading model

app = Flask(__name__)
# initialising the app 

@app.route('/')
def hello():
    return render_template('index.html')
    # home page 

@app.route('/predictCOlor', methods=['POST'])
def predictColor():
    imgData = Image.open(BytesIO(b64decode(request.form.get('image')))).convert('L').resize((28,28))
    # getting the image and resizing it 

    features = torch.from_numpy(np.array(imgData).astype(np.float32).reshape(1, 784))
    # converting the image to a tensor 

    predictions = (model(features).flatten() * 100).tolist()
    # predicting the digit 

    predictionsTuple = [[x,predictions[x]] for x in range(len(predictions))]
    predictionsTuple.sort(key=lambda x:x[1], reverse=True)
    # sorting the predictions 

    return json.dumps(predictionsTuple)

if __name__ == '__main__':
    app.run(debug=True)