import random
import matplotlib.pyplot as plt

# Заздалегідь визначимо кількість способів отримати кожну суму (2..12)
WAYS_TO_GET_SUM = {
    2: 1,  3: 2,  4: 3,  5: 4,  6: 5,
    7: 6,  8: 5,  9: 4, 10: 3, 11: 2, 12: 1
}
TOTAL_COMBINATIONS = 36  # 6 * 6

def simulate_dice_throws(num_throws=1_000_000):
    """
    Симулює кидки двох гральних кубиків.
    Повертає словник {сума: кількість появ}.
    """
    # Ініціалізуємо лічильник для сум від 2 до 12
    sum_counts = {s: 0 for s in range(2, 13)}

    for _ in range(num_throws):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice_sum = dice1 + dice2
        sum_counts[dice_sum] += 1

    return sum_counts

def compute_probabilities(sum_counts, num_throws):
    """
    Обчислює емпіричні ймовірності появи кожної суми.
    Повертає словник {сума: ймовірність}.
    """
    probabilities = {}
    for s in range(2, 13):
        probabilities[s] = sum_counts[s] / num_throws
    return probabilities

def print_probability_table(emp_probabilities):
    """
    Виводить таблицю, де порівнюються емпірична (Монте-Карло)
    та теоретична імовірності у форматі:
      - сумарна ймовірність у відсотках
      - (x/36) для теоретичної
    """
    print(f"{'Сума':^5} | {'Емпірична (Монте-Карло)':^26} | {'Теоретична':^26}")
    print("-" * 68)

    for dice_sum in range(2, 13):
        ways = WAYS_TO_GET_SUM[dice_sum]
        theoretical_prob = ways / TOTAL_COMBINATIONS
        empirical_prob = emp_probabilities[dice_sum]

        # Переводимо в відсотки
        theoretical_percent = theoretical_prob * 100
        empirical_percent = empirical_prob * 100

        print(
            f"{dice_sum:>4}  | "
            f"{empirical_percent:>5.2f}% ({emp_probabilities[dice_sum]:.4f})  | "
            f"{theoretical_percent:>5.2f}% ({ways}/{TOTAL_COMBINATIONS})"
        )

def plot_probabilities(empirical_probabilities):
    """
    Будує гістограму для порівняння емпіричних і теоретичних ймовірностей.
    """
    sums = list(range(2, 13))
    exp_vals = [empirical_probabilities[s] for s in sums]
    # Обчислимо теоретичні ймовірності за допомогою WAYS_TO_GET_SUM
    theo_vals = [WAYS_TO_GET_SUM[s] / TOTAL_COMBINATIONS for s in sums]

    plt.figure(figsize=(8, 5))
    # Зсунемо стовпчики, щоб вони не перекривалися
    plt.bar([s - 0.2 for s in sums], exp_vals, width=0.4, label='Монте-Карло', alpha=0.7)
    plt.bar([s + 0.2 for s in sums], theo_vals, width=0.4, label='Теоретична', alpha=0.7)

    plt.xticks(sums, sums)
    plt.xlabel('Сума на двох кубиках')
    plt.ylabel('Ймовірність')
    plt.title('Порівняння емпіричної та теоретичної ймовірностей (2 кубики)')
    plt.legend()
    plt.grid(axis='y', alpha=0.3)
    plt.show()

def main():
    # Кількість кидків для симуляції (змінюйте за потреби)
    num_throws = 1_000_000

    # 1. Запускаємо симуляцію
    sum_counts = simulate_dice_throws(num_throws)

    # 2. Обчислюємо емпіричні ймовірності
    empirical_probabilities = compute_probabilities(sum_counts, num_throws)

    # 3. Виводимо таблицю порівняння
    print_probability_table(emp_probabilities=empirical_probabilities)

    # 4. Будуємо графік для наочності
    plot_probabilities(empirical_probabilities)

if __name__ == "__main__":
    main()
