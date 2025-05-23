import math
import pytest
from task_shapes import Shape, Circle, Triangle

def test_shape_cannot_be_instantiated():
    with pytest.raises(TypeError):
        Shape()

def test_circle_area():
    c = Circle(3)
    expected_area = math.pi * 3**2
    assert math.isclose(c.area(), expected_area, rel_tol=1e-9)

def test_triangle_invalid_sides():
    with pytest.raises(ValueError):
        Triangle(1, 2, 10)  # Невозможный треугольник

def test_triangle_area():
    t = Triangle(3, 4, 5)
    assert math.isclose(t.area(), 6.0, rel_tol=1e-9)

def test_triangle_check_rect_true():
    t = Triangle(3, 4, 5)
    assert t.check_rect() == True

def test_triangle_check_rect_false():
    t = Triangle(3, 3, 3)
    assert t.check_rect() == False