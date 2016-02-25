import subprocess
import sys
import os
import pifacecad as p

cad = p.PiFaceCAD()
cad.lcd.backlight_on()
cad.lcd.write("Select Music")
music=["01.mp3", "02.mp3", "07.mp3"]
while(1):
    if cad.switches[0].value:
        cad.lcd.clear()
        cad.lcd.write("Holy Wars...The Punishment Due")
        a = 0
    if cad.switches[1].value:
        cad.lcd.clear()
        cad.lcd.write("Hangar 18")
        a = 1
    if cad.switches[2].value:
        cad.lcd.clear()
        cad.lcd.write("Tornado of Souls")
        a = 2
    if cad.switches[4].value:
        cad.lcd.clear()
        cad.lcd.write("START")
        os.system("omxplayer -o local /home/pi/Music/"+music[a])
