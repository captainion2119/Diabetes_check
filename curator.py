from flask import jsonify


def curate(age, gluc, bp, skin, insulin, bmi_opt, bmi_val, height, weight):
    #check for invalid inputs
    if age.isdigit():
        pass
    else:
        return jsonify({'data': "Invalid input for age"})
    
    if gluc.isdigit():
        pass
    else:
        return jsonify({'data': "Invalid input for glucose level"})
    
    if bp.isdigit():
        pass
    else:
        return jsonify({'data': "Invalid input for blood pressure"})
    
    if skin.isdigit():
        pass
    else:
        return jsonify({'data': "Invalid input for skin thickness"})
    
    if insulin.isdigit():
        pass
    else:
        return jsonify({'data': "Invalid input for insulin level"})
    
    if bmi_opt == "yes":
        if bmi_val.isdigit():
            pass
        else:
            return jsonify({'data': "Invalid input for BMI"})
        
    if height.isdigit():
        pass
    else:
        return jsonify({'data': "Invalid input for height"})
    
    if weight.isdigit():
        pass
    else:
        return jsonify({'data': "Invalid input for weight"})
        