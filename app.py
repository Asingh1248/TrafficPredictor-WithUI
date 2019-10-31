import numpy as np
from flask import Flask, request, jsonify,render_template
# Redirect to fisrt Home Page
import pickle

app = Flask(__name__)

# Load the model
model = pickle.load(open('mlp.pkl1571928435','rb'))

def Predictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,-1)
    result = model.predict(to_predict)
    print(result[0])
    return int(result[0]) # Type Error 

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])

def predict():
    # Date te liye --Doubt
    #date_features = [int(x) for x in request.form.values()]
    #final_features=[np.array(date_features)]
#   prediction=model.predict(final_features)
    
#   output=round(prediction[0],2)
#   return render_template('index.html',prediction_text = 'Traffic Volume should be ${}'.format(output))
    to_predict_list=request.form.to_dict()
    to_predict_list = list(to_predict_list.values())
    print(to_predict_list)
    to_predict_list = list(map(float, to_predict_list))
    print(to_predict_list)
    result=Predictor(to_predict_list)
    return render_template('index.html',prediction_text = 'Traffic Volume should be {}'.format(result))




@app.route('/predict_api',methods=['POST'])
def predict_api():
    # Get the data from the POST request.
    data = request.get_json(force=True)

    # Make prediction using model loaded from disk as per the data.
    
    data = list(data.values())
    print(data)
    #data = list(map(int,data))
    result=Predictor(data) 
    # Take the first value of prediction
   
    return jsonify(result)

if __name__ == '__main__':
    app.run(port=5000,debug=True)