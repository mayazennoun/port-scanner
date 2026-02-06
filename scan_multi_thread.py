import socket
import concurrent.futures
import threading
from datetime import datetime

print_lock = threading.Lock()

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        
        if result == 0:
            with print_lock:
                print(f"[+] Port {port} est OUVERT")
        
        sock.close()
    except:
        pass

def main():
    target = input("Entrez l'IP à scanner : ")
    start_port = 1
    end_port = 1024
    threads_count = 100

    print("-" * 50)
    print(f"Scan rapide de {target} avec {threads_count} threads...")
    print(f"Démarrage : {datetime.now()}")
    print("-" * 50)

    t1 = datetime.now()

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads_count) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, target, port)

    t2 = datetime.now()
    total = t2 - t1

    print("-" * 50)
    print(f"Scan terminé en {total}")

if __name__ == "__main__":
    main()