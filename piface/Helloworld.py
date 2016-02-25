import pifacecad as p
import sys
import time
import subprocess

GET_IP_CMD = "hostname --all-ip-addresses"

cad = p.PiFaceCAD()
cad.lcd.backlight_on()
cad.lcd.write("My IP is \n")

def run_cmd(cmd):
   return subprocess.check_output(cmd, shell=True).decode('utf-8')
def get_my_ip():
   return run_cmd(GET_IP_CMD)[:-1]

cad.lcd.blink_off()
cad.lcd.cursor_off()
time.sleep(5)
cad.lcd.write(get_my_ip())
'''
time.sleep(6)
cad.lcd.clear()
cad.lcd.blink_off()
cad.lcd.cursor_off()
cad.lcd.backlight_off()
'''
while 1 :
    if cad.switches[0].value:
        cad.lcd.backlight_off()

    if cad.switches[1].value:
        cad.lcd.backlight_on()

    if cad.switches[3].value:
        cad.lcd.clear()
        cad.lcd.backlight_on()
        cad.lcd.write("My IP is \n")
        cad.lcd.write(get_my_ip())

    if cad.switches[2].value:
        cad.lcd.clear()
        cad.lcd.backlight_off()
        cad.lcd.cursor_off()
        cad.lcd.blink_off()

    if cad.switches[4].value:
        cad.lcd.clear()
        cad.lcd.write("PiFace OFF")
        time.sleep(2)
        cad.lcd.clear()
        cad.lcd.backlight_off()
        cad.lcd.cursor_off()
        cad.lcd.blink_off()
        break
