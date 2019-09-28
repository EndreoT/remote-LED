from RPi import GPIO
from time import sleep

class LedController:
    LED_PIN = 18

    def __init__(self):
        self.GPIO = GPIO
        self.GPIO.setwarnings(False)
        self.GPIO.setmode(self.GPIO.BCM)
        self.GPIO.setup(LedController.LED_PIN, self.GPIO.OUT)

    def on(self):
        self.GPIO.output(LedController.LED_PIN, True)
        
    
    def off(self):
        self.GPIO.output(LedController.LED_PIN, False)
    
    def onOff(self):
        self.on()
        sleep(2)
        self.off()


if __name__ == "__main__":
    ledController = LedController()
    ledController.onOff()
