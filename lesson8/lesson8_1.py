#只import edu資料夾 -> edu module
#import edu

#從edu資料夾中的tools module，import calculate_bmi, get_state兩個function
#from edu.tools import calculate_bmi, get_state

#從edu資料夾中的tools module，import calculate_bmi, get_state兩個function
#且分別重新命名(用as)為a1, a2
from edu.tools import calculate_bmi as a1
from edu.tools import get_state as a2


def main():
    height:int = int(input("請輸入身高(cm):"))
    weight:int = int(input("請輸入體重(kg):"))

    bmi = a1(height, weight)

    print(bmi)
    print(a2(bmi))


#結構化程式碼
#此處為主程式：
if __name__ == '__main__':
    main()