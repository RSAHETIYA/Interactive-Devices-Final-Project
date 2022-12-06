import time, board, pwmio, adafruit_mpr121, busio

#code from below:
#https://www.youtube.com/watch?v=6kQyU-pu8HE&ab_channel=JohnGallaugher

#i2c = board.I2C()
i2c = busio.I2C(board.SCL, board.SDA)
touch_pad = adafruit_mpr121.MPR121(i2c)

tone = pwmio.PWMOut(board.D3, variable_frequency = True)
volume = 25
tone.duty_cycle = volume
notes = [262, 277, 294, 311, 330, 349, 370, 392, 410, 440, 466, 494]
tone_duration = 0.2
rest_duration = 0.01

def play_a_tone(freq):
    tone.duty_cycle = volume
    tone.frequency = freq

def play_a_rest(duration):
    tone.duty_cycle = 0
    time.sleep(duration)

while True:
    touched = False
    for i in range(12):
        if touch_pad[i].value:
            print("You touched pad #{}!".format(i))
            play_a_tone(notes[i])
            touched = True
    if touched == False:
        tone.duty_cycle = 0

