import numpy as np

# Сравнение
a = np.array([1, 3, 0], float)
b = np.array([0, 3, 2], float)
# print(a > b)
# print(a > 2)

# any, all
c = np.array([True, False, False], bool)
any(c)  # True
all(c)  # False

# Сложные сравнения - logical_and, logical_or и logical_not
a = np.array([1, 3, 0], float)
# print(np.logical_and(a > 0, a < 3))

# Функция where создает новый массив из двух других массивов одинаковых длин
# используя булев фильтр для выбора межу двумя элементами.
# Если условие уддовлетворяется, берется элемент из 1го массива, если нет, то из 2го
a = np.array([1, 0, 4], float)
b = np.array([5, 3, 7, 8], float)
# print(np.where(np.logical_and(a != 0, b != 0), a, a))

# С функцией where так же может быть реализовано «массовое сравнение»
# print(a)
# a = np.array([1], int)
# print(np.where(a > 0, 3, 2))
# #
# Смотри гайд по WHERE !!!!!!!!
# https://numpy.org/doc/stable/reference/generated/numpy.where.html
# #

# take

a = np.array([2, 4, 6, 8], float)
b = np.array([0, 0, 1, 3, 2, 1], int)
a.take(b)  # a.take(b) == a[b]


# Векторная и матричная математика
# ...