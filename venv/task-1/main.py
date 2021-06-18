from functools import wraps, lru_cache
import time


# 0.
# Декоратор для замера времени
def time_decorator(func):
    @wraps(func)  # необходимо, чтобы получать верную ссылку
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(time.time() - start_time)
        return result

    return wrapper


# возвращаем список результатов во N-ой степени
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


#########################################################

# 3.
# Дерократор, который показывает вложенные входы в функцию
def show_enter_info_deco(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(args)
        return func(*args, **kwargs)

    return wrapper


# 4.
# функция Фибоначчи
@lru_cache
@show_enter_info_deco
def fibonacci_func(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci_func(n - 1) + fibonacci_func(n - 2)


print(fibonacci_func(6))


# 5. Аналог lru_cache
# Если в словаре cache есть нужное значени, то мы его не вычисляем,
# а сразу отдаем в функцию fibonacci_func, если значения нет, то мы его вычисляем
def lru_cache_analog(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return cache[args]
        except KeyError:
            pass
        res = func(*args)
        cache[args] = res
        print(cache)
        return res

    return wrapper
