
import numpy as np
from globals_module import *

class ProgramCounter:
    def __init__(self) -> None:
        self.data = np.uint16(0)

    def pclOp(self, op = 'r'):
        global DataBus
        if op == 'r':
            self.data = (self.data & np.uint16(0xFF00)) | np.uint8(DataBus.read())
            if verbose: print('pclread', hex(DataBus.read()), '-->', hex(self.data))
        elif op == 'w':
            DataBus.write(np.uint8(self.data))
            if verbose: print('pclwrite', hex(self.data), '-->', hex(DataBus.read()))

    def pchOp(self, op = 'r'):
        global DataBus
        if op == 'r':
            self.data = (self.data & np.uint16(0x00FF)) | (np.uint8(DataBus.read()) << 8)
            if verbose: print('pchread', hex(DataBus.read()), '-->', hex(self.data))
        elif op == 'w':
            DataBus.write(np.uint8(self.data >> 8))
            if verbose: print('pclwrite', hex(self.data), '-->', hex(DataBus.read()))

    def pclAddOp(self, op = 'r'):
        global AddressBus
        if op == 'r':
            self.data = (self.data & np.uint16(0xFF00)) | np.uint8(AddressBus.read())
            if verbose: print('pclAddRead', hex(AddressBus.read()), '-->', hex(self.data))
        elif op == 'w':
            AddressBus.write((AddressBus.read() & np.uint16(0xFF00)) | np.uint8(self.data))
            if verbose: print('pclAddwrite', hex(self.data), '-->', hex(AddressBus.read()))

    def pchAddOp(self, op = 'r'):
        global AddressBus
        if op == 'r':
            self.data = (self.data & np.uint16(0x00FF)) | (np.uint8(AddressBus.read()) << 8)
            if verbose: print('pchAddread', hex(AddressBus.read()), '-->', hex(self.data))
        elif op == 'w':
            AddressBus.write((AddressBus.read() & np.uint16(0x00FF)) | (np.uint8(self.data) << 8))
            if verbose: print('pclAddwrite', hex(self.data), '-->', hex(AddressBus.read()))

    def pcAddOp(self, op = 'r'):
        global AddressBus
        if op == 'r':
            self.data = AddressBus.read()
            if verbose: print('pcAddread', hex(AddressBus.read()), '-->', hex(self.data))
        elif op == 'w':
            AddressBus.write(self.data)
            if verbose: print('pcAddwrite', hex(self.data), '-->', hex(AddressBus.read()))