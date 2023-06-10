# КОНСПЕКТ =======================================================
# - название функции принято писать с маленькой буквы
# - функции можно передать неизвестное сначала количество параметров:
#       def function (*params):
#           for i in args:
#               res += i
#       return res
# 
#       function ("q", "w", "e", "r", "t", "y", "0")
# ПОСТАНОВКА ЗВЁЗДОЧКИ в списке аргументов обозначет, что в это место будет передан СПИСОК - работает ВЕЗДЕ

# Область видимости переменных или просто “Область видимости” (англ. variable scope или просто scope) — 
# это такая область программы, в пределах которой установлена связь между некоторой переменной и её 
# идентификатором (именем), по которому можно получить значение этой переменной

# ========== ЛЯМБДА lambda ФУНКЦИИ ==============
# пишется в 1 строчку
# в начале список ПЕРЕМЕННЫХ, потом ДВОЕТОЧИЕ, затем ВЫРАЖЕНИЕ с этими переменными
# (lambda x: x**2)

# МАР (функциональное программирование) - функция, в которую передается функция (ЛЯМБДА на месте 
# или другая, прописанная из вне)
# если есть ИТЕРИРУЕМЫЙ объект контейнер (может содержать разные объёкты в том числе 
# самого себя - словари и прочие коллекции), МАР преобразует каждый элемент из коллекции
# в соответствии с указанной функцией и возвращает НОВУЮ коллекцию с преобразованными элементами
# list(map(lambda item: (1 if item > 3 else item), scoreList))

# Подобным образом работают другие ФУНКЦИИ ВЫСШЕГО ПОРЯДКА (функции, которая принимает другие 
# функции в качестве аргументов) filter(), reduce(), max()

# Функция filter() в Python принимает в качестве аргументов функцию и список.
# Функция вызывается со всеми элементами в списке, и в результате возвращается новый 
# список, содержащий элементы, для которых функция результирует в True.
# new_list = list(filter(lambda x: (x%2 == 0) , my_list))

# Функция reduce() принимает в качестве аргументов функцию и список. Функция вызывается 
# с помощью лямбда-функции и итерируемого объекта  и возвращается новый уменьшенный результат. 
# Так выполняется повторяющаяся операцию над парами итерируемых объектов. 
# Функция reduce() входит в состав модуля functools.
# summa = reduce((lambda x, y: x + y), current_list)


#  ЗАДАЧА =======================================================
# У вас есть код, который вы не можете менять(так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.

# def transformation(values):
#     return list(map(lambda x: x, values))

# values = [1,2,3,4]
# transformed_values = transformation(values)
# print(transformed_values)


# ЗАДАЧА =========================================================
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна

# from math import pi as PI

# def find_farthest_orbit(list_of_orbits):
#     maxArea = 0
#     a,b = list_of_orbits[1]

#     # for orbit in list_of_orbits:
#     #     a, b = orbit
#     #     if a != b:
#     #         currentArea = PI * a * b
#     #         if currentArea > maxArea:
#     #                 maxArea = currentArea
#     #                 farest = orbit
#     # return farest
    
    

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(find_farthest_orbit(orbits))
# print(sum(orbits))


# from math import pi

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# p = max(orbits, key=lambda x: (x[0] != x[1]) * x[0] * x[1]*pi)
# print(p)

list_1 = [1,2,2,2,1,1,4,3,3,3,4,4,4,3,4]

for item in sorted(set(list_1)):
    print(f"элемент {item} имеет {list_1.count(item) // 2} пар")

