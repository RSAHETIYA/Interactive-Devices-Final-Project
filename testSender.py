import time
import board
import busio

i2c = busio.I2C(board.SCL, board.SDA)

#mpr121 = adafruit_mpr121.MPR121(i2c)

print(i2c.scan())