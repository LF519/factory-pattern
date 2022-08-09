"""
组合模式
内容:
    将对象组合成以树形结构表示"部分-整体"的层次结果. 组合模式使得用户对单个对象和组合对象的使用具有一致性
角色:
    抽象组件(Component)
    叶子组件(Leaf)
    复合组件(Composite)
    客户端(Client)
适用场景:
    表示对象的"部分-整体"层次结构(特别是结构是递归的)
    希望用户忽略组合对象与单个对象的不同, 用户统一地使用组合结构中的所有对象
优点:
    定义了包含基本对象和组合对象的类层次结构
    简化客户端代码, 即客户端可以一致地使用组合对象和单个对象
    更容易增加新类型的组件
"""
from abc import ABCMeta, abstractmethod


# 抽象组件
class Graphic(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass


# 叶子主件
class Point(Graphic):
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return "点(%s, %s)" % (self.x, self.y)

    def draw(self):
        print(self)


# 叶子组件
class Line(Graphic):
    def __init__(self, p1: Point, p2: Point) -> None:
        self.p1 = p1
        self.p2 = p2

    def __str__(self) -> str:
        return "线段[%s, %s]" % (self.p1, self.p2)

    def draw(self):
        print(self)


# 复合组件, 由多个叶子组件组成
class Picture(Graphic):
    def __init__(self, iterable) -> None:
        self.children = []
        for g in iterable:
            self.add(g)

    def add(self, graphic):
        self.children.append(graphic)

    def __str__(self) -> str:
        return "线段[%s, %s]" % (self.p1, self.p2)

    def draw(self):
        print("-------start draw 复合图形--------")
        for g in self.children:
            g.draw()
        print("-------end draw 复合图形--------")


if __name__ == "__main__":
    # 客户端
    p1 = Point(1, 3)
    p1.draw()
    l1 = Line(Point(1, 2), Point(3, 4))
    l1.draw()
    l2 = Line(Point(1, 3), Point(2, 4))
    l2.draw()
    pic1 = Picture([l1, p1, l2])
    pic1.draw()

    pic2 = Picture([pic1, l1, p1])
    pic2.draw()
