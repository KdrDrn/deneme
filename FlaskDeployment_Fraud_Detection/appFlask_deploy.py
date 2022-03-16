from flask import Flask, render_template, request
import jsonify
import requests
import pandas as pd
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from keras import models
from keras.models import load_model
import tensorflow as tf

app = Flask(__name__)
rf_model = pickle.load(open('rf_deploy', 'rb'))
#lgbm_model = pickle.load(open('lgbm_deploy', 'rb'))
dl_model = dl_deploy = load_model("dl_deploy.h5")

@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')

data = {"v14":0, "v4":0 ,"v12":0,"v10":0, "v11":0, "v17":0, "v3":0}

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        data["v14"] = float(request.form['v14']) 
        data["v4"] = float(request.form['v4'])
        data["v12"] = float(request.form['v12']) 
        data["v10"] = float(request.form['v10'])
        data["v11"] = float(request.form['v11'])
        data["v17"] = float(request.form['v17'])
        data["v3"] = float(request.form['v3'])
        model_selection=int(request.form['ModelSelection'])
        
        data = pd.DataFrame.from_dict([data])
    
        if model_selection == 1:
            print("merhaba")
        else:
            print("hello")
    #         prediction = rf_model.predict(data)

    #         if prediction == 1: 
    #             return render_template("index.html", 
    #                                    prediction_text="Model predicted a fradulent issue \
    #                                    and a confirmation e-mail and sms were sent to the customer.")
    #         else:
    #             return render_template("index.html", 
    #                                    prediction_text="Everthing seems OK")

    #     elif model_selection == 2:
    #          prediction = lgbm_model.predict(data)

    #         if prediction == 1: 
    #             return render_template("index.html", 
    #                                    prediction_text="Model predicted a fradulent issue \
    #                                    and a confirmation e-mail and sms were sent to the customer.")
    #         else:
    #             return render_template("index.html", 
    #                                    prediction_text="Everthing seems OK")
            
    #    else:     
    #        prediction = dl_model.predict(data)

    #         if prediction > 0.50:
    #             return render_template("index.html", 
    #                                    prediction_text="Model predicted a fradulent issue \
    #                                    and a confirmation e-mail and sms were sent to the customer.")
    #         else:
    #             return render_template("index.html", 
    #                                    prediction_text="Everthing seems OK")
            
if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')