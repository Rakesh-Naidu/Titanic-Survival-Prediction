import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [int(x) for x in request.form.values()]
    print(features)
    final_feat = [np.array(features)]
    print(final_feat)
    print(len(final_feat))
    prediction = model.predict(final_feat)
    if(prediction==1):
        return render_template('index.html', prediction_text = "This Passenger will Survive")
    else:
        return render_template('index.html', prediction_text= "This Passenger will not Survive")

if __name__ == "__main__":
    app.run(debug=True)