"""
代理模式
内容: 为其他对象提供一种代理以控制这个对象的访问
应用场景:
    远程代理: 为远程的对象提供代理
    虚代理: 根据需要创建很大的对象
    保护代理: 控制原始对象的访问, 用于对象有不同访问权限时
"""


from abc import ABCMeta, abstractmethod


class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def set_content(self):
        pass


class RealSubject(Subject):
    def __init__(self, filename) -> None:
        self.filename = filename
        with open(filename, "r") as f:
            self.content = f.read()

    def get_content(self):
        return self.content

    def set_content(self, content):
        with open(self.filename, "w") as f:
            f.write(content)


# 虚代理
class VirtualProxy(Subject):
    """在读取或写入内容的时候才真正地创建对象"""
    def __init__(self, filename) -> None:
        self.filename = filename
        self.subj = None

    def get_content(self):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.get_content()

    def set_content(self, content):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        self.subj.set_content(content)


# 保护代理
class ProtectProxy(Subject):
    """当请求操作文件时报没有写权限"""
    def __init__(self, filename) -> None:
        self.subj = RealSubject(filename)

    def get_content(self):
        return self.subj.get_content()

    def set_content(self, content):
        raise PermissionError("没有写入权限")
        

# 远程代理类似于Django框架的ORM模式, 本地只管操作对象, 由代理去连接数据库
# 因为需要有全程操作, 在这里就不写远程代理相关的代码了

subj = VirtualProxy("test.txt")
content = subj.get_content()
print(content)

subj1 = VirtualProxy("test.txt")
subj1.set_content("456")
print(subj1.subj.content)

subj2 = ProtectProxy("test.txt")
content = subj2.get_content()
print(content)
subj2.set_content("123")  # 报错

