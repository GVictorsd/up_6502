
import numpy as np
from globals_module import *
from modules.register import Register

class stackPointer(Register):
    def __init__(self) -> None:
        super().__init__()
        self.data = np.uint8(0x80)

    def read(self):
        global DataBus
        self.data = np.array(DataBus.read()).astype(dtype=np.uint8)
        self.data = (self.data | np.uint8(0x80))
        if verbose: print('stack pointer read', hex(DataBus.read()), '-->', hex(self.data))