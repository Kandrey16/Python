year = int(input('Введите год: '))
int_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
result = 0
if(year % 4 == 0):
    int_list[1] = 29
    for x in range(12):
        for y in range(int_list[x]+1):
            result +=  y // 10 + y % 10
elif(year % 4 !=0):
    for x in range(12):
        for y in range(int_list[x]+1):
            result += y // 10 + y % 10
print(result)
