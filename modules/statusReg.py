import numpy as np
from globals_module import *

class statusRegister:
    def __init__(self) -> None:
        self.data = np.uint8(0b00100000)

    def carry(self, value: bool):
        self.data = (self.data & np.uint8(0b11111110)) | value

    def zero(self, value: bool):
        self.data = (self.data & np.uint8(0b11111101)) | (np.uint8(value) << 1)

    def irq(self, value: bool):
        self.data = (self.data & np.uint8(0b11111011)) | (np.uint8(value) << 2)

    def decimalMode(self, value: bool):
        self.data = (self.data & np.uint8(0b11110111)) | (np.uint8(value) << 3)

    def brk(self, value: bool):
        self.data = (self.data & np.uint8(0b11101111)) | (np.uint8(value) << 4)

    def overflow(self, value: bool):
        self.data = (self.data & np.uint8(0b10111111)) | (np.uint8(value) << 6)

    def negative(self, value: bool):
        self.data = (self.data & np.uint8(0b01111111)) | (np.uint8(value) << 7)
