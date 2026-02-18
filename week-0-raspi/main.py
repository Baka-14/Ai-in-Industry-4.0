import RPi.GPIO as GPIO
import time
import pyrebase

# Firebase configuration the json values will change with respect to where the database is made
config = {
    'apiKey': "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    'authDomain': "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    'projectId': "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    'storageBucket': "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    'messagingSenderId': "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    'appId': "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    'databaseURL':'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'measurementId': "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}
  
firebase = pyrebase.initialize_app(config)
db = firebase.database()

# Ultrasonic sensor setup
TRIG_PIN = 18  # GPIO pin for trigger
ECHO_PIN = 24  # GPIO pin for echo

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG_PIN, GPIO.OUT)
    GPIO.setup(ECHO_PIN, GPIO.IN)

def get_distance():
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)

    start_time = time.time()
    stop_time = time.time()

    while GPIO.input(ECHO_PIN) == 0:
        start_time = time.time()

    while GPIO.input(ECHO_PIN) == 1:
        stop_time = time.time()

    elapsed_time = stop_time - start_time
    distance = (elapsed_time * 34300) / 2  # Speed of sound is 343 m/s
    return distance

if __name__ == "__main__":
    try:
        setup()
        while True:
            distance = get_distance()
            print(f"Distance: {distance} cm")
            
            # Create a data object with distance and a timestamp
            data = {
                "distance": distance,
                "timestamp": int(time.time())
            }

            # Push the data object to Firebase
            db.child("Status").push(data)

            time.sleep(1)  # Wait for 1 second before the next reading

    except KeyboardInterrupt:
        GPIO.cleanup()