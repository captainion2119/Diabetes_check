


def calc_bmi(height,weight):
    m_height = int(height)/100
    weight = int(weight)
    return round((weight / m_height**2),2)
