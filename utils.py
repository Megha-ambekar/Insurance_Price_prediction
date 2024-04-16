import numpy as np
import os
import pickle
import json
import config

class medicalInsurancePred():
    def __init__(self,age, gender, bmi, children, smoker, region):
        self.age = age
        self.gender = gender
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = region

    def load_model(self):
        with open(config.MODEL_FILE_PATH,"rb") as file:
            self.model = pickle.load(file) 
        with open(config.JSON_FILE_PATH,"r") as file:
            self.json_data = json.load(file) 

    def calc_price(self):
        self.load_model()
        arr1 = np.zeros(len(self.json_data["columns"]))
        print(arr1)
        arr1[0] = self.age
        arr1[1] = self.json_data["gender"][self.gender]
        arr1[2] = self.bmi
        arr1[3] = self.children
        arr1[4] = self.json_data["smoker"][self.smoker]
        arr1[5] = self.json_data["region"][self.region]
        predict_charges = self.model.predict([arr1])
        return predict_charges








