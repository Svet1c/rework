# 3 задание

list_1 = [2, 3, 4]
list_2 = [5, 6, 7, 8, 9, 0]
list_3 = [11, 12, 13, 14]
while True:
    percent = int(input("Введите кол-во % : "))
    if percent % 10 == 1 and percent % 100 not in list_3:
        print(percent, "процент")
    elif percent % 10 in list_1 and percent % 100 not in list_3:
        print(percent, "процента")
    elif percent % 10 in list_2 or percent % 100 in list_3:
        print(percent, "процентов")