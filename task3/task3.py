# Практика 
## Запросить у пользователя 3 значения (вводит число Int) 

### Действия 

#1. Если нет ни одого нуля - вывести: "Нет нулевых значений!!!"(Без if - использовать лень)
#2. Вывести первое ненулевое значение. Если введены все нули - вывести "Введены все нули!" (цикл не использовать) без if - использовать лень
#3. Если первое значение  больше чем сумма второго и третьего вывести a - b - c
#4. Если первое значение меньше чем сумма второго и третьего вывести b + c - a
#5. Если первое значение больше 50 и при этом одно из оставшихся значение больше первого вывести "Вася"
#6. Если первое значение больше 5 или оба из оставшихся значений равны 7 вывести "Петя"

a = int(input('Введите первое значение: '))
b = int(input('Введите второе значение: '))
c = int(input('Введите третье значение: '))
print("Нет нулевых значений!!!" * (a != 0 and b != 0 and c != 0)) 
print(str(a or b or c or "Введены все нули!"))
a > (b + c) and print(a - b - c)
a < (b + c) and print(b + c - a)
a > 50 and (b > a or c > a) and print("Вася!")
print("Петя" * (a > 5 or (b == 7 and c == 7)))