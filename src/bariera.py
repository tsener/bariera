import RPi.GPIO as GPIO
import time
from bottle import route, run, template

##
# Simple script to manipulate a barrier remote, attached to a RasPI via GPIO
##

@route('/raise_gate', method='POST')
def click_outer_gate():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(24, GPIO.OUT)
    GPIO.output(24, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(24, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(24, GPIO.LOW)
    GPIO.cleanup()
    return 'ack'

run(host='localhost', port=5151)
