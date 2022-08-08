"""
桥模式
内容: 将一个事物的两个维度分离, 使其都可以独立地变化
角色:
    抽象(Abstraction)
    细化抽象(RefinedAbstraction)
    实现者(Implementor)
    具体实现者(ConcreteImplementor)
应用场景:
    当事物有两个维度上的表现, 两个维度都可能扩展时
优点:
    抽象和实现相分离
    优秀的扩展能力
"""
from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    """图形接口, 抽象"""

    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass


class Color(metaclass=ABCMeta):
    """颜色接口, 实现者"""
    @abstractmethod
    def paint(self, shape):
        pass


# -------细化抽象--------
class Rectangle(Shape):
    name = "长方形"

    def draw(self):
        self.color.paint(self)


class Line(Shape):
    name = "直线"

    def draw(self):
        self.color.paint(self)


class CirCle(Shape):
    name = "圆形"

    def draw(self):
        self.color.paint(self)


# -------具体实现者--------
class Red(Color):
    def paint(self, shape):
        print("红色的%s" % shape.name)


class Green(Color):
    def paint(self, shape):
        print("绿色的%s" % shape.name)


if __name__ == "__main__":
    shape = Line(Red())
    shape.draw()

    shape2 = CirCle(Green())
    shape2.draw()
