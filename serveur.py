import paho.mqtt.client as mqtt
import json
import time

# Configuration MQTT
broker_address = "localhost"
broker_port = 1883
topic_vehicle_data = "vehicle/data"
topic_commands = "vehicle/commands"

server = mqtt.Client(protocol=mqtt.MQTTv311)

# Fonction appelée lors de la connexion au broker
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(topic_vehicle_data)  # Écouter les données des véhicules

# Fonction appelée à la réception d'un message
def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    print(f"Received data from vehicle {data['vehicle_id']}: {data}")

server.on_connect = on_connect
server.on_message = on_message

server.connect(broker_address, broker_port, 60)
server.loop_start()

try:
    while True:
        command = {"command": "slow_down", "reason": "heavy_rain"}  # Commande exemple
        server.publish(topic_commands, json.dumps(command))  # Publier la commande
        time.sleep(30)  # Intervalles entre les commandes
except KeyboardInterrupt:
    print("Server shutdown requested by user.")
    server.loop_stop()
    server.disconnect()
