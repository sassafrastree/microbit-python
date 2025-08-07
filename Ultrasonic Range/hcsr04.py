from microbit import pin0, pin1
from machine import time_pulse_us

class HCSR04:
    def __init__(self, trig=pin0, echo=pin1):
        self.trig = trig
        self.echo = echo
        self.trig.write_digital(0)
        self.echo.read_digital()
        
    def read(self):
        self.trig.write_digital(1)
        self.trig.write_digital(0)
        dist_cm = time_pulse_us(self.echo, 1) * 0.01715
        return (dist_cm)
