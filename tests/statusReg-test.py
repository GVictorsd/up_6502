import unittest
import numpy as np
from modules.statusReg import statusRegister

class TestStatusRegister(unittest.TestCase):
    def setUp(self):
        self.sr = statusRegister()

    def test_carry(self):
        self.sr.carry(True)
        self.assertEqual(self.sr.data, np.uint8(0b00100001))
        self.sr.carry(False)
        self.assertEqual(self.sr.data, np.uint8(0b00100000))

    def test_zero(self):
        self.sr.zero(True)
        self.assertEqual(self.sr.data, np.uint8(0b00100010))
        self.sr.zero(False)
        self.assertEqual(self.sr.data, np.uint8(0b00100000))

    def test_irq(self):
        self.sr.irq(True)
        self.assertEqual(self.sr.data, np.uint8(0b00100100))
        self.sr.irq(False)
        self.assertEqual(self.sr.data, np.uint8(0b00100000))

    def test_decimalMode(self):
        self.sr.decimalMode(True)
        self.assertEqual(self.sr.data, np.uint8(0b00101000))
        self.sr.decimalMode(False)
        self.assertEqual(self.sr.data, np.uint8(0b00100000))

    def test_brk(self):
        self.sr.brk(True)
        self.assertEqual(self.sr.data, np.uint8(0b00110000))
        self.sr.brk(False)
        self.assertEqual(self.sr.data, np.uint8(0b00100000))

    def test_overflow(self):
        self.sr.overflow(True)
        self.assertEqual(self.sr.data, np.uint8(0b01100000))
        self.sr.overflow(False)
        self.assertEqual(self.sr.data, np.uint8(0b00100000))

    def test_negative(self):
        self.sr.negative(True)
        self.assertEqual(self.sr.data, np.uint8(0b10100000))
        self.sr.negative(False)
        self.assertEqual(self.sr.data, np.uint8(0b00100000))

if __name__ == '__main__':
    unittest.main()