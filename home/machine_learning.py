import json
import pickle
import os
import numpy as np
from .models import TitanicData

class Test_Data:
    def __init__(self, obj):
        self.age =  0 if obj.age == "" else obj.age
        self.fare = obj.fare
        self.sex = obj.sex
        self.siblings = 0 if obj.siblings == "" else obj.siblings
        self.parch = 0 if obj.parch == "" else obj.parch
        self.pclass = obj.pclass
        self.embarked = obj.embarked

        with open(os.path.sep.join([os.getcwd(),'missing_data/missing_value_impute.json']), 'r') as f:
            m_data = json.load(f)

        self.missing_age_male = m_data["male_age"]
        self.missing_age_female = m_data["female_age"]
        self.missing_fare = m_data["fare"]


        with open(os.path.sep.join([os.getcwd(),'category_encode/categorical_en.json']), 'r') as f:
            category_enc = json.load(f)

        self.category_enc = category_enc

    def preprocess(self):
        if self.age == "":
            if self.sex == "male":
                self.age = self.missing_age_male
            else:
                self.age = self.missing_age_female
        
        if self.sex == "male":
            self.sex = self.category_enc["Sex"][self.sex]
        else:
            self.sex = self.category_enc["Sex"][self.sex]
        
        if self.fare == "":
            self.fare = self.missing_fare
        
        self.embarked = self.category_enc["Embarked"][self.embarked]
        
        data = np.array([int(self.pclass), int(self.age), int(self.siblings), int(self.parch), int(self.fare), int(self.embarked), int(self.sex)])
        data = np.expand_dims(data, axis=0)
        return data


def load_ml_model(data):
    model = pickle.load(open(os.path.sep.join([os.getcwd(),'model/model']), 'rb'))
    test_data = Test_Data(data)
    test_data = test_data.preprocess()
    pred = model.predict(test_data)
    return pred[0]