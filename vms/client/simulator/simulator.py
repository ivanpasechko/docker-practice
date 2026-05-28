import time
import json
import random
import paho.mqtt.client as mqtt

MQTT_BROKER = "192.168.56.102"
MQTT_PORT = 1883
MQTT_TOPIC = "sensors/temperature/value"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Успешно подключились к MQTT-брокеру!")
    else:
        print(f"Ошибка подключения, код: {rc}")

client = mqtt.Client()
client.on_connect = on_connect

print(f"Подключение к брокеру {MQTT_BROKER}...")
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_start()

while True:
    metrics = [
        {"name": "temp_housing", "value": round(random.uniform(55.0, 72.0), 2)},
        {"name": "temp_environment", "value": round(random.uniform(19.0, 24.5), 2)},
        {"name": "hydraulic_pressure", "value": round(random.uniform(4.2, 5.8), 2)},
        {"name": "motor_current", "value": round(random.uniform(115.0, 148.0), 2)},
        {"name": "vibration_level", "value": round(random.uniform(1.8, 3.5), 2)}
    ]
    
    for metric in metrics:
        payload = json.dumps(metric)
        client.publish(MQTT_TOPIC, payload)
        print(f"Отправлено: {payload}")
        
    time.sleep(5)
