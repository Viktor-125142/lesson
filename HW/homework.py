class Shape:
    def __init__(self, s):
        self.sides = s  # [1, 2, 3, 4]

    def __str__(self):
        return (
            "\nЭто фигура на плоскости.\nУ неё " + str(len(self.sides)) + " сторон(ы)"
        )

    def area(self):
        return "\nПлощадь фигуры невозможно определить\n"


class Rectangle(Shape):
    def __init__(self, s):
        super().__init__(s)

    def __str__(self):
        return "\nЭто прямоугольник\nсо сторонами " + str(self.sides)

    def area(self):
        return "\nПлощадь прямоугольника: " + str(self.sides[0] * self.sides[1])


class Triangle(Shape):
    def __init__(self, s):
        super().__init__(s)

    def __str__(self):
        return "\nЭто треугольник\nсо сторонами " + str(self.sides)

    def area(self):
        return "\nПлощадь треугольника: " + str((self.sides[0] * self.sides[1]) / 2)


class Square(Rectangle):
    def __init__(self, s):
        super().__init__(s)

    def __str__(self):
        return "\nЭто квадрат\nсо сторонами " + str(self.sides)

    def area(self):
        return "\nПлощадь квадрата: " + str(self.sides**2)


shape1 = Shape([1, 2, 3, 4])
shape2 = Rectangle([3, 4])
shape3 = Square(8)
shape4 = Triangle([12, 4, 10])

print(shape1, shape1.area())
print(shape2, shape2.area())
print(shape3, shape3.area())
print(shape4, shape4.area())
