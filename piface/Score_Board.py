import pifacecad as p

cad = p.PiFaceCAD()
cad.lcd.backlight_on()
A_sum, B_sum, a , b = 0, 0, 0, 0
while 1:
    cad.lcd.write(" A team Score:"+str(A_sum)+"\n")
    cad.lcd.write(" B team Score:"+str(B_sum))
    cad.lcd.blink_off()
    cad.lcd.cursor_off()

    if cad.switches[0].value:
        a = 1
        cad.lcd.clear()
    A_sum += a
    a=0

    if cad.switches[1].value:
        b=1
        cad.lcd.clear()
    B_sum += b
    b=0

    if cad.switches[2].value:
        A_sum, B_sum = 0, 0
        cad.lcd.clear()

    if A_sum >= 100 or A_sum >= 100:
        A_sum, B_sum = 0, 0

    if cad.switches[4].value:
        cad.lcd.clear()
        cad.lcd.blink_off()
        cad.lcd.cursor_off()
        cad.lcd.backlight_off()
        break
    
    cad.lcd.write(" A team Score:"+str(A_sum)+"\n")
    cad.lcd.write(" B team Score:"+str(B_sum))
    cad.lcd.blink_off()
    cad.lcd.cursor_off()
