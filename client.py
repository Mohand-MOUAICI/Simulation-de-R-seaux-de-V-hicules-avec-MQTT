import paho.mqtt.client as mqtt
import json
import time

# Configuration MQTT
broker_address = "localhost"  # Adresse du broker MQTT
broker_port = 1883            # Port utilisé par le broker MQTT
topic_request = "vehicle/requests"  # Topic pour écouter les requêtes
topic_response = "vehicle/responses"  # Topic pour publier les réponses

# Données initiales du véhicule
vehicle_data = {"id": "105", "vtype": 1, "x": 20, "y": 30, "dir": 1, "speed": 5}

# Initialisation du client MQTT
client = mqtt.Client(protocol=mqtt.MQTTv311)

# Fonction appelée lors de la connexion au broker
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(topic_request)  # S'abonner au topic de requêtes

# Fonction appelée à la réception d'un message
def on_message(client, userdata, msg):
    print(f"Received message on topic {msg.topic}: {msg.payload.decode()}")
    if msg.topic == topic_request:
        request = json.loads(msg.payload.decode())
        if request["vehicle_id"] == vehicle_data["id"]:
            # Créer une réponse avec la position et l'heure actuelle
            response = {
                "vehicle_id": vehicle_data["id"],
                "position": {"x": vehicle_data["x"], "y": vehicle_data["y"]},
                "timestamp": time.time()
            }
            client.publish(topic_response, json.dumps(response))  # Publier la réponse

client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, broker_port, 60)
client.loop_start()

try:
    while True:
        vehicle_data['x'] += 1  # Déplacement en X
        vehicle_data['y'] += 1  # Déplacement en Y
        print(f"Vehicle at (x: {vehicle_data['x']}, y: {vehicle_data['y']})")
        time.sleep(1)
except KeyboardInterrupt:
    print("Vehicle simulation terminated by user.")
    client.loop_stop()
    client.disconnect()
