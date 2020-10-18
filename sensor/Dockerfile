
FROM balenalib/raspberry-pi-python:3.7-stretch-run

RUN pip install --upgrade pip

WORKDIR /usr/src/app

RUN pip install flask

# "pip install Adafruit_DHT" doesn't work. The command returns the following error:
# Could not detect if running on the Raspberry Pi or Beaglebone Black.
# installing wheel for a specific arch(armv6l) works
RUN pip install https://www.piwheels.org/simple/adafruit-dht/Adafruit_DHT-1.4.0-cp37-cp37m-linux_armv6l.whl

COPY . ./

ENV UDEV=1

CMD [ "python","-u","app.py" ]