"""
建造者模式
内容: 将一个复杂对象的构建与它的表示分离, 使得同样的构建过程可以创建不同的表示
角色:
    抽象建造者(Builder)
    具体建造者(Concrete Builder)
    指挥者(Director)
    产品(Product)
特点: 建造者模式与抽象工厂模式相似, 也用来创建复杂对象.主要区别是建造者模式从一
    步构造一个复杂对象, 而抽象工厂模式着重于多个系列的产品对象
优点:
    隐藏了一个产品的内部结构和装配过程
    将构造代码与表示代码分开
    可以对构造过程进行更精细的控制
"""
from abc import ABCMeta, abstractmethod


class Player():
    def __init__(self, face=None, body=None, arm=None, leg=None) -> None:
        self.face = face
        self.body = body
        self.arm = arm
        self.leg = leg

    def __str__(self) -> str:
        return "%s, %s, %s, %s" % (self.face, self.body, self.arm, self.leg)


class PlayBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_face(self) -> None:
        pass

    @abstractmethod
    def build_body(self) -> None:
        pass

    @abstractmethod
    def build_arm(self) -> None:
        pass

    @abstractmethod
    def build_leg(self) -> None:
        pass


class SexyGirlBuilder(PlayBuilder):
    def __init__(self) -> None:
        self.player = Player()

    def build_face(self) -> None:
        self.player.face = "漂亮的"

    def build_body(self) -> None:
        self.player.body = "苗条的"

    def build_arm(self) -> None:
        self.player.arm = "细长的"

    def build_leg(self) -> None:
        self.player.leg = "大长腿"


class MonsterBuilder(PlayBuilder):
    def __init__(self) -> None:
        self.player = Player()

    def build_face(self) -> None:
        self.player.face = "怪兽脸"

    def build_body(self) -> None:
        self.player.body = "臃肿的"

    def build_arm(self) -> None:
        self.player.arm = "长毛的"

    def build_leg(self) -> None:
        self.player.leg = "粗壮的"


class PlayDirector():
    def build_player(self, builder: PlayBuilder) -> Player:
        builder.build_body()
        builder.build_face()
        builder.build_arm()
        builder.build_leg()
        return builder.player


# client
builder = SexyGirlBuilder()
director = PlayDirector()
p = director.build_player(builder)
print(p)
