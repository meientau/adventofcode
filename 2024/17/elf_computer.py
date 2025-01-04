import itertools

class OperationBxl():
    def __init__(self, ops):
        self.op = 1
        ops[self.op] = self

    def execute(self, arg, cpu):
        cpu.b ^= arg

class OperationBst():
    def __init__(self, ops):
        self.op = 2
        ops[self.op] = self

    def execute(self, arg, cpu):
        cpu.b = arg % 3

class ElfComputer():
    def __init__(self):
        self.ops = dict()
        self.bxl = OperationBxl(self.ops)
        self.bst = OperationBst(self.ops)
        self.b = 0

    def run(self, program):
        for instruction, argument in itertools.batched(program, 2):
            self.ops[instruction].execute(argument, self)
