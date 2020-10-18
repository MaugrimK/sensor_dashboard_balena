import json
import random
import os

from temperature_sensor import TempSensor

from flask import Flask

app = Flask(__name__)


@app.route('/get_value')
def get_value():
    humidity, temperature = app.temp_sensor.get_measurement_from_sensor()
    tags = {
        'temp_value': temperature,
        'humidity_value': humidity
        }
    return tags


def main():
    if os.environ['HAS_SENSORS'] == 'TRUE':
        fake_measurements = False
    elif os.environ['HAS_SENSORS'] == 'FALSE':
        fake_measurements = True

    app.temp_sensor = TempSensor(20, fake_measurements)
    app.run(host='0.0.0.0', port=80)


if __name__ == "__main__":
    main()