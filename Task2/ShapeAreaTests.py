import math
import unittest
from Task2 import ShapeArea as sa

# При тестировании класса Shape будут вызываться методы и создание объектов классов Triangle и Circle,
# их отдельное тестирование не требуется


class TestShapeArea(unittest.TestCase):
    def setUp(self):
        self.eps = 1e-5


    def test_invalidTriangle_BigSide(self):
        triangle = sa.Shape(10, 1, 1)
        self.assertEqual(triangle.getArea(), None)

    def test_invalidTriangle_NegativeSide(self):
        triangle = sa.Shape(6, -8, 10)
        self.assertEqual(triangle.getArea(), None)

    def test_Triangle_IsNotValid_BigSide(self):
        triangle = sa.Triangle(2, 2, 10)
        self.assertFalse(triangle.isValid())

    def test_Triangle_IsNotValid_NegativeSide(self):
        triangle = sa.Triangle(6, -8, 10)
        self.assertFalse(triangle.isValid())

    def test_Triangle_IsValid(self):
        triangle = sa.Triangle(1, 2, 2)
        self.assertTrue(triangle.isValid())

    def test_Triangle_IsRight(self):
        triangle = sa.Triangle(6, 8, 10)
        self.assertTrue(triangle.isRight())

    def test_Triangle_IsNotRight(self):
        triangle = sa.Triangle(5, 8, 10)
        self.assertFalse(triangle.isRight())

    def test_validTriangle(self):
        triangle = sa.Shape(2, 3, 4)
        print(triangle.getArea())
        self.assertTrue(math.isclose(triangle.getArea(), 2.904738, rel_tol=self.eps))

    def test_RightTriangle(self):
        triangle = sa.Shape(6, 8, 10)
        self.assertTrue(math.isclose(triangle.getArea(), 24, rel_tol=self.eps))


    def test_InvalidCircle(self):
        circle = sa.Shape(-1)
        self.assertEqual(circle.getArea(), None)

    def test_ValidCircle(self):
        circle = sa.Shape(1)
        self.assertTrue(math.isclose(circle.getArea(), 3.141592, rel_tol=self.eps))

    def test_Circle_IsValid(self):
        circle = sa.Circle(1)
        self.assertEqual(circle.isValid, True)

    def test_Circle_NotValid(self):
        circle = sa.Circle(-1)
        self.assertEqual(circle.isValid, False)


if __name__ == "__main__":
  unittest.main()