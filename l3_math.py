from math import sqrt #открываем библиотеку
a =int (input("Ввод радиус круга в сантиметрах:" )) #ввод радиус круга в сантиметрах
b = 3.14*a*a #формула площади круга 
print(b, "Площадь круга в сантиметрах")
print(b/10000, "Площадь круга в метрах")
с = 2*a*3.14 # формула длины окружности 
print(с, "Длина окружности в сантиметрах")
print(с/100, "Длина окружности в метрах")
d = (2*a)/sqrt(2) # формула длины стороны вписанного в окружность квадрата
print(d, "Длина стороны вписанного в окружность квадрата в сантиметрах")
print(d/100, "Длина стороны вписанного в окружность квадрата в метрах")
e = (a*sqrt(3)) # формула длины стороны вписанного равностороннего треугольника
print(e, "Длина стороны вписанного равностороннего треугольника в сантиметрах")
print(e/100, "Длина стороны вписанного равностороннего треугольника в метрах")
f = (2*a) # формула длины стороны описанного вокруг окружности квадрата 
print(f, "Длина стороны описанного вокруг окружности квадрата в сантиметрах")
print(f/100, "Длина стороны описанного вокруг окружности квадрата в метрах")
t = (6*a/sqrt(3)) # формула длины стороны описанного вокруг окружности равностороннего треугольника
print(t,"Длина стороны описанного вокруг окружности равностороннего треугольника в сантиметрах")
print(t/100,"Длина стороны описанного вокруг окружности равностороннего треугольника в метрах")
o = (a*2*(sqrt(2)-1)) # формуда длины стороны описанного вокруг окружности правильного восьмиугольника
print(o, "Длина стороны описанного вокруг окружности правильного восьмиугольника в сантиметрах ")
print(o/100, "Длина стороны описанного вокруг окружности правильного восьмиугольника в метрах ")