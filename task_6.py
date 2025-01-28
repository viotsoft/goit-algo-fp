items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items: dict, budget: int) -> list:
    """
    Жадібний алгоритм (для порівняння з динамічним програмуванням):
    - Сортуємо страви за спаданням співвідношення 'калорії / вартість'.
    - Проходимо посортовані страви та додаємо в результат, 
      якщо залишок бюджету дозволяє взяти страву.
    - Кожну страву можна взяти не більше одного разу (0/1).
    """
    # Створимо список кортежів (назва, вартість, калорії, співвідношення калорій до вартості)
    items_list = [
        (name, data["cost"], data["calories"], data["calories"] / data["cost"])
        for name, data in items.items()
    ]
    # Сортуємо за спаданням співвідношення калорій до вартості
    items_list.sort(key=lambda x: x[3], reverse=True)

    chosen_items = []
    for name, cost, calories, ratio in items_list:
        if cost <= budget:
            chosen_items.append(name)
            budget -= cost

    return chosen_items


def dynamic_programming(items: dict, budget: int) -> list:
    """
    Алгоритм динамічного програмування для 0/1 Knapsack:
    Повертає список страв, що дає максимальну сумарну калорійність
    за умови, що кожну страву можна обрати не більше одного разу
    і загальна вартість не перевищує заданий бюджет.
    """
    # Перетворюємо вхідний словник у список для зручності індексації: (name, cost, calories)
    item_list = [(name, data["cost"], data["calories"]) for name, data in items.items()]
    n = len(item_list)

    # Створюємо таблицю dp, де dp[i][b] — максимально можливі калорії
    # при розгляді перших i страв і бюджеті b
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    # Заповнюємо таблицю dp
    for i in range(1, n + 1):
        name_i, cost_i, cal_i = item_list[i - 1]  # зсув на 1
        for b in range(budget + 1):
            # Випадок: не беремо i-ту страву
            dp[i][b] = dp[i - 1][b]
            # Якщо можна взяти i-ту страву, перевіряємо, чи покращить це результат
            if cost_i <= b:
                dp[i][b] = max(dp[i][b], dp[i - 1][b - cost_i] + cal_i)

    # У dp[n][budget] міститься максимальна сума калорій
    # Тепер «відкатуємося» (reconstruct), щоб визначити, які саме страви були взяті
    chosen_items = []
    b = budget
    i = n
    while i > 0 and b >= 0:
        if dp[i][b] == dp[i - 1][b]:
            # Страву не брали
            i -= 1
        else:
            # Страву брали
            name_i, cost_i, cal_i = item_list[i - 1]
            chosen_items.append(name_i)
            b -= cost_i
            i -= 1

    # Список обраних страв формується з кінця в початок, тому розвертаємо його
    chosen_items.reverse()
    return chosen_items


if __name__ == "__main__":
    test_budget = 100
    dp_result = dynamic_programming(items, test_budget)
    greedy_result = greedy_algorithm(items, test_budget)

    print(f"Бюджет: {test_budget}")
    print("Результат динамічного програмування (0/1 Knapsack):", dp_result)
    print("Результат жадібного алгоритму (0/1):", greedy_result)
