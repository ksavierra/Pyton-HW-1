# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

print('Введите значение x в координатах первой точки: ')
x1 = float(input())
print('Введите значение y в координатах первой точки: ')
y1 = float(input())
print('Введите значение x в координатах второй точки: ')
x2 = float(input())
print('Введите значение y в координатах второй точки: ')
y2 = float(input())


import math
dis = ((x2-x1)**2 + (y2-y1)**2)
sqrt = math.sqrt(dis) 

print("Расстояние между точками - " +str(sqrt))





    
    