# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 17:37:59 2021

@author: PAVILION
"""


from flask import Flask,request
import pandas as pd
import numpy as np
import pickle
import flasgger
from flasgger import Swagger


app = Flask(__name__)
Swagger(app)

pickle_in = open('model.pkl','rb')
model = pickle.load(pickle_in)


@app.route('/')
def welcome():
    return"Welcome All"



@app.route('/predict')
def predict_employee_performance():
    
    
    """Evaluation of Employee Performance
    This is using docstring for specifications.
    
    ---
    
    parameters:
        - name: EmpLastSalaryHikePercent
          in : query
          type: number
          required: true
        - name: EmpWorkLifeBalance
          in : query
          type: number
          required: true
        - name: YearsSinceLastPromotion
          in : query
          type: number
          required: true
        - name: EmpEnvironmentSatisfaction
          in : query
          type: number
          required: true    
    
    responses:
        200:
            description: The output values
    
    
    """
    
    
    EmpLastSalaryHikePercent = request.args.get('EmpLastSalaryHikePercent')
    EmpWorkLifeBalance = request.args.get('EmpWorkLifeBalance')
    YearsSinceLastPromotion = request.args.get('YearsSinceLastPromotion')
    EmpEnvironmentSatisfaction = request.args.get('EmpEnvironmentSatisfaction')
    prediction = model.predict([[EmpLastSalaryHikePercent,EmpWorkLifeBalance,YearsSinceLastPromotion,EmpEnvironmentSatisfaction]])
    return "The employess performance is rated as " + str(prediction)

@app.route('/predict_file',methods=["POST"])
def predict_employee_file():
    
    
    
     """Evaluation of Employee Performance
    This is using docstring for specifications.
    
    ---
    
    parameters:
        - name: file
          in : formData
          type: file
          required: true
       
    responses:
        200:
            description: The output values
    
    
    """
    
    
    
     df_test = pd.read_csv(request.files.get("file"))
     predictions = model.predict(df_test)
     return "The employess performance is rated as " + str(list(predictions))
 










if __name__ == '__main__':
    app.run()