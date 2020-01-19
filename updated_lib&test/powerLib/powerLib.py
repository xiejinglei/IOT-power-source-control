# -*- coding: utf-8 -*-
# @Time    : 2020/1/15 9:57
# @Author  : Jinglei Xie


import serial
import visa
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
from abc import ABC, abstractmethod


# abstract class interface for power sources
class power(ABC):
    @abstractmethod
    def __init__(self, port, slave, baud=9600):
        pass

    @abstractmethod
    def output_on(self):
        pass

    @abstractmethod
    def output_off(self):
        pass

    @abstractmethod
    def set_voltage(self, voltage):
        pass

    @abstractmethod
    def __del__(self):
        pass


class power_66319d(power):
    def __init__(self, port='GPIB0::5::INSTR'):
        rm = visa.ResourceManager()
        self.inst = rm.open_resource(str(port))
        print('The following instrument has been connected:')
        print(self.inst.query('*IDN?'))
        self.inst.write('*RST')

    def output_on(self):
        self.inst.write('OUTPut1:STATe 1')

    def output_off(self):
        self.inst.write('OUTPut1:STATe 0')

    def set_voltage(self, voltage):
        vstr = str(voltage)
        cmd = 'VOLT ' + vstr
        self.inst.write(cmd)

    def __del__(self):
        pass


class power_DPM8600(power):
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
