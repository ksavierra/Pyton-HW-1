# 1. Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

print('Введите день недели: ')
x = float(input())

def f(x):
     if x < 1 or x > 7:
         return 'В неделе 7 дней'
     elif x == 1 or x == 2 or x == 3 or x == 4 or x == 5:
         return 'Будни'
     elif x == 6 or x == 7:
         return 'Выходной'
     else:
         return
day = x        
print(f(day))

