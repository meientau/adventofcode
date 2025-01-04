import unittest

from elf_computer import ElfComputer

class OpCodeTes(unittest.TestCase):
    # The adv instruction (opcode 0) performs division. The numerator
    # is the value in the A register. The denominator is found by
    # raising 2 to the power of the instruction's combo operand. (So,
    # an operand of 2 would divide A by 4 (2^2); an operand of 5 would
    # divide A by 2^B.) The result of the division operation is
    # truncated to an integer and then written to the A register.
    def test_adv(self):
        cpu = ElfComputer()

        x = 67
        y = 2
        r = x // (2**y)
        program = [cpu.adv, y]

        cpu.a = x
        cpu.run(program)

        self.assertEqual(r, cpu.a)

    # The bxl instruction (opcode 1) calculates the bitwise XOR of
    # register B and the instruction's literal operand, then stores
    # the result in register B.
    def test_bxl(self):
        cpu = ElfComputer()

        x = 0b001011
        y = 0b011010
        r = 0b010001
        program = [cpu.bxl, y]

        cpu.b = x
        cpu.run(program)

        self.assertEqual(r, cpu.b)

    # The bst instruction (opcode 2) calculates the value of its combo
    # operand modulo 8 (thereby keeping only its lowest 3 bits), then
    # writes that value to the B register.
    def test_bst(self):
        cpu = ElfComputer()

        y = 0b011010
        r = 0b000010
        program = [cpu.bst, y]

        cpu.run(program)

        self.assertEqual(r, cpu.b)

    # The jnz instruction (opcode 3) does nothing if the A register is
    # 0. However, if the A register is not zero, it jumps by setting
    # the instruction pointer to the value of its literal operand; if
    # this instruction jumps, the instruction pointer is not increased
    # by 2 after this instruction.

    # The bxc instruction (opcode 4) calculates the bitwise XOR of
    # register B and register C, then stores the result in register
    # B. (For legacy reasons, this instruction reads an operand but
    # ignores it.)

    # The out instruction (opcode 5) calculates the value of its combo
    # operand modulo 8, then outputs that value. (If a program outputs
    # multiple values, they are separated by commas.)

    # The bdv instruction (opcode 6) works exactly like the adv
    # instruction except that the result is stored in the B
    # register. (The numerator is still read from the A register.)

    # The cdv instruction (opcode 7) works exactly like the adv
    # instruction except that the result is stored in the C
    # register. (The numerator is still read from the A register.)

    # If register C contains 9, the program 2,6 would set register B to 1.

    # If register A contains 10, the program 5,0,5,1,5,4 would output 0,1,2.

    # If register A contains 2024, the program 0,1,5,4,3,0 would output 4,2,5,6,7,7,7,7,3,1,0 and leave 0 in register A.

    # If register B contains 29, the program 1,7 would set register B to 26.

    # If register B contains 2024 and register C contains 43690, the program 4,0 would set register B to 44354.
