class Base:
    module_name = "Base"

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.module_name}: {self.name}"


class Base1(Base):
    module_name = "Base1"


class Base2(Base):
    module_name = "Base2"


class Base3(Base):
    module_name = "Base3"


class Module12(Base1, Base2):
    """Extend 1, 2"""


class Module23(Base2, Base3):
    """Extend 1, 2"""

m12 = Module12("Firas")
print(m12)
print([each.__name__ for each in Module12.mro()])