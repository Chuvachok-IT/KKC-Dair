a = int(input("Введите число "))
if a >=90 and a <=100:
    print("5")
elif a >=75 and a <90:
    print("4")
elif a >=60 and a <75:
    print("3")
elif a < 60:
    print("2")
elif a <0 or a > 100:
    print("Ошибка ввода")