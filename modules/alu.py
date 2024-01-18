import numpy as np
from globals_module import *

class ALU:
    def __init__(self) -> None:
        self.Accumulator = np.uint8(0)

    def databusop(self, opcode):
        global DataBus
        if opcode == 'w':
            DataBus.write(self.Accumulator)
            if verbose: print('alu write', hex(self.Accumulator), '-->', hex(DataBus.read()))
        elif opcode == 'r':
            self.Accumulator = DataBus.read()
            if verbose: print('alu read', hex(DataBus.read()), '-->', hex(self.Accumulator))

    def addressbusop(self, opcode):
        global AddressBus
        if opcode == 'w':
            AddressBus.write(self.Accumulator)
            if verbose: print('alu write add', hex(self.Accumulator), '-->', hex(AddressBus.read()))
        elif opcode == 'r':
            self.Accumulator = AddressBus.read()
            if verbose: print('alu read add', hex(AddressBus.read()), '-->', hex(self.Accumulator))

    def op(self, opcode, operand):
        if operand == 'db':
            operand = DataBus.read()
        elif operand == 'ab':
            operand = AddressBus.read()

        if opcode == 0:
            self.Accumulator = self.Accumulator + operand
        elif opcode == 1:
            self.Accumulator = self.Accumulator - operand
        elif opcode == 2:
            self.Accumulator = self.Accumulator & operand
        elif opcode == 3:
            self.Accumulator = self.Accumulator | operand
        elif opcode == 4:
            self.Accumulator = self.Accumulator ^ operand
        elif opcode == 5:
            self.Accumulator = self.Accumulator << operand
        elif opcode == 6:
            self.Accumulator = self.Accumulator >> operand
        elif opcode == 7:
            self.Accumulator = self.Accumulator + 1
        elif opcode == 8:
            self.Accumulator = self.Accumulator - 1
        elif opcode == 9:
            self.Accumulator = self.Accumulator & 1
        elif opcode == 10:
            self.Accumulator = self.Accumulator | 1
        elif opcode == 11:
            self.Accumulator = self.Accumulator ^ 1
        elif opcode == 12:
            self.Accumulator = self.Accumulator << 1
        elif opcode == 13:
            self.Accumulator = self.Accumulator >> 1
        elif opcode == 14:
            self.Accumulator = ~self.Accumulator
        else:
            raise Exception("Invalid opcode")

        if verbose: print('alu op', hex(self.Accumulator))