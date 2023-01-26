print("Операции: \n 1.Сложение \n 2.Вычитание \n 3.Умножение \n 4.Деление \n")

operation = int(input("Выберите операцию: "))
firstValue = float(input("Введите первое число: "))
secondValue = float(input("Введите второе число: "))

if (operation == 1):
    finalValue = firstValue + secondValue
elif (operation == 2):
    finalValue = firstValue - secondValue
elif (operation == 3):
    finalValue = firstValue * secondValue
elif (operation == 4):
    if (secondValue == 0):
        print("На ноль делить нельзя")
    else:    
        finalValue = firstValue / secondValue
print("Вывод", finalValue)
while(True):
    operation = int(input("Выберите операцию: "))
    secondValue = float(input("Введите второе число: "))
    if (operation == 1):
        finalValue = finalValue + secondValue
    elif (operation == 2):
        finalValue = finalValue - secondValue
    elif (operation == 3):
        finalValue = finalValue * secondValue
    elif (operation == 4):
        if (secondValue == 0):
            print("На ноль делить нельзя")
        else:    
            finalValue = firstValue / secondValue
    print("Вывод", finalValue)


