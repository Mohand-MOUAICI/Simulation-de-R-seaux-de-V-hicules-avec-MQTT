import paho.mqtt.client as mqtt
import json
import time

# Configuration MQTT
broker_address = "localhost"
broker_port = 1883
topic_request = "vehicle/requests"
topic_response = "vehicle/responses"

upper_tester = mqtt.Client(protocol=mqtt.MQTTv311)

# Fonction appelée lors de la connexion au broker
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(topic_response)  # S'abonner au topic de réponses

# Fonction appelée à la réception d'un message
def on_message(client, userdata, msg):
    print(f"Received message on topic {msg.topic}: {msg.payload.decode()}")

upper_tester.on_connect = on_connect
upper_tester.on_message = on_message

upper_tester.connect(broker_address, broker_port, 60)
upper_tester.loop_start()

try:
    while True:
        request = {"request": "get_status", "vehicle_id": "105"}
        upper_tester.publish(topic_request, json.dumps(request))  # Envoyer la requête
        time.sleep(5)  # Intervalles entre les requêtes
except KeyboardInterrupt:
    print("Test terminated by user.")
    upper_tester.disconnect()
