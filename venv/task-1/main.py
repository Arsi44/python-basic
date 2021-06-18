from functools import wraps
import time


# 0.
# Декоратор для замера времени
def time_decorator(func):
    @wraps(func)  # необходимо, чтобы получать верную ссылку (см аргумент true_link).
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(time.time() - start_time)
        return result

    return wrapper


# возвращаем список результатов во 2ой степени
@time_decorator
def square_func(power, *args) -> list:
    all_results = []
    for arg in args:
        all_results.append(arg ** power)
    return all_results


# 2.
# возвращаем четные/нечетные числа из списка
@time_decorator
def get_numbers(nums: list, parity: bool) -> list:
    if parity:
        result_nums = [num for num in nums if num % 2 == 0]
    else:
        result_nums = [num for num in nums if num % 2 != 0]
    return result_nums


square_func(1, 3)
get_numbers([1, 2, 3], parity=True)

true_link = get_numbers
print(true_link)
