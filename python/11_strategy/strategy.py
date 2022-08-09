"""
策略模式
内容:
    定义一系列的算法, 把它们一个个地封装起来, 并且使它们可以互相替换.
    本模式使得算法可独立于使用它的客户而变化
角色:
    抽象策略(Strategy)
    具体策略(ConcreteStrategy)
    上下文(Context)
优点:
    定义了一系列可重用的算法和行为
    消除了一些条件语句
    可以提供相同行为的不同实现
缺点:
    客户必须了解不同的策略
"""
from abc import ABC, abstractmethod
from multiprocessing import context


class Strategy(ABC):
    @abstractmethod
    def execute(self, data):
        pass


class FastStrategy(Strategy):
    def execute(self, data):
        print("用较快的策略处理%s" % data)


class SlowStrategy(Strategy):
    def execute(self, data):
        print("用较慢的策略处理%s" % data)


class Context():
    """context可以隐藏一些内部属性"""
    def __init__(self, strategy, data):
        self.startegy = strategy
        self.data = data

    def set_strategy(self, strategy):
        self.startegy = strategy

    def do_strategy(self):
        self.startegy.execute(self.data)


# Client
data = "[数据]"
fs = FastStrategy()
context = Context(fs, data)
context.do_strategy()
ss = SlowStrategy()
context.set_strategy(ss)
context.do_strategy()
