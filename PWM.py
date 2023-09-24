import RPi.GPIO as GPIO
import time

# Define GPIO pins
TRIG_PIN = 17
ECHO_PIN = 18
BUZZER_PIN = 19  # GPIO pin for the buzzer

# Initialize GPIO settings
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# Function to calculate distance from the Ultrasonic Sensor
def get_distance():
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)
    
    pulse_start = time.time()
    pulse_end = time.time()
    
    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()
    
    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()
    
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # Speed of sound = 343 m/s (17150 cm/s) assume
    
    return round(distance, 2)

try:
    while True:
        distance = get_distance()
        print(f"Distance: {distance} cm")

        # Adjust the buzzer sound based on distance 
        if distance < 20:
            GPIO.output(BUZZER_PIN, GPIO.HIGH)
        else:
            GPIO.output(BUZZER_PIN, GPIO.LOW)

        time.sleep(0.1)

except KeyboardInterrupt:
    pass

GPIO.cleanup()