import pandas as pd
from sklearn.ensemble import RandomForestRegressor

import bmicalc

#initialization:
diabetes_path = "C:/Users/Adithyakarthik/Documents/internship/Diabetes-main/Diabetes-main/conclusion/data/diabetes.csv" #add path here
diabetes_data = pd.read_csv(diabetes_path)

def diabetic_check(age, preg_val, preg_count, gluc, bp, skin, insulin, bmi_opt, bmi_val,height,weight):
    #defining the parameters to be considered to make a prediction
    attributes = ['Age', 'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin'] #ADD BMI AT THE END
    y = diabetes_data.Outcome
    X = diabetes_data[attributes]

    #defining and fitting the model
    diabetes_model = RandomForestRegressor(random_state=1)
    diabetes_model.fit(X,y)

    Val = [] #empty list to input values

    #inputting age
    #print(f"Age: {age}")
    Val.append(age)

    #checking for pregnancy and number of pregnancies
    while True:
        if preg_val == 1:
            pregnancy_count = preg_count
            break
        elif preg_val == 0:
            pregnancy_count = 0
            break
    #print(f"Pregnancy: {preg_val}")
    #print(f"pregnancy count: {preg_count}")

    Val.append(pregnancy_count)
    #print(f"glucose level: {gluc}")
    Val.append(gluc)
    #print(f"Blood pressure: {bp}")
    Val.append(bp)
    #print(f"Skin thickness: {skin}")
    Val.append(skin)
    #print(f"Insuling level: {insulin}")
    Val.append(insulin)
    while True:
        if bmi_opt == 1:
            bmi = bmi_val
            break
        elif bmi_opt == 0:
            bmi = bmicalc.calc_bmi(height,weight)
            break
    #print(bmi)
    Val.append(bmi)

    val_df = pd.DataFrame({'Age': [int(Val[0])],
                        'Pregnancies': [int(Val[1])],
                        'Glucose': [int(Val[2])],
                        'BloodPressure': [int(Val[3])], 
                        'SkinThickness': [int(Val[4])],
                        'Insulin': [int(Val[5])]
                        #,'BMI': [int(Val[6])] uncomment when BMI has been added
                        })

    pred_diab = float(diabetes_model.predict(val_df))
    #print(f"presence percentage of Diabetes {pred_diab*100} %")
    return pred_diab*100