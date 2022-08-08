"""
简单工厂模式
内容: 不直接像客户端暴露对象创建的细节, 而是通过一个工厂类来负责创建产品类的实例
角色:
    工厂角色(Creator)
    抽象产品角色(Product)
    具体产品角色(Concrete Product)
优点:
    隐藏了对象创建实现的细节
    客户端不需要修改代码
缺点:
    违反了单一职责原则, 将创建逻辑集中到一个工厂类里
    当添加新产品是, 需要修改工厂类代码, 违反了开闭原则
"""
from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    def pay(self, money):
        print("支付宝支付%d元" % money)


class WechatPay(Payment):
    def pay(self, money):
        print("微信支付%d元" % money)


class PaymnetFactory():
    """
    工厂类
    """
    def create_payment(self, method):
        if method == "alipay":
            return Alipay()

        elif method == "wechat":
            return WechatPay()

        else:
            raise TypeError("No such payment %s" % method)

if __name__ == "__main__":
    pf = PaymnetFactory()
    ap = pf.create_payment("alipay")
    ap.pay(100)
