import turtle


class Printer:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.printer = turtle.Turtle()
        self.printer.speed(0)
        self.printer.color("white")
        self.printer.penup()
        self.printer.hideturtle()
        self.printer.goto(self.x, self.y)

    def display(self, text, font_size=16):
        self.printer.clear()
        self.printer.write(text, align="center", font=("Courier", font_size, "normal"))

