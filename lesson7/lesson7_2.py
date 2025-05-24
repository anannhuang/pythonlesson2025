import tools

def main():
    height:int = int(input("請輸入身高(cm):"))
    weight:int = int(input("請輸入體重(kg):"))

    bmi = tools.calculate_bmi(height, weight)

    print(bmi)
    print(tools.get_state(bmi))


#結構化程式碼
#此處為主程式：
if __name__ == '__main__':
    main()