import time
import requests
import re
import random

def valiDomain ():
    patron = r"^[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"  # Ej: google.com, ejemplo.org, test-site.net
    while True:
        domain = input("Ingrese el domain con este formato (ej: xxxxx.xxx):\n")
        if re.match(patron, domain):
            return domain
        else:
            print("Por favor, ingrese un domain válido con el formato correcto.")



def main():

    protocol = 'https://'
    subDomainFind = []

    # Solicitamos el domain
    print("-" * 30)
    domain = valiDomain()

    # Se abre solo el documento y se cierra solo
    with open("subDomains.txt") as doc:

    
        ## Empezamos a contar cuanto tiempo tarda en realizar la busqueda
        start_time = time.time()

        for line in doc:
            subdominio = line.strip()
            url = f"{protocol}{subdominio}.{domain}"

            headers = {"User-Agent": "Mozilla/5.0 (compatible; SubdomainScanner/1.0)"}
            
            try:
                response = requests.get(url, headers=headers, timeout=5)
                if response.status_code == 200:
                    subDomainFind.append(url)
            except requests.RequestException:
                pass  # ignorar subdominios que fallan

            time.sleep(random.uniform(0.5, 1.5))  # prevenir bloqueos

        end_time = time.time()

    print(f"\n⏱ Tiempo total: {end_time - start_time:.2f} segundos")
    
    print(f"\n🔍 Se encontraron {len(subDomainFind)} subdominios válidos:\n")
    for dom in subDomainFind:
        print(dom)


if __name__ == "__main__":
    main()
