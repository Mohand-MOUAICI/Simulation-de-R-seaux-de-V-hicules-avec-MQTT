
# Simulation de Réseaux de Véhicules avec MQTT

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![MQTT Protocol](https://img.shields.io/badge/protocol-MQTT-green.svg)

Ce projet démontre la simulation de réseaux de véhicules qui se déplacent dans un environnement urbain et communiquent via MQTT, utilisant un broker MQTT pour coordonner la communication entre les véhicules simulés et un serveur central, ainsi qu'un upper-tester pour valider le fonctionnement des boîtiers de communication.

## Prérequis

Avant de démarrer, assurez-vous que vous avez installé :

- **Python 3.8+** : Téléchargeable depuis [python.org](https://www.python.org/downloads/)
- **Mosquitto** (ou tout autre broker MQTT) : Instructions d'installation disponibles sur [mosquitto.org](https://mosquitto.org/download/)
- **paho-mqtt** : Une bibliothèque Python pour MQTT

```bash
pip install paho-mqtt
```

## Installation

1. **Broker MQTT (Mosquitto)**
   - Sous Windows, téléchargez et installez depuis [mosquitto.org](https://mosquitto.org/download/).
   - Sous Linux, utilisez `sudo apt-get install mosquitto`.

2. **Clonez le dépôt**
   ```bash
   git clone [https://yourrepository.git](https://github.com/Mohand-MOUAICI/Simulation-de-R-seaux-de-V-hicules-avec-MQTT.git)
   cd project-folder
   ```

## Structure du Projet

- `client.py` - Simule un véhicule se déplaçant et communiquant ses données.
- `server.py` - Agit comme un serveur central pour recevoir et gérer les données des véhicules.
- `upper_tester.py` - Envoie des requêtes et reçoit des réponses des véhicules.

## Exécution

Ouvrez trois terminaux et exécutez chaque composant dans un terminal séparé :

### Serveur Central
```bash
python server.py
```

### Véhicule
```bash
python client.py
```

### Upper-Tester
```bash
python upper_tester.py
```

## Utilisation

Après le démarrage des scripts, le système simule les mouvements des véhicules et les interactions de messages. Le serveur central collecte et gère les données, et l'upper-tester vérifie la communication.

## Contribution

Les contributions sont toujours les bienvenues! Pour contribuer :

1. Fork le projet
2. Créez votre branche de fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Commit vos modifications (`git commit -m 'Add some AmazingFeature'`)
4. Push à la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## Licence

Distribué sous la licence MIT. Voir `LICENSE` pour plus d'informations.
