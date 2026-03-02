import time
from typing import List

# Декоратор - это функция, принимающая другую функцию и модифицирующая её
def runtime(func):
    def wrapper(*args, **kwargs):
        start_time = time.time() * 1000
        result = func(*args, **kwargs)
        end_time = time.time() * 1000

        print(f'Функция {func.__name__} выполнена за {round(end_time - start_time, 2)}мс')

        return result
    
    return wrapper

# Для применения декоратора используетс синтаксис @название_декоратора
@runtime
def swap(arr: List[int]) -> None:
    for i in range(len(arr) - 1):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]


@runtime
def bubble_sort(arr: List[int]) -> None:
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

if __name__ == "__main__":
    arr = [3, 6, 8, 10, 1, 2, 1] * 1000

    swap(arr)
    print(arr[:10])
    bubble_sort(arr)
    print(arr[:10])
