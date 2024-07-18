import math

# Для добавления новых фигур необходимо создать класс, наследуемый от интерфейса ShapeInterface и реализовать
# в нем функцию getArea, возвращающую площадь фигуры
# Для поддержки новых фигур классом Shape необходимо добавить в метод __init__ проверку на другие типы фигур по кол-ву параметров
class ShapeInterface:
    """
    Интерфейс для объекта фигуры с вычисляемой площадью
    """
    def getArea(self, *args):
        """
        Нахождение плозади фигуры
        :param args: Информация об измерениях фигуры, необходимая для нахождения площади
        """
        pass

# "Вычисление площади фигуры без знания типа фигуры в compile-time" - я поняла это так, можно создать либо
# класс круга/треугольника и напрямую в нем вызывать поиск площади, либо создать объект класса Shape, который
# на основе количества введенных параметров сам решает, что это за фигура и потом вызывает поиск площади из ее класса
class Shape(ShapeInterface):
    """
    Класс абстрактной фигуры
    """
    def __init__(self, *args):
        self.shapeIsValid = True

        if len(args) == 1:
            self.shape = Circle(*args)
        elif len(args) == 3:
            self.shape = Triangle(*args)
        else:
            self.shapeIsValid = False
            print("Данный тип фигуры не поддерживается, вычислить площадь будет невозможно.")
    def getArea(self) -> float:
        """
        Вычисление площади фигуры из двух доступных вариантов - круг и треугольник
        :return: Площадь фигуры (float)
        """
        if self.shapeIsValid:
            return self.shape.getArea()
        else:
            print("Невозможно вычислить площадь данной фигуры.")


class Circle(ShapeInterface):
    """
    Класс круга
    """
    def __init__(self, radius: float):

        if radius > 0:
            self.radius = radius
            self.isValid = True
        else:
            self.isValid = False
            print("Круг с радиусом меньше или равным нулю не может существовать.")

    def getArea(self) -> float:
        """
        Вычисление площади круга по радиусу, если круг существует
        :return: Площадь (float) или None
        """
        if self.isValid:
            return self.radius * self.radius * math.pi
        else:
            print("Невозможно вычислить площадь данного круга.")


class Triangle(ShapeInterface):
    """
    Класс треугольника
    """
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def isValid(self) -> bool:
        """
        Проверка существования треугольника
        :return: bool
        """
        max_side = max(self.a, self.b, self.c)
        return max_side < (sum([self.a, self.b, self.c]) - max_side) and (self.a > 0 and self.b > 0 and self.c > 0)

    def isRight(self) -> bool:
        """
        Проверка прямоугольности треугольника
        :return: bool
        """
        # a * a работает быстрее a**2
        # Для сравнения чисел с плавающей точкой - math.isclose
        eps = 1e-5
        return ((math.isclose((self.a * self.a + self.b * self.b), (self.c * self.c), rel_tol=eps)) or
                (math.isclose((self.c * self.c + self.b * self.b), (self.a * self.a), rel_tol=eps)) or
                (math.isclose((self.a * self.a + self.c * self.c), (self.b * self.b), rel_tol=eps)))

    def getArea(self) -> float or None:
        """
        Вычисление площади треугольника при его существовании
        :return: Площадь (float) или None при невозможности вычислить площадь
        """
        # Проверка на валидность треугольника
        if self.isValid():
            # Проверка на прямоугольность треугольника
            if self.isRight():
                sides = [self.a, self.b, self.c]
                sides.remove(max(sides))
                return sides[0]*sides[1]/2

            p = (self.a+self.b+self.c)/2
            return (p*(p - self.a)*(p - self.b)*(p - self.c))**0.5
        else:
            print("Треугольник не может существовать, вычислить площадь невозможно")


test_triangle = Shape(6, 8, 10)
print("Площадь треугольника: ", test_triangle.getArea())

test_circle = Shape(1)
print("Площадь круга: ", test_circle.getArea())