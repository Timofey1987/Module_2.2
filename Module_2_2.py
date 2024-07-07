first = int(input('Введите любое читло: '))
second = int(input('Введите любое читло: '))
third = int(input('Введите любое читло: '))
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)