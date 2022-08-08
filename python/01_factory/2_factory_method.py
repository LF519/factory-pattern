"""
工厂方法模式
内容: 定义一个用于创建对象的接口(工厂接口), 让子类决定实例化哪一个产品类
角色:
    抽象工厂角色(Creator)
    具体工厂角色(Concrete Creator)
    抽象产品角色(Product)
    具体产品角色(Concrete Product)
优点:
    每个具体产品都对应一个具体工厂类, 不需要修改工厂类代码
    隐藏了对象创建的细节
缺点:
    每增加一个具体产品类, 就必须增加一个相应的具体工厂类
"""
from abc import ABCMeta, abstractmethod
from mimetypes import init


class Payment(metaclass=ABCMeta):
    """
    产品类接口
    """
    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    """
    Alipay产品类
    """

    def __init__(self, use_huabei=False):
        self.use_huabei = use_huabei

    def pay(self, money):
        if self.use_huabei:
            print("花呗支付%d元" % money)
            return
        print("支付宝支付%d元" % money)


class WechatPay(Payment):
    """
    Wechat产品类
    """

    def pay(self, money):
        print("微信支付%d元" % money)


class PaymnetFactory(metaclass=ABCMeta):
    """
    工厂类接口
    """
    @abstractmethod
    def create_payment(self):
        pass


class AlipayFactory(PaymnetFactory):
    """
    Alipay工厂类
    """

    def create_payment(self):
        return Alipay()


class WechatPayFactory(PaymnetFactory):
    """
    WechatPay工厂类
    """

    def create_payment(self):
        return WechatPay()


class HuabeiFactory(PaymnetFactory):
    """花呗工厂类"""

    def create_payment(self):
        return Alipay(use_huabei=True)


if __name__ == "__main__":
    pf = HuabeiFactory()
    p = pf.create_payment()
    p.pay(100)
