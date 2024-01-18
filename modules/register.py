import numpy as np
from globals_module import *

class Register:
    def __init__(self) -> None:
        self.data = np.uint8(0)

    def read(self):
        global DataBus
        self.data = np.array(DataBus.read()).astype(dtype=np.uint8)
        if verbose: print('reg read', hex(DataBus.read()), '-->', hex(self.data))

    def writeData(self):
        global DataBus
        DataBus.write(self.data)
        if verbose: print('reg write', hex(self.data), '-->', hex(DataBus.read()))

    def writeAddLo(self):
        global AddressBus
        AddressBus.write((AddressBus.read() & np.uint16(0xFF00)) | np.uint8(self.data))
        if verbose: print('reg write addlo', hex(self.data), '-->', hex(AddressBus.read()))

    def writeAddHi(self):
        global AddressBus
        AddressBus.write((AddressBus.read() & np.uint16(0x00FF)) | (np.uint8(self.data) << 8))
        if verbose: print('reg write addhi', hex(self.data), '-->', hex(AddressBus.read()))