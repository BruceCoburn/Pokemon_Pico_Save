import machine
import utime

g_ON = 1
g_OFF = 0

button_pin = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

led_bit7 = machine.Pin(6, machine.Pin.OUT)
led_bit6 = machine.Pin(7, machine.Pin.OUT)
led_bit5 = machine.Pin(8, machine.Pin.OUT)
led_bit4 = machine.Pin(9, machine.Pin.OUT)
led_bit3 = machine.Pin(10, machine.Pin.OUT)
led_bit2 = machine.Pin(11, machine.Pin.OUT)
led_bit1 = machine.Pin(12, machine.Pin.OUT)
led_bit0 = machine.Pin(13, machine.Pin.OUT)

led_onboard = machine.Pin(25, machine.Pin.OUT)

while True:
    
    if button_pin.value():

        led_bit7.toggle()
        led_bit6.value(g_OFF)
        led_bit5.value(g_ON)
        led_bit4.value(g_OFF)
        led_bit3.value(g_ON)
        led_bit2.value(g_OFF)
        led_bit1.value(g_ON)
        led_bit0.value(g_OFF)
        
        led_onboard.value(g_ON)
        
        utime.sleep(0.5)
        
        led_bit7.value(g_OFF)
        led_bit6.value(g_ON)
        led_bit5.value(g_OFF)
        led_bit4.value(g_ON)
        led_bit3.value(g_OFF)
        led_bit2.value(g_ON)
        led_bit1.value(g_OFF)
        led_bit0.value(g_ON)

        
        led_onboard.value(g_OFF)
        
        utime.sleep(0.5)
