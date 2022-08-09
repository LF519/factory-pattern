"""
观察者模式(发布-订阅者模式)
内容:
    定义对象间的一种一对多的依赖关系, 当一个对象的状态发生改变时, 所有依赖于它的对象都
    得到通知并被自动更新. 观察者模式又称"发布-订阅"模式
角色:
    抽象主题(Subject)
    具体主题(ConcreteSubject) -- 发布者
    抽象观察者(Observer)
    具体观察者(ConcreteObserver) -- 订阅者
适用场景:
    当一个抽象模型有两方面, 其中一个方面依赖于另一个方面.将这两者封装在独立对象中以使它们可以各自独立和复用
    当对一个对象的改变需要同时改变其他对象, 而不知道具体有多少对象有待改变
    当一个对象必须通知其他对象, 而它们又不是假定其它对象是谁. 换言之, 你不希望这些对象是紧密耦合的
优点:
    目标和观察者之间的抽象耦合最小
    支持广播通信
"""
from abc import ABC, abstractmethod


class Notice():
    """抽象发布者"""

    def __init__(self):
        self.observers = []

    def attach(self, obs):
        self.observers.append(obs)

    def detach(self, obs):
        self.observers.remove(obs)

    def notify(self):
        for obs in self.observers:
            obs.update(self)


class Observer(ABC):
    """抽象订阅者"""
    @abstractmethod
    def update(self, notice):  # notice是一个Notice类的对象
        pass


class StaffNotice(Notice):
    """具体发布者"""

    def __init__(self, company_info):
        super().__init__()
        self.__company_info = company_info

    @property
    def company_info(self):
        return self.__company_info

    @company_info.setter
    def company_info(self, info):
        self.__company_info = info
        # 当company_info发生变化时, 调用notify方法推送
        self.notify()


class Staff(Observer):
    """具体订阅者"""

    def __init__(self) -> None:
        self.company_info = None

    def update(self, notice: Notice):
        self.company_info = notice.company_info


# Client
notice = StaffNotice("初始公司信息")
s1 = Staff()
s2 = Staff()
notice.attach(s1)
notice.attach(s2)
print(s1.company_info)
notice.company_info = "发奖金!!!"
print(s1.company_info, s2.company_info)
notice.detach(s2)
notice.company_info = "明天放假!!!"
print(s1.company_info, s2.company_info)
