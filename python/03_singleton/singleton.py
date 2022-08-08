"""
单例模式
内容: 保证一个类只有一个实例, 并提供一个访问它的全局访问点
角色:
    单例(Singleton)
优点:
    对唯一实例的受控访问
    单例相当于全局变量, 但防止了命名空间被污染
"""


class Singleton():
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            # 调用父类的__new__方法创建一个实例, 父类是Object
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class Myclass(Singleton):
    def __init__(self, a) -> None:
        self.a = a


x = Myclass(10)
y = Myclass(20)
print(x.a)
print(id(x))
print(y.a)
print(id(y))
