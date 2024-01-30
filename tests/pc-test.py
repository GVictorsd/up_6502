# need to modify

import unittest
import numpy as np
from globals_module import *
from modules.pc import ProgramCounter

class TestProgramCounter(unittest.TestCase):
    def setUp(self):
        global DataBus, AddressBus
        self.DataBus = DataBus()
        self.AddressBus = AddressBus()
        self.pc = ProgramCounter()

    def test_pclOp_read(self):
        self.DataBus.write(np.uint8(123))
        self.pc.pclOp('r')
        self.assertEqual(self.pc.data, np.uint16(123))

    def test_pclOp_write(self):
        self.pc.data = np.uint16(123)
        self.pc.pclOp('w')
        self.assertEqual(self.DataBus.read(), np.uint8(123))

    def test_pchOp_read(self):
        self.DataBus.write(np.uint8(123))
        self.pc.pchOp('r')
        self.assertEqual(self.pc.data, np.uint16(123 << 8))

    def test_pchOp_write(self):
        self.pc.data = np.uint16(123 << 8)
        self.pc.pchOp('w')
        self.assertEqual(self.DataBus.read(), np.uint8(123))

    def test_pclAddOp_read(self):
        self.AddressBus.write(np.uint16(123))
        self.pc.pclAddOp('r')
        self.assertEqual(self.pc.data, np.uint16(123))

    def test_pclAddOp_write(self):
        self.pc.data = np.uint16(123)
        self.pc.pclAddOp('w')
        self.assertEqual(self.AddressBus.read(), np.uint16(123))

    def test_pchAddOp_read(self):
        self.AddressBus.write(np.uint16(123))
        self.pc.pchAddOp('r')
        self.assertEqual(self.pc.data, np.uint16(123 << 8))

    def test_pchAddOp_write(self):
        self.pc.data = np.uint16(123 << 8)
        self.pc.pchAddOp('w')
        self.assertEqual(self.AddressBus.read(), np.uint16(123))

    def test_pcAddOp_read(self):
        self.AddressBus.write(np.uint16(123))
        self.pc.pcAddOp('r')
        self.assertEqual(self.pc.data, np.uint16(123))

    def test_pcAddOp_write(self):
        self.pc.data = np.uint16(123)
        self.pc.pcAddOp('w')
        self.assertEqual(self.AddressBus.read(), np.uint16(123))

if __name__ == '__main__':
    unittest.main()