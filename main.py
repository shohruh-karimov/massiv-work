import random

# Создаем одномерный массив случайных чисел
array = [random.randint(1, 100) for _ in range(10)]

# Находим наибольший элемент и его индекс
max_element = max(array)
max_index = array.index(max_element)

# Выводим результаты
print(f"Наибольший элемент: {max_element}")
print(f"Порядковый номер элемента: {max_index}")