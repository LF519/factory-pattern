"""
接口隔离原则: 
    使用多个专门的接口, 而不使用单一的总接口, 即客户端不应该依赖于那些它不需要的接口.
单一职责原则:
    不要存在多于一个导致类变更的原因. 通俗地说, 即一个类只负责一项职责.
"""
from abc import ABCMeta, abstractmethod


class LandAnimal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        pass


class WaterAnimal(metaclass=ABCMeta):
    @abstractmethod
    def swim(self):
        pass


class SkyAnimal(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass


class Frog(LandAnimal, WaterAnimal):
    def walk(self):
        print("frog walk")

    def swim(self):
        print("frog swim")