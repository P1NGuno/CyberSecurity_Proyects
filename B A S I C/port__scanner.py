import socket
import threading
import sys
import time
import argparse

DEFAULT_TIMEOUT = 1.0

open_ports = []

lock = threading.Lock()

def scan_port(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.settimeout(DEFAULT_TIMEOUT)
    
        result = s.connect_ex((host, port))

        if result == 0:
            with lock:
                open_ports.append(port)
            print(f"Puerto {port} abierto")

    except socket.error as e:

        if "Host is down" in str(e) or "No route to host" in str(e):
             sys.stderr.write(f"\nError de red para {host}: {e}\n")
             sys.exit(1)

def main():
    # Configuración de Argumentos de Línea de Comandos con argparse
    parser = argparse.ArgumentParser(
        description="Escáner de puertos TCP. Escanea un rango de puertos en un host específico."
    )
    
    parser.add_argument("host", help="La dirección IP o nombre de host a escanear.")
   
    parser.add_argument(
        "-p", "--ports",
        help="Rango de puertos a escanear (ej. '1-1000' o '80,443'). Por defecto: 1-1024.",
        default="1-1024"
    )
    
    parser.add_argument(
        "-t", "--threads",
        type=int,
        help="Número de hilos concurrentes a usar. Por defecto: 100.",
        default=100
    )

    args = parser.parse_args()

    target_host = args.host
    port_range_str = args.ports
    max_threads = args.threads

    # Procesamiento del Rango de Puertos
    ports_to_scan = []
    if '-' in port_range_str:
        
        try:
            start_port, end_port = map(int, port_range_str.split('-'))
            ports_to_scan.extend(range(start_port, end_port + 1))
        except ValueError:
            sys.stderr.write("Error: Formato de rango de puertos inválido. Use 'inicio-fin'.\n")
            sys.exit(1)
    elif ',' in port_range_str:
        
        try:
            ports_to_scan.extend(map(int, port_range_str.split(',')))
        except ValueError:
            sys.stderr.write("Error: Formato de lista de puertos inválido. Use 'p1,p2,p3'.\n")
            sys.exit(1)
    else:
        
        try:
            ports_to_scan.append(int(port_range_str))
        except ValueError:
            sys.stderr.write("Error: Formato de puerto individual inválido.\n")
            sys.exit(1)

    # Filtrar puertos fuera del rango válido (1-65535)
    ports_to_scan = [p for p in ports_to_scan if 1 <= p <= 65535]
    if not ports_to_scan:
        sys.stderr.write("Error: No hay puertos válidos para escanear en el rango especificado.\n")
        sys.exit(1)

    print(f"Escaneando {len(ports_to_scan)} puertos en {target_host} con {max_threads} hilos concurrentes...")
    print("-" * 30)

    # Gestión de Hilos
    
    semaphore = threading.Semaphore(max_threads)
    threads = []
    start_time = time.time()

    for port in ports_to_scan:
        
        semaphore.acquire()
        
        thread = threading.Thread(target=scan_port_with_release, args=(target_host, port, semaphore))
        threads.append(thread)
        thread.start() 

    
    for thread in threads:
        thread.join()

    end_time = time.time()

    print("-" * 30)
    # Mostrar Resultados
    if open_ports:
        print(f"\nPuertos abiertos encontrados en {target_host}:")
        
        open_ports.sort()
        for port in open_ports:
            print(f"- {port}")
    else:
        print(f"\nNo se encontraron puertos abiertos en {target_host} en el rango especificado.")

    print(f"\nEscaneo completado en {end_time - start_time:.2f} segundos.")

# Función auxiliar para liberar el semáforo ---

def scan_port_with_release(host, port, semaphore):
    try:
        scan_port(host, port)
    finally:
        semaphore.release() 




if __name__ == "__main__":
    main()