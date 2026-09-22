from signal import pause
from gpiozero import LED, Button, PWMLED
import time, sched
import board
from adafruit_ltr329_ltr303 import LTR303
import serial
from time import gmtime, strftime

#setup UART


ser = serial.Serial(
        port='/dev/ttyS0',
        baudrate = 115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=0.1
)


#setup interrupt
#BUTTON_PIN = 16
TOGGLE_VALUE = 0
#button = Button(BUTTON_PIN,pull_up = False,bounce_time = 0.5)
#LED_PIN = 14
#led1 = LED(LED_PIN) 

#setup PWM
SIGNAL = PWMLED(pin=18,initial_value=0,frequency = 100)
power =0
#setup LUX-sensor
i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller

time.sleep(0.1)  # sensor takes 100ms to 'boot' on power up
ltr303 = LTR303(i2c)


#Reglering
börvärde_LUX = 300
ärvärde_LUX = ltr303.visible_plus_ir_light
time.sleep(0.5)  # sleep for half a second
PWM_dutycycle = 0.25 # 25%
LAMP_STATE = True

def PWM(procent):
    global PWM_dutycycle
    PWM_dutycycle = PWM_dutycycle + procent
    if(PWM_dutycycle >= 1):
        PWM_dutycycle = 1
    if(PWM_dutycycle <= 0):
        PWM_dutycycle = 0
    if(PWM_dutycycle <= 1 and PWM_dutycycle >= 0):
        SIGNAL.value = PWM_dutycycle
    else:
        print("PWM_dutycycle > 1", PWM_dutycycle)
    print("PWM_dutycycle =",PWM_dutycycle)
    time.sleep(0.1)
    return
    
# def indoor_LUX():
#     global ltr303
#     print("Visible + IR:", ltr303.visible_plus_ir_light)
#     print("Infrared    :", ltr303.ir_light)
#     print()
#     time.sleep(0.5)  # sleep for half a second
#     return

def reglering():
    global PWM_dutycycle
    global LAMP_STATE
    ärvärde_LUX = ltr303.visible_plus_ir_light
    print("current_LUX",ärvärde_LUX)
    if((ärvärde_LUX < börvärde_LUX-7 or ärvärde_LUX > börvärde_LUX+7) and LAMP_STATE and PWM_dutycycle <= 1 and PWM_dutycycle >= 0 ):
        ärvärde_LUX = ltr303.visible_plus_ir_light # mät är-värdet
        print("current_LUX",ärvärde_LUX)
        if(ärvärde_LUX < börvärde_LUX):            # kolla om är-värdet är mindre än bör-värdet
            if(ärvärde_LUX < börvärde_LUX-20):     # kolla om är-värdet är mycket mindre än börvärdet
                PWM(0.05)
            elif(ärvärde_LUX < börvärde_LUX):     # kolla om är-värdet är LITE mindre än börvärdet
               PWM(0.01)
            
        elif(ärvärde_LUX > börvärde_LUX):           # kolla om är-värdet är större än börvärdet
            if(ärvärde_LUX > börvärde_LUX+20):     # kolla om är-värdet är mycket större än börvärdet
                PWM(-0.05)
            elif(ärvärde_LUX > börvärde_LUX):     # kolla om är-värdet är LITE större än börvärdet                
                PWM(-0.01)

    
            
            


def led_toggle():
    global TOGGLE_VALUE
    global LAMP_STATE
    

    
    if LAMP_STATE == True:
        #led1.off()
        SIGNAL.value = 0
        LAMP_STATE = False
        print("LED OFF")
        TOGGLE_VALUE = 1
    elif LAMP_STATE == False:
        #led1.on()
        LAMP_STATE = True
        print("LED ON")
        TOGGLE_VALUE = 0
    return

def LogLUX():
    time = strftime("%H:%M:%S", gmtime())
    print("Log time: ",time)
    inomhus_lux = ltr303.visible_plus_ir_light
    utomhus_lux = 0
    
    with open("LUX.txt", "r") as f:
        utomhus_lux = f.readline()
        print("utomhus_lux: ",utomhus_lux)
    with open("datalog.txt", "a") as f:
            f.write(time+", Inomhus LUX: "+str(inomhus_lux)+", Utomhus LUX: "+ str(utomhus_lux)+"\n")

def set_bor_varde():
    global börvärde_LUX
    utomhus_lux = 0
    with open("LUX.txt", "r") as f:
        utomhus_lux = f.readline()
    print("utomhus_lux",utomhus_lux)        
    if(float(utomhus_lux) >150):
        börvärde_LUX = 0.75*float(utomhus_lux) 
    elif(float(utomhus_lux) <= 150):
        börvärde_LUX = 0.35*float(utomhus_lux)


def main():
    #global LAMP_STATE
    #global börvärde_LUX
   
    
    while(1):
        set_bor_varde()
        x=ser.readline()
        print("börvärde_LUX: ",börvärde_LUX)
        print(x)
        if("LOG" in str(x)):
            LogLUX()
            print("log")
        with open("AppCommands.txt", "r") as f:
            line = f.readlines()
            line[0] = line[0].strip("\n")
            print(line)
            if line[0] == "app-off":
                reglering()
                x=ser.readline()
                print(x)
                if("ON" in str(x)):
                    print("ON in x")
                    led_toggle()
                elif("OFF" in str(x)):
                    print("OFF in x")
                    led_toggle()
                elif("LOG" in str(x)):
                    LogLUX()
                    print("LOG in x")
            elif( line[0] == "app-on"and len(line)==2):
                #line = f.readline()
                print(line[0])
                if line[1] == "on":
                    
                    #LAMP_STATE = True
                    SIGNAL.value = 1
                    #reglering()
                elif line[1] == "off":
                    #LAMP_STATE = False
                    SIGNAL.value = 0
                elif (float(line[1]) >= 0 or float(line[1]) <= 100):
                    dutyCycle = float(line[1])*0.01
                    print("dutyCycle =", dutyCycle)
                    SIGNAL.value = dutyCycle
                    print("LUX:", ltr303.visible_plus_ir_light)
                    time.sleep(0.1)
                  
                    
                
        

        
    #indoor_LUX()
    

 
    
    
main()