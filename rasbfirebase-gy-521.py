import smbus2
import time
import firebase_admin
from firebase_admin import credentials, db

# Adresse I2C du GY-521
DEVICE_ADDRESS = 0x68

# Registres du MPU6050
POWER_MGMT_1 = 0x6B
ACCEL_XOUT_H = 0x3B

# Initialisation du bus I2C
bus = smbus2.SMBus(1)

def read_byte(reg):
    return bus.read_byte_data(DEVICE_ADDRESS, reg)

def read_word(reg):
    high = bus.read_byte_data(DEVICE_ADDRESS, reg)
    low = bus.read_byte_data(DEVICE_ADDRESS, reg + 1)
    value = (high << 8) + low
    return value

def read_word_2c(reg):
    value = read_word(reg)
    if value >= 0x8000:
        return -((65535 - value) + 1)
    else:
        return value

# Initialisation du capteur
bus.write_byte_data(DEVICE_ADDRESS, POWER_MGMT_1, 0)

# Configuration Firebase
cred = credentials.Certificate('/home/pi/firebase-adminsdk.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://benrover-8ebf6-default-rtdb.firebaseio.com'
})
ref = db.reference('/gy521_data')

def get_acceleration():
    x = read_word_2c(ACCEL_XOUT_H)
    y = read_word_2c(ACCEL_XOUT_H + 2)
    z = read_word_2c(ACCEL_XOUT_H + 4)
    return x, y, z

while True:
    x, y, z = get_acceleration()
    data = {
        'x': x,
        'y': y,
        'z': z,
        'timestamp': time.time()
    }
    ref.push(data)
    print(f"Data sent: {data}")
    time.sleep(1)
