from flask import Flask, jsonify, request

import curator
import diabetes

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST']) 
def home(): 
    if(request.method == 'GET'): 
        #gather data
        age = request.args['age']
        preg = request.args['pregnant']
        preg_val = 0
        preg_count = request.args['preg-count']
        gluc = request.args['glucose']
        bp = request.args['blood-pressure']
        skin = request.args['skin-thickness']
        insulin = request.args['insulin-level']
        bmi_opt = request.args['bmi']
        bmi_val = request.args['bmi-value']
        height = request.args['height']
        weight = request.args['weight']

        curator.curate(age, gluc, bp, skin, insulin, bmi_opt, bmi_val, height, weight)

        if preg == "yes":
            preg_val = 1
            if bmi_opt == "yes":
                bmi_opt = 1
                height = 0
                weight = 0
                prec = diabetes.diabetic_check(age, preg_val, preg_count, gluc, bp, skin, insulin, bmi_opt, bmi_val,height,weight)
                data = {"probablility": str(prec)+"%"}
            else:
                bmi_opt = 0
                prec = diabetes.diabetic_check(age, preg_val, preg_count, gluc, bp, skin, insulin, bmi_opt, bmi_val,height,weight)
                data = {"probablility": str(prec)+"%"}
        else:
            preg_val = 0
            if bmi_opt == "yes":
                bmi_opt = 1
                height = 0
                weight = 0
                prec = diabetes.diabetic_check(age, preg_val, preg_count, gluc, bp, skin, insulin, bmi_opt, bmi_val,height,weight)
                data = {"probablility": str(prec)+"%"}
            else:
                bmi_opt = 0
                prec = diabetes.diabetic_check(age, preg_val, preg_count, gluc, bp, skin, insulin, bmi_opt, bmi_val,height,weight)
                data = {"probablility": str(prec)+"%"}

            


        return jsonify({'data': data}) 
    
if __name__ == '__main__':
    app.run(debug=True)
