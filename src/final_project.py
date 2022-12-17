import musicalbeeps
import time
import board
import busio

import adafruit_mpr121
import socket

import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
import uuid
import signal


#GPIO mappings
#5 = 7
#6 = 6
#13 = 5
#19 = 4
#16 = 3
#20 = 2
#21 = 1


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)


i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)

player = musicalbeeps.Player(volume = 1,
                            mute_output = False)

# MQTT topic
topic = 'IDD/learning_pianos/data'

# On connect callback
def on_connect(client, userdata, flags, rc):
    client.subscribe(topic)

# On message callback
def on_message(cleint, userdata, msg):
    if msg.topic == topic:
        message = msg.payload.decode('UTF-8')
        # Condition to not check messages sent by self
        if (message.split(":")[0] != "1"):
            in_key_pressed = message.split(":")[1]
            if (in_key_pressed == "11"):
                GPIO.output(19,GPIO.HIGH)
            elif (in_key_pressed == "10"):
                GPIO.output([13,19],GPIO.HIGH)
            elif (in_key_pressed == "9"):
                GPIO.output(13,GPIO.HIGH)
            elif (in_key_pressed == "8"):
                GPIO.output([5,13],GPIO.HIGH)
            elif (in_key_pressed == "7"):
                GPIO.output(5,GPIO.HIGH)
            elif (in_key_pressed == "6"):
                GPIO.output([5,6],GPIO.HIGH)
            elif (in_key_pressed == "5"):
                GPIO.output(6,GPIO.HIGH)
            elif (in_key_pressed == "4"):
                GPIO.output(21,GPIO.HIGH)
            elif (in_key_pressed == "3"):
                GPIO.output([20,21],GPIO.HIGH)
            elif (in_key_pressed == "2"):
                GPIO.output(20,GPIO.HIGH)
            elif (in_key_pressed == "1"):
                GPIO.output([16,20],GPIO.HIGH)
            elif (in_key_pressed == "0"):
                GPIO.output(16,GPIO.HIGH)

# MQTT Set Up
client = mqtt.Client(str(uuid.uuid1()))
client.tls_set()
client.username_pw_set('idd', 'device@theFarm')
client.on_connect = on_connect
client.on_message = on_message

client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

client.loop_start()

def handler(signum, frame):
    client.loop_stop()
    exit (0)

signal.signal(signal.SIGINT, handler)


while True:

    GPIO.output(5,GPIO.LOW)
    GPIO.output(6,GPIO.LOW)
    GPIO.output(13,GPIO.LOW)
    GPIO.output(19,GPIO.LOW)
    GPIO.output(16,GPIO.LOW)
    GPIO.output(20,GPIO.LOW)
    GPIO.output(21,GPIO.LOW)
    MESSAGE = ""

    # Message to Note and LED condition block
    for i in range(12):
        if mpr121[i].value:
            if (i == 0):
                MESSAGE = "0"
                player.play_note("C", 0.1)
            elif (i == 1):
                MESSAGE = "1"
                player.play_note("Db", 0.1)
            elif (i == 2):
                MESSAGE = "2"
                player.play_note("D", 0.1) 
            elif (i == 3):
                MESSAGE = "3"
                player.play_note("Eb", 0.1) 
            elif (i == 4):
                MESSAGE = "4"
                player.play_note("E", 0.1) 
            elif (i == 5):
                MESSAGE = "5"
                player.play_note("F", 0.1) 
            elif (i == 6):
                MESSAGE = "6"
                player.play_note("Gb", 0.1) 
            elif (i == 7):
                MESSAGE = "7"
                player.play_note("G", 0.1) 
            elif (i == 8):
                MESSAGE = "8"
                player.play_note("Ab", 0.1) 
            elif (i == 9):
                MESSAGE = "9"
                player.play_note("A", 0.1) 
            elif (i == 10):
                MESSAGE = "10"
                player.play_note("Bb", 0.1) 
            elif (i == 11):
                MESSAGE = "11"
                player.play_note("B", 0.1) 

    client.publish(topic, "1:" + MESSAGE)
    time.sleep(.1)


