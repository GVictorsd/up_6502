import numpy as np

from globals_module import *
from modules.alu import ALU
from modules.register import Register


def main():
    print('verbose', verbose)

    global DataBus
    a = Register()
    printh(a.data)
    DataBus.write(np.uint8(0x42))
    a.read()
    printh(a.data)
    a.writeAddHi()
    printh(AddressBus.read())



def printb(a):
    print(bin(a))
def printh(a):
    print(hex(a))

if __name__ == '__main__':
    main()
