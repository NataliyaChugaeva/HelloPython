#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#Пример:
#- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


from math import factorial


number = int(input('Введите положительное число: '))

factorial = 1

if number < 0:
    print('Условие не выполнено!')
if number == 0:
    print('Произведение чисел равно 0')  
else:
    for i in range (1, number + 1):
        factorial = factorial * i        

print('Произведение чисел от 1 до',number,'равно',factorial )    

    
         
