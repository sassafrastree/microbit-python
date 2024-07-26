class Joystick:
    def __init__(self, y, x, button):
        x.set_analog_period(20)
        y.set_analog_period(20)
        self.x = x.read_analog() - 420
        self.y = y.read_analog() - 420
        self.button = button.read_digital()
