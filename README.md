# Projet GY-521 avec Firebase

Ce projet utilise un capteur GY-521 (MPU6050) connecté à un Raspberry Pi pour lire des données d'accélération et les envoyer à une base de données Firebase en temps réel.

## Prérequis

- Raspberry Pi (avec Raspberry Pi OS installé)
- Capteur GY-521 (MPU6050)
- Accès à Internet pour le Raspberry Pi
- Compte Firebase avec un projet configuré

## Installation

### 1. Préparer le Raspberry Pi

1. **Mettre à jour le système et installer les dépendances nécessaires :**

    ```bash
    sudo apt update
    sudo apt upgrade
    sudo apt install python3-pip python3-smbus i2c-tools
    ```

2. **Installer les bibliothèques Python nécessaires :**

    ```bash
    pip3 install firebase-admin smbus2
    ```

3. **Activer l'interface I2C :**

    Exécute `raspi-config`, va dans **Interface Options** et active **I2C**.

    ```bash
    sudo raspi-config
    ```

### 2. Préparer le Projet Firebase

1. **Créer un projet Firebase :**

   - Accède à [Firebase Console](https://console.firebase.google.com/).
   - Crée un nouveau projet ou sélectionne un projet existant.
   - Dans la section **Paramètres du projet**, télécharge le fichier de clé privée JSON pour le SDK Admin.

2. **Téléverser le fichier JSON sur le Raspberry Pi :**

   Copie le fichier JSON que tu as téléchargé dans le répertoire `/home/pi/` de ton Raspberry Pi. Renomme le fichier si nécessaire pour qu'il corresponde au nom attendu dans le script.

### 3. Configuration du Script Python

1. **Télécharger ou cloner le script Python :**

   Clone le dépôt Git ou télécharge le script Python sur le Raspberry Pi.

   ```bash
   git clone https://github.com/<TON_NOM_D_UTILISATEUR>/<TON_DEPOT>.git
