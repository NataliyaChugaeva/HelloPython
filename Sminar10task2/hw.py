#Во входной строке записана последовательность чисел через пробел.
#Для каждого числа выведите слово YES (в отдельной строке),
#если это число ранее встречалось в последовательности или NO, если не встречалось



L = [int(i) for i in input().split()]
S = set()
for i in L:
    if i in S:
        print('YES')
    else:
        print('NO')
    S.add(i)






