import serial
import logging

import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu


class modbus_DPM8600:

    def __init__(self, com, slave, baud=9600):
        self.slave = int(slave)
        ser = serial.Serial(str(com), baud, bytesize=8, parity='N', stopbits=1)
        self.master = modbus_rtu.RtuMaster(ser)
        self.master.set_timeout(5.0)
        self.master.set_verbose(True)

    def output_on(self):
        self.master.execute(self.slave, cst.WRITE_SINGLE_REGISTER, 0x0002, 2, output_value=1)

    def output_off(self):
        self.master.execute(self.slave, cst.WRITE_SINGLE_REGISTER, 0x0002, 2, output_value=0)

    def set_voltage(self, volatge):
        v = int(100*float(volatge))
        self.master.execute(self.slave, cst.WRITE_SINGLE_REGISTER, 0x0000, 2, output_value=v)

    def __del__(self):
        self.master.close()
