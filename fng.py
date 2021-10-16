import time
import board
import pwmio
from digitalio import DigitalInOut, Direction, Pull

class Fng:
    def __init__(self, pwm_pin, cw_pin, ccw_pin):
        self.pwm_pin = pwm_pin
        #self.cw_pin = Pin(cw_pin, Pin.OUT)
        self.cw_pin = DigitalInOut(cw_pin)
        self.cw_pin.direction = Direction.OUTPUT
        #self.ccw_pin = Pin(ccw_pin, Pin.OUT)
        self.ccw_pin = DigitalInOut(ccw_pin)
        self.ccw_pin.direction = Direction.OUTPUT

        #self.motor = PWM(Pin(self.pwm_pin), freq=1000, duty=0)
        self.motor =  pwmio.PWMOut(pwm_pin, frequency=1000, duty_cycle=0)
        #begin.freq(1000) # Set PWM frequency 1000Hz
        #begin.duty(0)

    def write(self, pwm_in, dir):
        if dir == 'cw':
            self.cw_pin.value = True # Turns on cw_pin
            self.ccw_pin.value = False # Some nodemcu's wires connected in other way around 
        elif dir == 'ccw':
            self.cw_pin.value = False 
            self.ccw_pin.value = True 
        self.motor.duty_cycle = pwm_in

if __name__ == '__main__':
    m1 = Fng(14, 0, 2)
    m2 = Fng(12, 13, 15)

    m1.write(0, 'cw')
    m2.write(0, 'cw')