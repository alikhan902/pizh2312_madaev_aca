import timeit
import random
import matplotlib.pyplot as plt


# ===== Часть 1. Базовая задача =====
def calculate_sum():
    """Считает сумму двух введенных чисел."""
    a = int(input("Введите первое число: "))  # O(1) - чтение и преобразование
    b = int(input("Введите второе число: "))  # O(1)
    result = a + b                            # O(1) - сложение
    print("Сумма:", result)                   # O(1) - вывод

    # Общая сложность функции: O(1)


# ===== Часть 2. Усложнённая задача =====
def sum_array(arr):
    """Возвращает сумму всех элементов массива.
    
    Сложность: O(N), где N - длина массива.
    """
    total = 0               # O(1)
    for num in arr:         # O(N)
        total += num        # O(1)
    return total            # O(1)
    # Общая сложность: O(N)


# ===== Часть 3. Замер времени =====
def measure_time(func, data):
    """Измеряет время выполнения функции (мс)."""
    start = timeit.default_timer()
    func(data)
    end = timeit.default_timer()
    return (end - start) * 1000  # миллисекунды


if __name__ == "__main__":
    # --- Базовая задача ---
    print("=== Базовая задача: сумма двух чисел ===")
    # calculate_sum()  # ← можно раскомментировать для запуска

    # --- Характеристики ПК (заполняются вручную) ---
    pc_info = """
    Характеристики ПК для тестирования:
    - Процессор: Intel Core i5-10200H @ 2.40GHz
    - Оперативная память: 16 GB DDR4
    - ОС: Windows 10
    - Python: 3.10
    """
    print(pc_info)

    # --- Усложнённая задача ---
    sizes = [1000, 5000, 10000, 50000, 100000, 500000]
    times = []

    print("=== Замеры времени выполнения суммирования массива ===")
    print(f"{'Размер N':>10} {'Время (мс)':>12} {'Время/N (мкс)':>15}")

    for size in sizes:
        # Генерация случайного массива заданного размера
        data = [random.randint(1, 1000) for _ in range(size)]

        # Замер времени (усреднение по 10 запускам)
        execution_time = timeit.timeit(lambda: sum_array(data), number=10) * 1000 / 10
        times.append(execution_time)

        time_per_element = (execution_time * 1000) / size
        print(f"{size:>10} {execution_time:>12.4f} {time_per_element:>15.4f}")

    # --- Построение графика ---
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, 'bo-', label="Измеренное время")
    plt.xlabel("Размер массива (N)")
    plt.ylabel("Время выполнения (мс)")
    plt.title("Зависимость времени выполнения от размера массива\nСложность: O(N)")
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.legend()
    plt.savefig("time_complexity_plot.png", dpi=300, bbox_inches="tight")
    plt.show()

    # --- Анализ результатов ---
    print("\nАнализ результатов:")
    print("1. Теоретическая сложность алгоритма: O(N)")
    print("2. Практические замеры показывают линейную зависимость времени от N")
    print("3. Время на один элемент примерно постоянно (в микросекундах)")