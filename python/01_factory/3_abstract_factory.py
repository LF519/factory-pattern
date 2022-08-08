"""
抽象工厂模式
内容: 定义一个工厂类接口, 让工厂子类来创建一系列相关或相互依赖的对象
角色:
    抽象工厂角色(Creator)
    具体工厂角色(Concrete Creator)
    抽象产品角色(Product)
    具体产品角色(Concrete Product)
    客户端(Client)
优点:
    将客户端与类的具体实现相分离
    每个工厂创建了一个完整的产品系列, 使得易于交换产品系列
    有利于产品的一致性(即产品之间的约束关系)
缺点:
    难以支持新种类的(抽象)产品
对比:
    相比工厂方法模式, 抽象工厂模式中的每个具体工厂都生产一套产品
"""
from abc import abstractmethod, ABCMeta


# ---------抽象产品----------

class PhoneShell(metaclass=ABCMeta):
    """
    手机壳
    """
    @abstractmethod
    def show_shell(self):
        pass


class CPU(metaclass=ABCMeta):
    """
    cpu
    """
    @abstractmethod
    def show_cpu(self):
        pass


class OS(metaclass=ABCMeta):
    """
    操作系统
    """
    @abstractmethod
    def show_os(self):
        pass


# ---------抽象工厂----------

class PhoneFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_shell(self):
        pass

    @abstractmethod
    def make_cpu(self):
        pass

    @abstractmethod
    def make_os(self):
        pass


# ---------具体产品----------

class SmallShell(PhoneShell):
    def show_shell(self):
        print("SmallShell")


class BigShell(PhoneShell):
    def show_shell(self):
        print("BigShell")


class AppleShell(PhoneShell):
    def show_shell(self):
        print("AppleShell")


class SmallShell(PhoneShell):
    def show_shell(self):
        print("SmallShell")


class SnapDragonCPU(CPU):
    def show_cpu(self):
        print("SnapDragonCPU")


class MediaTekCPU(CPU):
    def show_cpu(self):
        print("MediaTekCPU")


class AppleCPU(CPU):
    def show_cpu(self):
        print("AppleCPU")


class Android(OS):
    def show_os(self):
        print("Android")


class IOS(OS):
    def show_os(self):
        print("IOS")


# ---------具体工厂----------

class MiFactory(PhoneFactory):
    def make_cpu(self):
        return SnapDragonCPU()

    def make_os(self):
        return Android()

    def make_shell(self):
        return BigShell()


class Huaweiactory(PhoneFactory):
    def make_cpu(self):
        return MediaTekCPU()

    def make_os(self):
        return Android()

    def make_shell(self):
        return SmallShell()


class IPhoneFactory(PhoneFactory):
    def make_cpu(self):
        return AppleCPU()

    def make_os(self):
        return IOS()

    def make_shell(self):
        return AppleShell()


# ---------客户端----------

class Phone():
    def __init__(self, cpu, os, shell):
        self.cpu = cpu
        self.os = os
        self.shell = shell

    def show_info(self):
        print("手机信息")
        self.cpu.show_cpu()
        self.os.show_os()
        self.shell.show_shell()


def make_phone(factory: PhoneFactory) -> Phone:
    cpu = factory.make_cpu()
    os = factory.make_os()
    shell = factory.make_shell()
    return Phone(cpu, os, shell)


if __name__ == "__main__":
    p1 = make_phone(MiFactory())
    p1.show_info()
