#建立module，結構化專案
#在主執行檔：lesson8_1.py中import此module

def calculate_bmi(height:int, weight:int)->float:
    return weight / (height / 100) ** 2

def get_state(bmi:float)->str:
    if bmi < 18.5:
        return "體重過輕"
    elif bmi < 24:
        return "正常範圍"
    elif bmi < 27:
        return "過重"
    elif bmi < 30:
        return "輕度肥胖"
    elif bmi < 35:
        return "中度肥胖"
    else:
        return "重度肥胖"