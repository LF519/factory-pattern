"""
使用ABCMeta实现接口模式
接口: 若干抽象方法的集合
作用: 限制实现的接口的类必须按照接口给定的调用方式实现这些方法;
    对高层模块隐藏了类的内部实现
"""


from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    # 继承了Payment的类必须要实现pay方法
    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    def pay(self, money):
        print("支付宝支付%d元" % money)


class WechatPay(Payment):
    def pay(self, money):
        print("微信支付%d元" % money)


if __name__ == "__main__":
    p = Alipay()
    p.pay(20)
    p = WechatPay()
    p.pay(30)
