import itertools

class Operation():
    def __init__(self, ops):
        self.op = 1
        ops[self.op] = self

    def execute(self, arg, cpu):
        cpu.b ^= arg

class ElfComputer():
    def __init__(self):
        self.ops = dict()
        self.bxl = Operation(self.ops)
        self.b = 0

    def run(self, program):
        for instruction, argument in itertools.batched(program, 2):
            self.ops[instruction].execute(argument, self)
