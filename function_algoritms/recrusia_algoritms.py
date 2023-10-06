def factorial(x):
 
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
 
 
num = int(input("Введите число для нахождение факториала:"))

print("Факториал числа", num, "это", factorial(num))

