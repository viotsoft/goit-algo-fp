items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def dynamic_programming_01_knapsack(items: dict, budget: int) -> list:
    """
    Алгоритм динамічного програмування під задачу 0/1 Knapsack:
    Повертає список страв, що дає максимальну сумарну калорійність
    при умові, що кожну страву можна обрати не більше одного разу.
    """
    # Переведемо словник у список для зручності індексації:
    # item_list[i] = (name, cost, calories)
    item_list = [(name, data["cost"], data["calories"]) for name, data in items.items()]
    n = len(item_list)

    # Створюємо 2D-таблицю dp, де dp[i][b] — максимальні калорії
    # при розгляді перших i страв і бюджеті b
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    # Заповнюємо dp
    for i in range(1, n + 1):
        name_i, cost_i, cal_i = item_list[i-1]  # i-1 через зсув індекса
        for b in range(budget + 1):
            # Не беремо i-ту страву:
            dp[i][b] = dp[i-1][b]
            # Якщо можемо взяти i-ту страву, перевіряємо, чи покращить це результат
            if cost_i <= b:
                dp[i][b] = max(dp[i][b], dp[i-1][b - cost_i] + cal_i)

    # В dp[n][budget] — оптимальна кількість калорій
    # Відновлюємо (reconstruct) вибрані страви
    chosen_items = []
    b = budget
    i = n
    while i > 0 and b >= 0:
        # Якщо калорії ті ж самі, що й без i-ї страви, то її не брали
        if dp[i][b] == dp[i-1][b]:
            i -= 1
        else:
            # Страву взяли
            name_i, cost_i, cal_i = item_list[i-1]
            chosen_items.append(name_i)
            b -= cost_i
            i -= 1

    # Порядок у chosen_items зараз з кінця до початку, можна розвернути, якщо треба
    chosen_items.reverse()
    return chosen_items


def greedy_algorithm(items: dict, budget: int) -> list:
    """
    Жадібний алгоритм (для порівняння):
    - Сортуємо за спаданням калорій/вартість.
    - Беремо страви, поки вистачає бюджету.
    Для 0/1 задачі жадібний підхід не гарантує оптимальності,
    але продемонструє різницю з DP.
    """
    # Створимо список кортежів (назва, вартість, калорії, співвідношення)
    items_list = [
        (name, data["cost"], data["calories"], data["calories"] / data["cost"])
        for name, data in items.items()
    ]
    # Сортуємо за спаданням співвідношення калорій до вартості
    items_list.sort(key=lambda x: x[3], reverse=True)

    chosen_items = []
    for name, cost, calories, ratio in items_list:
        # Для 0/1 knapsack ми можемо взяти цей пункт лише 1 раз
        if cost <= budget:
            chosen_items.append(name)
            budget -= cost

    return chosen_items

if __name__ == "__main__":
    test_budget = 100
    dp_result_01 = dynamic_programming_01_knapsack(items, test_budget)
    greedy_result = greedy_algorithm(items, test_budget)

    print(f"Бюджет: {test_budget}")
    print("Результат динамічного програмування (0/1 Knapsack):", dp_result_01)
    print("Результат жадібного алгоритму (0/1 підхід):", greedy_result)

