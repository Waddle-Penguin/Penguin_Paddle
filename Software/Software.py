#Imports
from machine import Pin, ADC, PWM, TouchPad
from time import sleep, ticks_ms, ticks_diff

#Defining Pins
dit = TouchPad(Pin(7))
dah = TouchPad(Pin(8))
On_Off = Pin(3, Pin.IN, Pin.PULL_UP)
Stereo_USB = Pin(4, Pin.IN, Pin.Pull_UP)
AudioJack = Pin(2 ,Pin.OUT)

#Poteniometers are weird. And buzzers.
p_wpm = ADC(Pin(5))     
p_wpm.atten(ADC.ATTN_11DB)

volume = ADC(Pin(6))  
volume.atten(ADC.ATTN_11DB)

buzzer = PWM(Pin(1))
buzzer.freq(4000)  #should be like, the sound it makes

#Touch Stuff I dunno what to call it
dit_baseline = dit.read()
dah_baseline = dah.read()

dit_threshold = dit_baseline - 100
dah_threshold = dah_baseline - 100

#Buzzer go brrrrrr
def transmit_jack(duration):
    if On_Off.value() == 0:
        volume_raw = volume.read()
        duty = int(volume_raw / 4095 * 512)
        buzzer.duty(duty)
    else:
        buzzer.duty(0)

    AudioJack.value(1)
    sleep(duration)
    buzzer.duty(0)
    AudioJack.value(0)
    while dit.read() < dit_threshold:
        sleep(0.01)
    while dah.read() < dah_threshold:
        sleep(0.01)

#USB tansmission mode will go here eventually

#Main loop that does stuff
while True:
    timeout = ticks_ms() + 2000  # 2-second timeout
    while dit.read() < dit_threshold and ticks_ms() < timeout:
        sleep(0.01)

    wpm_raw = p_wpm.read()
    wpm = max(5, int(wpm_raw / 4095 * 30)) #this should make wpm actually work

    #How long stuff takes, will probably need to be tuned
    dit_time = 1 / wpm
    dah_time = 3 / wpm

    #Dits & Dahs
    if dit.read() < dit_threshold:
        timeout = ticks_ms() + 2000  # 2-second timeout
        while dit.read() < dit_threshold and ticks_diff(timeout, ticks_ms()) > 0:
            sleep(0.01)

        print(f"dit at {wpm} wpm") #for initial setup
        if Stereo_USB.value(): #Audio mode
            transmit_jack(dit_time)
        else:
            #keyboard support
            print("dit input error")
        sleep(0.01)

    if dah.read() < dah_threshold:
        timeout = ticks_ms() + 2000  # Repeat for dah 
        while dah.read() < dah_threshold and ticks_diff(timeout, ticks_ms()) > 0:
            sleep(0.01)

        print(f"dah at {wpm} wpm") #for initial setup
        if Stereo_USB.value(): #Audio mode
            transmit_jack(dah_time)
        else:
            #keyboard support
            print("dah input error")
        sleep(0.01)