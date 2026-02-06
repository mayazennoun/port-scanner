# Quick Nmap Port Scanner

Un script Python simple permettant d’effectuer un scan rapide de ports sur une adresse IP cible à l’aide de Nmap.
Il analyse les ports les plus courants et affiche les services détectés ainsi que leurs versions.

## Fonctionnalités

* Scan des ports TCP de 1 à 1024

* Détection de l’état des ports


* Identification des services et des versions

* Scan rapide avec Nmap

* Affichage clair des résultats dans le terminal.

## Prérequis

* Python 3

* Nmap

* Bibliothèque python-nmap

Installation de la bibliothèque Python

```bash
pip install python-nmap
```
Assurez-vous que Nmap est installé et accessible depuis le PATH du système.

## Utilisation
Lancer le script
```bash
python scan_nmap.py
```
Entrer l’adresse IP à scanner lorsque demandé.

## Options Nmap utilisées
* -sV Détection des versions des services

* -T4 Accélération du scan

* 1-1024 Plage des ports standards

## Exemple de sortie
```bash
Hôte : 192.168.1.1
État : up
Protocole : tcp
Port 22 : open | Service : ssh OpenSSH 8.2
Port 80 : open | Service : http Apache 2.4.41
```
