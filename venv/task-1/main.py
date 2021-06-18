# 1.
# возвращаем список результатов во 2ой степени
def square_func(power, *args) -> list:
    all_results = []
    for arg in args:
        all_results.append(arg ** power)
    return all_results


x_1 = square_func(3, 2, 3, 4)


# # возвращаем генератор
# def square_func_gen(*args):
#     return (arg**2 for arg in args)
# x_2 = square_func_gen(2, 3, 4)
##################################################

# 2.
# возвращаем четные/нечетные числа из списка
def get_numbers(nums: list, parity: bool) -> list:
    if parity:
        result_nums = [num for num in nums if num % 2 == 0]
    else:
        result_nums = [num for num in nums if num % 2 != 0]
    return result_nums


lst_get_numbers = get_numbers([2, 3, 4, 5, 6, 90, 91], parity = False)
print(lst_get_numbers)
