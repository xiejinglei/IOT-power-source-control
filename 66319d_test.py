from powerLib.DPIB_66319d import DPIB_66319d
import time


def test0():
    my66319d = DPIB_66319d()
    my66319d.set_voltage(10)
    my66319d.output_on()
    time.sleep(1)
    my66319d.output_off()


