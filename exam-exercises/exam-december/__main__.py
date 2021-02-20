from project.easter_shop import EasterShop
from project.factory.chocolate_factory import ChocolateFactory
from project.factory.egg_factory import EggFactory
from project.factory.paint_factory import PaintFactory

cf = ChocolateFactory('CF', 2)
ef = EggFactory('EF', 2)
pf = PaintFactory('PF', 2)

shop = EasterShop('Shop', cf, ef, pf)

print(cf.__dict__)
print(ef.__dict__)
print(pf.__dict__)
print(shop.__dict__)

