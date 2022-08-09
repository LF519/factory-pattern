"""
模板方法模式
内容:
    定义一个操作中的算法的骨架, 而将一些步骤延迟到子类中. 模板方法使得子类
    可以不改变一个算法的结构即可重新定义该算法的某些特定步骤
角色:
    抽象类(AbstractClass):
        定义抽象的原子操作(钩子操作); 实现一个模板方法作为算法的骨架
    具体类(ConcreteClass):
        实现原子操作
适用场景:
    一次性实现一个算法的不变的部分
    各个子类中的公共行为应该为提取出来并集到一个公共父类中以避免代码重复
    控制子类扩展
"""
from abc import ABC, abstractmethod
import time


class Window(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def repaint(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def run(self):
        """模板方法, 此方法作为骨架, 在子类中直接继承, 无需变化"""
        self.start()
        while True:
            try:
                self.repaint()
                time.sleep(1)
            except KeyboardInterrupt:
                break
        self.stop()


class MyWindow(Window):
    def __init__(self, msg):
        self.msg = msg

    def start(self):
        print("窗口开始运行")

    def stop(self):
        print("窗口结束运行")

    def repaint(self):
        print(self.msg)


MyWindow("Hello...").run()
