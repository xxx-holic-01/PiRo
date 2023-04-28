import time
import RPi.GPIO as GPIO
from board import SCL, SDA
import busio

# Import the PCA9685 module. Available in the bundle and here:
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

i2c = busio.I2C(SCL, SDA)

#PCA9685 class instance.
pca = PCA9685(i2c)

pca.frequency = 50

#servos
servo1 = servo.Servo(pca.channels[1])
servo2 = servo.Servo(pca.channels[2])
servo3 = servo.Servo(pca.channels[3])
servo4 = servo.Servo(pca.channels[4])
servo5 = servo.Servo(pca.channels[5])
servo6 = servo.Servo(pca.channels[6])
servo7 = servo.Servo(pca.channels[7])
servo8 = servo.Servo(pca.channels[8])
servo9 = servo.Servo(pca.channels[9])
servo10 = servo.Servo(pca.channels[10])
servo11 = servo.Servo(pca.channels[11])
servo12 = servo.Servo(pca.channels[12])

#distance
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 16
GPIO_ECHO = 20
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
# set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
# set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
# save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
# save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
# time difference between start and arrival
    TimeElapsed = StopTime - StartTime
# multiply with the sonic speed (34300 cm/s)
# and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
def initial():
    servo1.angle=30
    servo4.angle=30
    servo10.angle=30
    servo7.angle=30
    
    
    servo8.angle=90
    servo11.angle=90
    servo5.angle=90
    servo2.angle=90
    
    servo9.angle=130
    servo12.angle=45
    servo6.angle=45
    servo3.angle=130
    
def stand():
    
    servo1.angle=140
    servo4.angle=140
    servo10.angle=140
    servo7.angle=140
    
    
    servo8.angle=height
    servo11.angle=height
    servo5.angle=height
    servo2.angle=height
    
    servo9.angle=130
    servo12.angle=45
    servo6.angle=45
    servo3.angle=130
#movement    
def forward():
    stand()
    servo10.angle=150
    servo11.angle=120
    servo12.angle=0
    time.sleep(0.2)
    
    servo5.angle=120
    servo6.angle=90
    servo4.angle=150
    time.sleep(0.2)
    
    servo5.angle=height
    servo11.angle=height
    time.sleep(0.2)
    
    servo2.angle=120
    servo6.angle=45
    servo12.angle=45
    time.sleep(0.2)
    
    servo2.angle=height
    time.sleep(0.1)
    
    stand()
    
    time.sleep(0.2)    
    servo1.angle=150
    servo2.angle=120
    servo3.angle=175
    time.sleep(0.2)
    
    servo8.angle=120
    servo9.angle=90
    servo7.angle=150
    time.sleep(0.2)
    
    servo8.angle=height
    servo2.angle=height
    time.sleep(0.2)
    
    servo9.angle=130
    servo3.angle=130
    servo11.angle=120
    time.sleep(0.2)
    
    servo11.angle=height
    time.sleep(0.1)
    
    stand()
def left():
    servo10.angle=150
    servo11.angle=120
    servo12.angle=10
    time.sleep(0.2)
    servo11.angle=90
    servo8.angle=120
    servo9.angle=85
    servo7.angle=150
    time.sleep(0.2)
    servo8.angle=90
    time.sleep(0.2)
    servo4.angle=150
    servo5.angle=120
    servo6.angle=10
    time.sleep(0.2)
    servo5.angle=90
    time.sleep(0.5)
    servo1.angle=150
    servo2.angle=120
    servo3.angle=85
    time.sleep(0.2)
    servo2.angle=height 
    forward()
    

def main():
    
    global height
    height = 90
    time.sleep(2)
    stand()
    
    time.sleep(2)
    ch=input("Enter control(W,A,D,O for exit): ")
    while(ch!='o'):
        dist = distance()
        linit_distance = 15
        print ("Measured Distance = %.1f cm" % dist)
        if(ch == "w" and dist > linit_distance):
            print("moving forward")
            forward()
            time.sleep(0.2)
        if(ch == "a"and dist > linit_distance):
            print("moving left")
            left()
            time.sleep(1)
        if(ch == "d"and dist > linit_distance):
            print("moving right")
            
            time.sleep(1)
        if dist < 15:
            print("distance less than 15 and the distance is :",dist)
        ch=input("Enter control(W,A,D,O for exit): ")
        '''
    for i in range(5):
        time.sleep(1)
        forward()
        '''
        
if __name__ == '__main__':
    main()
 