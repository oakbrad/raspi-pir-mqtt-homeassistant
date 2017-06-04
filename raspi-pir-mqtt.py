import time
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt

#
# Connect to MQTT
# Read PIR sensor
# On motion: send 1
# Wait 4 seconds, turn off
#
# Run with forever

auth = {
  'username’:”MQTT_USER”,
  'password’:”MQTT_PASS”
}

from gpiozero import MotionSensor


pir = MotionSensor(4)

while True:
    if pir.motion_detected:
#        print('Motion On')
        publish.single(“CHANNEL/Motion/Switch",
          payload="1",
          hostname=“MQTT_HOST_IP”,
          client_id="pi",
          auth=auth,
          port=1883,
          protocol=mqtt.MQTTv311)
        time.sleep(4)
#        print('Motion Off')
        publish.single(“CHANNEL/Motion/Switch",
          payload="0",
          hostname=“MQTT_HOST_IP”,
          client_id="pi",
          auth=auth,
          port=1883,
          protocol=mqtt.MQTTv311)