import numpy as np

class DATABUS:
    def __init__(self) -> None:
        self.data = np.uint8(0)
        self.dataBusBuffer = np.uint8(0)

    def read(self):
        return self.data

    def write(self, data):
        self.data = data

    def bufferRead(self):
        self.data = self.dataBusBuffer

    def bufferWrite(self):
        self.dataBusBuffer = self.data

    def eval(self):
        pass


class ADDRESSBUS:
    def __init__(self) -> None:
        self.data = np.uint16(0)

    def read(self):
        return self.data

    def write(self, data):
        self.data = data


class CONTROLSIGNAL:
    def __init__(self) -> None:
        self.data = False
    def set(self):
        self.data = True
    def reset(self):
        self.data = False

DataBus = DATABUS()
AddressBus = ADDRESSBUS()
int8 = np.uint8
int16 = np.uint16

BE = CONTROLSIGNAL()

verbose = True