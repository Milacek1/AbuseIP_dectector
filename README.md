# ABUSEIP-DETECTOR

[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](http://forthebadge.com)  
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

```
______________________________________________________________________________________________
           ____  _    _  _____ ______ _____ _____           _      _            _             
     /\   |  _ \| |  | |/ ____|  ____|_   _|  __ \         | |    | |          | |            
    /  \  | |_) | |  | | (___ | |__    | | | |__) |_____ __| | ___| |_ ___  ___| |_ ___  _ __ 
   / /\ \ |  _ <| |  | |\___ \|  __|   | | |  ___/______/ _` |/ _ \ __/ _ \/ __| __/ _ \| '__|
  / ____ \| |_) | |__| |____) | |____ _| |_| |         | (_| |  __/ ||  __/ (__| || (_) | |   
 /_/    \_\____/ \____/|_____/|______|_____|_|          \__,_|\___|\__\___|\___|\__\___/|_|   
_______________________________________________________________________________________________
```

Ce projet utilise l'API de : abuseipdb.com

## Pour commencer

### Pré-requis

Récuperation de la clé d'API abuseipdb.com :

- Se rendre sur le site https://www.abuseipdb.com/
  - Créer un compte gratuit
  - Se rendre dans l'onglet API et générer une clé d'API
  - Enrengistrer la clé d'API
- Rentrer la clé dans le code ip_abuse.py
  - Ligne 125 du code on trouve la zone à modifier pour insérer sa clé API


### Installation

L'installation du programme est relativement simple, il suffit de git clone le projet et celui-ci est opérationnel.

_Installation_: Executez la commande ``git clone https://github.com/Milacek1/AbuseIP_dectector``

## Usage

```
usage: python3 ip_abuse.py [-h] [-f] [-l file] [-o report] [--csv] 
    
    AbuseIP-detector - IP Scanner of Reputation
    
    optional arguments:
      -h, --help           show this help message and exit
      -f, --format         Format d'adresse IP (ipv4 ou ipv6)
      -l file              Fichier texte contenant les adresses IP
      -o report            Fichier de sortie pouvant être au format texte ou csv
      --csv                Ecrit un CSV log 

```

## Examples :

Pour une utilisation simple :
```
python3 ip_abuse.py
```

Pour une utilisation avec un fichier texte en entrée :
```
python3 ip_abuse.py -l ip_in.txt
```

Pour une utilisation avec un fichier texte en entrée avec un rapport en sortie :
```
python3 ip_abuse.py -l ip_in.txt -o rapport.txt
```

Pour une utilisation avec un fichier texte en entrée avec un rapport en sortie en csv :
```
python3 ip_abuse.py -l ip_in.txt -o rapport.csv --csv
```

## Fabriqué avec

* [Python](https://www.python.org/) - Python est un langage de programmation interprété, multiparadigme et multiplateformes. Il favorise la programmation impérative structurée, fonctionnelle et orientée objet.

## Auteurs

* **Milacek** (https://github.com/Milacek1)
