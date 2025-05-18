#奇偶數辨別（Odd or even）
#寫一個程式，當使用者輸入一個介於一定範圍（例如 1 到 1000）的數字，它能夠辨別奇偶，並輸出檢驗結果給使用者。

# def check_num():
#     while True:
#         try:
#             input_num = int(input("請輸入一個數字(1~1000)："))
#             if input_num < 1 or input_num > 1000:
#                 print("數字超出範圍")
#             else:
#                 num = input_num % 2
#                 if num == 0:
#                     print("這是偶數")
#                 else:
#                     print("這是奇數")
#                 break
#         except ValueError:
#             print("輸入錯誤，請輸入有效的整數。")

# while (True):
#     check_num()
#     check_again = input("再次檢查(Y/N)：").upper().strip()
#     if check_again != "Y":
#         print("檢查結束")
#         break



# def check_num():
#     while True:
#         try:
#             input_num = int(input("請輸入一個數字(1~1000)："))
#             if input_num < 1 or input_num > 1000:
#                 print("數字超出範圍，請重新輸入。")
#             else:
#                 if input_num % 2 == 0:
#                     print("這是偶數")
#                 else:
#                     print("這是奇數")
#                 break  # 輸入有效，跳出迴圈
#         except ValueError:
#             print("輸入錯誤，請輸入有效的整數。")

# while True:
#     check_num()
#     check_another_num = input("再次檢驗(O/X)：").strip().upper()
#     if check_another_num == "X":
#         break

# print("檢查結束")



# 計算字數（Word count）
# 使用者輸入一段文字，程式統計字數。
# 範例：
# 　畫面：你心裡在想什麼？
# 　輸入：我要成為寫程式的專家
# 　輸出：你用了 10 個文字述說內心的想法

# thought = input("你心裡在想什麼？").strip()
# words = len(thought)
# print(f"你用了 {words} 個文字述說內心的想法")





# 個資判斷（Biography info）
# 請使用者輸入個資，程式檢查資料是否有效，並將輸入的資訊統整，完整呈現給使用者。
# 例如，程式可以問使用者的名字。如果用戶輸入「*」，程式就要提醒他們輸入錯誤，並要求他們輸入有效的名字。
# 最後，程式會輸出類似以下的資訊：
# 　姓名：John Doe
# 　生日：1954/1/1
# 　地址：紐約第五大道 24 號
# 　目標：成為史上最強的工程師



#name
while True:
    name = input("what's your name?\n").lower().capitalize()
    if "*" in name:
        print("名字不能包含 '*' 字元，請重新輸入。")
    else:
        break
#birth
print("please enter your birthday.")
while True:
    birth_year = input("year(yyyy): ")
    if len(birth_year) != 4:
        print("please enter 4-digit numbers.")
    else:
        break
while True:
    birth_month = input("month(mm): ")
    if len(birth_month) != 2:
        print("please enter 2-digit numbers.")
    else:
        break
while True:
    birth_date = input("date(dd): ")
    if len(birth_date) != 2:
        print("please enter 2-digit numbers.")
    else:
        break
birthday = (f"{birth_year}/{birth_month}/{birth_date}")
#address
address = input("please enter your address:\n").lower().capitalize()

#target
target = input("and your target?\n").lower().capitalize()

print("-----------------------")
print("Your Biography is: ")
print(f"Name: {name}")
print(f"Birthday: {birthday}")
print("Address: "+address)
print(f"Target: {target}")

