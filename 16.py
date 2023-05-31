
# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

N = int(input('Введите количество элементов в массиве  А: '))
A_mass = input("Введите элементы списка: ").split()

Num = list(map(int, A_mass))
if len(Num) != N:
    print('Введенные элементы не соответствуют заявленному количеству!')
else:
    X = int(input('Введите число X, которое необходимо найти в списке: '))
    count = 0
    for i in range(N):
        if Num[i] == X:
            count += 1
    print(f'Число {X} встречается в списке A {count} раз') 
    
    

    
    
