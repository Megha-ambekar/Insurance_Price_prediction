from flask import Flask,request,jsonify
import config
from utils import medicalInsurancePred
import numpy as np

app = Flask(__name__)
@app.route("/")
def get_home():
    return "Hello Welcome to Medical Insurance"

@app.route("/Predict_charges",methods= ["POST","GET"])
def get_insurance():
    if request.method == "POST":
        data = request.form
        print("user input data is >> ",data)
        age = int(data["age"])
        gender = data["gender"]
        bmi = eval(data["bmi"])
        children = int(data["children"])
        smoker = data["smoker"]
        region = data["region"]
        med_obj = medicalInsurancePred(age,gender,bmi,children,smoker,region)
        charges = med_obj.calc_price()
        return jsonify({"Result":f"Predicted medical insurance charges is {charges[0]}" })

if __name__ == "__main__":
    app.run()




