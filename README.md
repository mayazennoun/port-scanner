# Python Multi-Threaded Port Scanner 

Un scanner de ports TCP rapide et léger écrit en Python, utilisant le multi-threading pour scanner des plages de ports en quelques secondes.

## 📌 Description

Ce script permet de vérifier quels ports TCP sont ouverts sur une adresse IP cible (hôte local ou distant). Il utilise la bibliothèque `concurrent.futures` pour gérer un pool de threads, ce qui permet de tester plusieurs ports simultanément plutôt que d'attendre la réponse de chaque port l'un après l'autre.

## ✨ Fonctionnalités

* **Vitesse :** Utilisation de `ThreadPoolExecutor` pour un scan ultra-rapide.
* **Sécurité :** Utilisation de verrous (`threading.Lock`) pour éviter l'entrelacement des messages dans la console.
* **Facilité d'utilisation :** Demande simplement l'IP cible à l'exécution.
* **Gestion des erreurs :** Gère les interruptions clavier (Ctrl+C) et les erreurs de résolution de nom d'hôte.

## 🛠️ Installation

1.  Assurez-vous d'avoir **Python 3.6+** installé sur votre système.
2.  Clonez ce dépôt ou copiez le fichier `.py`.
3.  Aucune bibliothèque externe n'est requise (utilise uniquement la bibliothèque standard).

## 🚀 Utilisation

Lancez le script depuis votre terminal :

```bash
python port_scanner.py