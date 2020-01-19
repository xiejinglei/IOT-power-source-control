from powerLib import powerLib
import time

power_inst = powerLib.power_66319d()
power_inst.set_voltage(10)
time.sleep(1)
power_inst.output_on()

power2 = powerLib.power_DPM8600('COM3', 2)
time.sleep(2)
power2.set_voltage(2.5)
time.sleep(2)
power2.output_on()
time.sleep(2)
power2.output_off()
time.sleep(2)

time.sleep(1)
power_inst.output_off()
