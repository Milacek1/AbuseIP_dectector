import subprocess
import json
import argparse
import csv
from datetime import datetime
import re

def check_ip(ip_address, api_key):
    command = [
        "curl",
        "-G",
        "https://api.abuseipdb.com/api/v2/check",
        "--data-urlencode",
        f"ipAddress={ip_address}",
        "-d",
        "maxAgeInDays=90",
        "-d",
        "verbose",
        "-H",
        f"Key: {api_key}",
        "-H",
        "Accept: application/json"
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    data = json.loads(result.stdout)
    return data

def read_ips_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    ips = set()  # Utiliser un ensemble pour éviter les doublons d'adresses IP
    for line in lines:
        line = line.strip()
        # Utiliser une expression régulière pour trouver les adresses IP dans chaque ligne
        ip_matches = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', line)
        ips.update(ip_matches)

    return list(ips)


def save_to_text(result, output_file):
    with open(output_file, 'a') as file:
        filtered_result = {
            "ipAddress": result["data"]["ipAddress"],
            "countryName": result["data"]["countryName"],
            "isPublic": result["data"]["isPublic"],
            "abuseConfidenceScore": result["data"]["abuseConfidenceScore"],
            "usageType": result["data"]["usageType"],
            "isp": result["data"]["isp"],
            "domain": result["data"]["domain"],
            "hostnames": result["data"]["hostnames"],
            "isTor": result["data"]["isTor"],
            "lastReportedAt": result["data"]["lastReportedAt"],
            "totalReports": result["data"]["totalReports"],
            "numDistinctUsers": result["data"]["numDistinctUsers"],
            "reports": result["data"]["reports"][:3]
        }
        file.write(json.dumps(filtered_result, indent=2))
        file.write("\n---\n")
        file.write("Adresse IP suivante : "+"\n")

def save_to_csv(result, output_file):
    with open(output_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            result['ipAddress'], result['countryName'], result['isPublic'], result['abuseConfidenceScore'],
            result['usageType'], result['isp'], result['domain'], result['hostnames'], result['isTor'],
            result['lastReportedAt'], result['totalReports'], result['numDistinctUsers'],
            json.dumps(result['reports'][:3])
        ])

            

def main():
    ### Partie Affichage du Script :
    print("\n")
    print("                    Bienvenue dans le script de vérification d'adresse IP !")
    print("______________________________________________________________________________________________")
    print("______________________________________________________________________________________________")
    print("           ____  _    _  _____ ______ _____ _____           _      _            _             ")
    print("     /\   |  _ \| |  | |/ ____|  ____|_   _|  __ \         | |    | |          | |            ")
    print("    /  \  | |_) | |  | | (___ | |__    | | | |__) |_____ __| | ___| |_ ___  ___| |_ ___  _ __ ")
    print("   / /\ \ |  _ <| |  | |\___ \|  __|   | | |  ___/______/ _` |/ _ \ __/ _ \/ __| __/ _ \| '__|")
    print("  / ____ \| |_) | |__| |____) | |____ _| |_| |         | (_| |  __/ ||  __/ (__| || (_) | |   ")
    print(" /_/    \_\____/ \____/|_____/|______|_____|_|          \__,_|\___|\__\___|\___|\__\___/|_|   ")
    print("______________________________________________________________________________________________")
    print("---------------------------------Made by : Milacek-------------------------------------------")
    print("--------------------------Don't forget to enter your API Key----------------------------------"+"\n")
    ### Fin Partie Affichage :
    
    # Analyse des arguments de ligne de commande :
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--file', help="Fichier texte contenant les adresses IP")
    parser.add_argument('-f', '--format', choices=['ipv4', 'ipv6'], help="Format d'adresse IP (ipv4 ou ipv6)")
    parser.add_argument('-o', '--output', help="Fichier texte de sortie")
    parser.add_argument('--csv', action='store_true', help="Fichier de sortie en format CSV")
    args = parser.parse_args()
    
    
    # Récupération de la liste d'adresses IP
    
    ip_list = []

    if args.file:
        ip_list = read_ips_from_file(args.file)
    else:
        if args.format:
            ip_prompt = f"Entrez la liste d'adresses IP au format {args.format} (séparées par des virgules) : "
        else:
            ip_prompt = "Entrez la liste d'adresses IP (séparées par des virgules) : "

        ip_input = input(ip_prompt).strip()

        if ip_input:
            ip_list = ip_input.split(",")

    if not ip_list:
        print("Aucune adresse IP fournie.")
        return
    
    ### 
    ###
    api_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # Remplacez par votre clé d'API AbuseIPDBv2
    ###
    ###
    
    if args.output and args.output.strip():
        output_file = args.output.strip()
        if args.csv:
            with open(output_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([
                'ipAddress', 'countryName', 'isPublic', 'abuseConfidenceScore', 'usageType',
                'isp', 'domain', 'hostnames', 'isTor', 'lastReportedAt', 'totalReports',
                'numDistinctUsers', 'reports'])
        else:
            with open(output_file, 'w') as file:
                file.write("-------------------------------"+"\n")
                file.write(f"Rapport IP - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                file.write("-------------------------------"+"\n")
            
            
    for ip_address in ip_list:
        ip_address = ip_address.strip()
        result = check_ip(ip_address, api_key)
        print(f"Résultat pour l'adresse IP {ip_address}:")
        print(json.dumps(result['data'], indent=2))  # Afficher tous les résultats
        print("---------------------------")
        print('---------------------------')
        
         # Enregistrer le résultat dans un fichier de sortie
        if args.output and args.output.strip():
            output_file = args.output.strip()
            if args.csv:
                save_to_csv(result['data'], output_file)
            else:
                save_to_text(result, output_file)
            
    print("Merci d'avoir utilisé le logiciel AbuseIP-detector")
    print("Pour des idées d'améliorations n'hésitez pas à me contacter directement."+'\n')
if __name__ == "__main__":
    main()