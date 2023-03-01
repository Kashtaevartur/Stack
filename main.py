import threading
import random
import time

# Определение функций для потоков
def thread_function_1(nums):
    for i in range(20):
        nums.append(random.randint(1, 15))
    print("Список заполнен.")
    time.sleep(3)  # Перерыв 3 секунды
    thread_2 = threading.Thread(target=thread_function_2, args=(nums,))
    thread_3 = threading.Thread(target=thread_function_3, args=(nums,))
    thread_2.start()
    thread_3.start()
    thread_2.join()
    thread_3.join()

def thread_function_2(nums):
    avg = sum(nums) / len(nums)
    print(f"Среднее арифметическое: {avg}")

def thread_function_3(nums):
    total = sum(nums)
    print(f"Сумма всех элементов: {total}")

# Создание пустого списка для чисел
nums = []

# Создание первого потока
thread_1 = threading.Thread(target=thread_function_1, args=(nums,))

# Запуск первого потока
thread_1.start()

# Ожидание завершения первого потока
thread_1.join()

# Вывод списка чисел
print(nums)