import turtle
import math

def draw_pythagoras_tree(t: turtle.Turtle, branch_length: float, angle: float, level: int) -> None:
    """
    Рекурсивно малює дерево Піфагора.
    :param t: Екземпляр черепашки для малювання
    :param branch_length: Довжина поточної гілки
    :param angle: Кут розгалуження
    :param level: Поточний рівень рекурсії
    """
    if level == 0:
        return

    t.forward(branch_length)
    t.left(angle)
    draw_pythagoras_tree(t, branch_length * math.cos(math.radians(angle)), angle, level - 1)
    t.right(2 * angle)
    draw_pythagoras_tree(t, branch_length * math.cos(math.radians(angle)), angle, level - 1)
    t.left(angle)
    t.backward(branch_length)

def main():
    """Головна функція програми."""
    # Валідація введення
    while True:
        try:
            level = int(input("Enter the recursion level (≥0): "))
            if level >= 0:
                break
            print("Level must be ≥0!")
        except ValueError:
            print("Please enter a valid integer!")

    branch_length = 100
    angle = 45

    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.setup(width=800, height=800)  # Збільшений розмір екрану

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()  # Сховати курсор
    t.left(90)
    t.up()
    t.backward(branch_length * (level + 1) / 2)  # Автоматичне позиціонування
    t.down()
    t.color("green")

    draw_pythagoras_tree(t, branch_length, angle, level)

    screen.mainloop()

if __name__ == "__main__":
    main()