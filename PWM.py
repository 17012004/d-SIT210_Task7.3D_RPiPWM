import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

TRIG_PIN = 21
ECHO_PIN = 20
LED_PIN = 4

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_PIN, GPIO.OUT)
led_pwm = GPIO.PWM(LED_PIN, 100)
led_pwm.start(0)

brightness_levels = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]

while True:
    # Configure the trigger and echo pins
    GPIO.setup(TRIG_PIN, GPIO.OUT)
    GPIO.setup(ECHO_PIN, GPIO.IN)

    GPIO.output(TRIG_PIN, False)
    time.sleep(0.2)
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)

    while GPIO.input(ECHO_PIN) == 0:
        pulse_start_time = time.time()
    while GPIO.input(ECHO_PIN) == 1:
        pulse_end_time = time.time()

    pulse_duration = pulse_end_time - pulse_start_time

    distance = pulse_duration * 17150
    distance = 2 * round(distance / 2)

    print("Distance:", distance, "cm")

    if distance >= 0 and distance <= 20:
        index = int((distance - 2) / 2)
        led_pwm.ChangeDutyCycle(brightness_levels[index])
    else:
        led_pwm.ChangeDutyCycle(0)

    time.sleep(1)
