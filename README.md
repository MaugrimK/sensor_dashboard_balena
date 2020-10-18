# Raspberry Pi Zero Sensor Dashboard hosted on Balena.io
A dashboard to show temperature and humidity readings from Raspberry Pi Zero. 

Adapted from Balena Sense project https://github.com/balenalabs/balena-sense for
Raspberry Pi Zero and DHT22 sensor.

I recommend starting with this tutorial: https://www.balena.io/docs/learn/getting-started/raspberry-pi/python/

## Features
* Readings taken every 10 seconds
* Supports "test" mode to run without sensors. This is controlled by HAS_SENSORS env variable.
* Uses a deprecated Adafruit_DHT python library installed through wheel

## Hardware
* Raspberry Pi Zero Wireless WH (Pre-Soldered Header)
* DHT22 AM2302 Digital Temperature and Humidity Sensor Module. The sensor is 
connected to +5V, Ground and Pin 38 (GPIO20)

## Dashboard
<img src=images/dashboard.png width=700>

## Balena

### Build on Balena cloud
```
balena login
cd <project_folder>
balena push <app-name>
```

### Build locally
* This requires "local mode" to be enabled on the device in Balena Cloud
* ssh requires a "development" OS image
```
# build locally
balena push <device_ip> --nolive

# ssh to the local device
ssh root@<device_ip> -p 22222

# ssh to a service
balena ssh <device_IP> <service_name>

#check what containers are running
ssh root@<device_ip> -p 22222
balena-engine ps -a

# a container can be forced to stay live and not exit by adding this to Dockerfile
CMD tail -f /dev/null
```