import itertools
from pprint import pprint


class ElfComputer():
    ops = list()

    def __init__(self):
        self.pc = 0
        self.a = 0
        self.b = 0
        self.c = 0

    def run(self, program):
        while 0 <= self.pc < len(program):
            instruction = program[self.pc]
            argument = self.interpret_arg(program[self.pc+1])
            self.pc += 2
            self.ops[instruction].execute(argument, self)

    def interpret_arg(self, argument):
        if argument < 4:
            return argument

        if argument >= 7:
            raise ValueError

        return [self.a, self.b, self.c][argument-4]


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
        print(f"{arg=}")
        cpu.b = arg % 8


@static_init
class Jnz(Operation):
    def execute(self, arg, cpu):
        if cpu.a:
            cpu.pc = arg

@static_init
class Bxc(Operation): pass

@static_init
class Out(Operation): pass

@static_init
class Bdv(Operation): pass

@static_init
class Cdv(Operation): pass
