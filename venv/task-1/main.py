

# возвращаем список результатов во 2ой степени
def square_func(power, *args):
    all_results = []
    for arg in args:
        all_results.append(arg**power)
    return all_results

# # возвращаем генератор
# def square_func_gen(*args):
#     return (arg**2 for arg in args)
# x_2 = square_func_gen(2, 3, 4)

x_1 = square_func(3, 2, 3, 4)


print(x_1)