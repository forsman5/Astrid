import RPi.GPIO as GPIO
from time import sleep

def turnMotor(sleepTime = 1):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)

    pwm = GPIO.PWM(12, 50)
    pwm.start(0)

    pwm.ChangeDutyCycle(5)
    sleep(sleepTime)
    pwm.ChangeDutyCycle(10)
    sleep(sleepTime)

    pwm.stop()
    GPIO.cleanup()
