import musicalbeeps
import time
import board
import busio

import adafruit_mpr121
import socket

i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)

player = musicalbeeps.Player(volume = 1,
                            mute_output = False)

state = 0

UDP_IP = "10.56.133.113"
UDP_PORT = 5005
MESSAGE = b"Hello, World!"

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)



sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

while True:
    MESSAGE = b""
    for i in range(12):
        if mpr121[i].value:
            if (i == 0):
                MESSAGE = b"0"
                player.play_note("C", 0.1)
            elif (i == 1):
                MESSAGE = b"1"
                player.play_note("Db", 0.1)
            elif (i == 2):
                MESSAGE = b"2"
                player.play_note("D", 0.1) 
            elif (i == 3):
                MESSAGE = b"3"
                player.play_note("Eb", 0.1) 
            elif (i == 4):
                MESSAGE = b"4"
                player.play_note("E", 0.1) 
            elif (i == 5):
                MESSAGE = b"5"
                player.play_note("F", 0.1) 
            elif (i == 6):
                MESSAGE = b"6"
                player.play_note("Gb", 0.1) 
            elif (i == 7):
                MESSAGE = b"7"
                player.play_note("G", 0.1) 
            elif (i == 8):
                MESSAGE = b"8"
                player.play_note("Ab", 0.1) 
            elif (i == 9):
                MESSAGE = b"9"
                player.play_note("A", 0.1) 
            elif (i == 10):
                MESSAGE = b"10"
                player.play_note("Bb", 0.1) 
            elif (i == 11):
                MESSAGE = b"11"
                player.play_note("B", 0.1) 
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    time.sleep(.1)