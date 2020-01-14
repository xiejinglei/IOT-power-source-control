from powerLib.DPIB_66319d import DPIB_66319d
from powerLib.modbus_DPM8600 import modbus_DPM8600
import time


def setup_module(module):
    # Turn on DPM8600
    my66319d = DPIB_66319d()
    my66319d.set_voltage(10)
    my66319d.output_on()
    time.sleep(0.5)



def test_ouput():
    inst = modbus_DPM8600('COM3', 2)
    inst.output_on()
    time.sleep(1)
    inst.output_off()


def test_change_voltage():
    inst = modbus_DPM8600('COM3', 2)
    inst.set_voltage(3.5)
