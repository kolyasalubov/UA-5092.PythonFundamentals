import unittest
from tools.errors import TriangleSidesError
from task2 import calculate_rectangle_area, calculate_circle_area, calculate_triangle_area, validate_triangle_sides

class TestTask2Functions(unittest.TestCase):
    
    def test_function_calculate_rectangle_area(self):
        side1 = 10
        side2 = 4
        area = calculate_rectangle_area(side1, side2)
        self.assertEqual(area, 40.0)

    def test_function_calculate_circle_area(self):
        radius = 1
        area = calculate_circle_area(radius)
        self.assertEqual(area, 3.14)

    def test_function_calculate_triangle_area(self):
        side1 = 3
        side2 = 4
        side3 = 5
        area = calculate_triangle_area(side1, side2, side3)
        self.assertEqual(area, 6.0)

    def test_function_validate_triangle_sides_raises_error(self):
        side1 = 5
        side2 = 2
        side3 = 2
        with self.assertRaises(TriangleSidesError):
            validate_triangle_sides(side1, side2, side3)