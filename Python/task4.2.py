#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input("Введите целое число: "))
#for i in range(1, number+1):
#    if(number % i == 0):
#        print(i)
data = [x for x in range(1, number + 1)]
res = (list(filter(lambda x: number % x == 0,data)))
print(res)