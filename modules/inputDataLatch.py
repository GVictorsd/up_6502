import numpy as np
from globals_module import *

class InputDataLatch:
    def __init__(self) -> None:
        self.data = np.uint8(0)

    def idlOp(self, op = 'r'):
        # Input data Latch - data bus operation
        global DataBus
        if op == 'r':
            self.data = DataBus.read()
            if verbose: print('idlread', hex(DataBus.read()), '-->', hex(self.data))
        elif op == 'w':
            DataBus.write(np.uint8(self.data))
            if verbose: print('idlop', hex(self.data), '-->', hex(DataBus.read()))

    def idlAddOpLo(self, op = 'r'):
        # Input data latch - address bus low byte operation
        global AddressBus
        if op == 'r':
            self.data = np.uint8(AddressBus.read())
            if verbose: print('idlAddOpLo read', hex(AddressBus.read()), '-->', hex(self.data))
        elif op == 'w':
            AddressBus.write((AddressBus.read() & np.uint16(0xFF00)) | np.uint8(self.data))
            if verbose: print('IdlAddOpLo write', hex(self.data), '-->', hex(AddressBus.read()))

    def idlAddOpHi(self, op = 'r'):
        # Input data latch - address bus high byte operation
        global AddressBus
        if op == 'r':
            self.data = (np.uint8(AddressBus.read() >> 8))
            if verbose: print('IdlAddOpHi read', hex(AddressBus.read()), '-->', hex(self.data))
        elif op == 'w':
            AddressBus.write((AddressBus.read() & np.uint16(0x00FF)) | (np.uint8(self.data) << 8))
            if verbose: print('IdlAddOpHi write', hex(self.data), '-->', hex(AddressBus.read()))
