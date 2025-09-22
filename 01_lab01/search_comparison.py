import timeit
import random
import matplotlib.pyplot as plt


# ===== Линейный поиск =====
def linear_search(arr, target):
    """Возвращает индекс элемента target или -1, если его нет.
    Сложность: O(n) в худшем случае.
    """
    for i in range(len(arr)):   # O(n)
        if arr[i] == target:    # O(1)
            return i            # O(1)
    return -1                   # O(1)
    # Общая сложность: O(n)


# ===== Бинарный поиск =====
def binary_search(arr, target):
    """Возвращает индекс элемента target или -1, если его нет.
    Сложность: O(log n) в худшем случае.
    """
    left, right = 0, len(arr) - 1  # O(1)
    while left <= right:           # O(log n) итераций
        mid = (left + right) // 2  # O(1)
        if arr[mid] == target:     # O(1)
            return mid             # O(1)
        elif arr[mid] < target:    # O(1)
            left = mid + 1         # O(1)
        else:
            right = mid - 1        # O(1)
    return -1                      # O(1)
    # Общая сложность: O(log n)


# ===== Функция для замеров времени =====
def measure_time(func, arr, target, repeats=5):
    """Измеряет среднее время выполнения функции (мс)."""
    execution_time = timeit.timeit(lambda: func(arr, target),
                                   number=repeats) * 1000 / repeats
    return execution_time


if __name__ == "__main__":
    # --- Характеристики ПК (заполнить вручную) ---
    pc_info = """
    Характеристики ПК для тестирования:
    - Процессор: Intel Core i5-10200H @ 2.40GHz
    - Оперативная память: 16 GB DDR4
    - ОС: Windows 10
    - Python: 3.10
    """
    print(pc_info)

    # --- Размеры массивов ---
    sizes = [1000, 5000, 10000, 50000, 100000, 500000, 1000000]
    linear_times = []
    binary_times = []

    print(f"{'Размер N':>10} {'Линейный (мс)':>15} {'Бинарный (мс)':>15}")

    for size in sizes:
        # Сгенерировать отсортированный массив
        arr = list(range(size))
        # Выбираем элемент (например, последний — худший случай для линейного поиска)
        target = size - 1

        # Замеры
        t_linear = measure_time(linear_search, arr, target)
        t_binary = measure_time(binary_search, arr, target)

        linear_times.append(t_linear)
        binary_times.append(t_binary)

        print(f"{size:>10} {t_linear:>15.6f} {t_binary:>15.6f}")

    # --- Построение графиков ---
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, linear_times, 'ro-', label="Линейный поиск O(n)")
    plt.plot(sizes, binary_times, 'bo-', label="Бинарный поиск O(log n)")
    plt.xlabel("Размер массива (N)")
    plt.ylabel("Время выполнения (мс)")
    plt.title("Сравнение линейного и бинарного поиска")
    plt.grid(True, linestyle="--", linewidth=0.5)
    plt.legend()
    plt.savefig("search_comparison_linear.png", dpi=300, bbox_inches="tight")
    plt.show()

    # --- График в логарифмическом масштабе ---
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, linear_times, 'ro-', label="Линейный поиск O(n)")
    plt.plot(sizes, binary_times, 'bo-', label="Бинарный поиск O(log n)")
    plt.xlabel("Размер массива (N)")
    plt.ylabel("Время выполнения (мс, log)")
    plt.yscale("log")   # логарифмическая шкала по y
    plt.title("Сравнение поисков (логарифмический масштаб)")
    plt.grid(True, linestyle="--", linewidth=0.5)
    plt.legend()
    plt.savefig("search_comparison_log.png", dpi=300, bbox_inches="tight")
    plt.show()

    # --- Анализ результатов ---
    print("\nАнализ результатов:")
    print("1. Линейный поиск растет пропорционально N (O(n)).")
    print("2. Бинарный поиск растет пропорционально log N (O(log n)).")
    print("3. Графики подтверждают теоретическую сложность.")
