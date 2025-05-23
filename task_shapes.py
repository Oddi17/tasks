import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self)->float:
        raise NotImplementedError


class Circle(Shape):
    def __init__(self,radius:float):
        self.radius = radius
    def area(self)->float:
        return math.pi * (self.radius)**2

class Triangle(Shape):
    def __init__(self,a:float,b:float,c:float):
        self.a = a 
        self.b = b
        self.c = c
        self.p = (a+b+c)/2 #полупериметр
        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            raise ValueError("Такой треугольник не может существовать")
    
    def area(self)->float:
            return math.sqrt(self.p*(self.p-self.a)*(self.p-self.b)*(self.p-self.c))
    def check_rect(self)->bool:
        max_side = max(self.a,self.b,self.c)
        return self.a**2 + self.b**2 == max_side**2
    
