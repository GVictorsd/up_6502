import numpy as np

class DATABUS:
    def __init__(self) -> None:
        self.data = np.uint8(0)

    def read(self):
        return self.data

    def write(self, data):
        self.data = data


class ADDRESSBUS:
    def __init__(self) -> None:
        self.data = np.uint16(0)

    def read(self):
        return self.data

    def write(self, data):
        self.data = data



DataBus = DATABUS()
AddressBus = ADDRESSBUS()
int8 = np.uint8
int16 = np.uint16

verbose = True