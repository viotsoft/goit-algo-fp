import turtle
import math

def draw_pythagoras_tree(t, branch_length, angle, level):
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
    level = int(input("Enter the recursion level: "))
    branch_length = 100
    angle = 45

    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    t.color("green")

    draw_pythagoras_tree(t, branch_length, angle, level)

    screen.mainloop()

if __name__ == "__main__":
    main()