import RPi.GPIO as GPIO
import time

#MODE_SET
GPIO.setmode(GPIO.BOARD)
#CHANNEL_SET
chan_list = [40,38,36,37]
GPIO.setup(chan_list, GPIO.OUT)

#RED
GPIO.output(40,GPIO.HIGH)
time.sleep(2)
GPIO.output(40,GPIO.LOW)
#GREEN
GPIO.output(38,GPIO.HIGH)
time.sleep(2)
GPIO.output(38,GPIO.LOW)
#BLUE
GPIO.output(36,GPIO.HIGH)
time.sleep(2)
GPIO.output(36,GPIO.LOW)
#YELLOW
GPIO.output(37,GPIO.HIGH)
time.sleep(2)
GPIO.output(37,GPIO.LOW)

#CLEANUP
GPIO.cleanup()
