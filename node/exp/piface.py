import pifacecad as p
import time
import subprocess

cad = p.PiFaceCAD()
p=subprocess.Popen([ "node", "server.js"])
while(True):
    f = open("text1.txt",'r')
    line = f.readline()
    
    time.sleep(1)
    cad.lcd.clear()
    cad.lcd.backlight_on()
    cad.lcd.write(line)
    cad.lcd.cursor_off()
    cad.lcd.blink_off()

    if (cad.switches[4].value==1):
        cad.lcd.clear()
        cad.lcd.write("OFF")
        time.sleep(2)
        cad.lcd.clear()
        cad.lcd.backlight_off()
        cad.lcd.cursor_off()
        cad.lcd.blink_off()
        p.kill()
        break
