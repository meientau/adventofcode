import itertools
from pprint import pprint


class ElfComputer():
    ops = list()

    def __init__(self):
        self.b = 0

    def run(self, program):
        for instruction, argument in itertools.batched(program, 2):
            self.ops[instruction].execute(argument, self)



def static_init(cls):
    if getattr(cls, "register", None):
        cls.register()
    return cls


class Operation():
    @classmethod
    def register(cls):
        setattr(ElfComputer, cls.__name__.lower(), len(ElfComputer.ops))
        ElfComputer.ops.append(cls())


@static_init
class Adv(Operation):
    def execute(self, arg, cpu):
        cpu.a //= 2**arg


@static_init
class Bxl(Operation):
    def execute(self, arg, cpu):
        cpu.b ^= arg


@static_init
class Bst(Operation):
    def execute(self, arg, cpu):
        cpu.b = arg % 3


@static_init
class Jnz(Operation): pass

@static_init
class Bxc(Operation): pass

@static_init
class Out(Operation): pass

@static_init
class Bdv(Operation): pass

@static_init
class Cdv(Operation): pass
