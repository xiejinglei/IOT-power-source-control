import visa


class DPIB_66319d:

    def __init__(self, addr='GPIB0::5::INSTR'):
        rm = visa.ResourceManager()
        self.inst = rm.open_resource(addr)
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

    def check_error(self):
        print(self.inst.query("SYSTem:ERRor?"))
