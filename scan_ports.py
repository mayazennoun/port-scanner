import nmap

def quick_nmap_scan():
    nm = nmap.PortScanner()
    target = input("Entrez l'IP à scanner : ")

    print(f"\nScan Nmap en cours sur {target}...")
    print("-" * 40)
    nm.scan(target, '1-1024', '-sV -T4')

    for host in nm.all_hosts():
        print(f"Hôte : {host} ({nm[host].hostname()})")
        print(f"État : {nm[host].state()}")
        
        for proto in nm[host].all_protocols():
            print(f"Protocole : {proto}")
            
            ports = nm[host][proto].keys()
            for port in ports:
                state = nm[host][proto][port]['state']
                service = nm[host][proto][port]['name']
                product = nm[host][proto][port]['product']
                version = nm[host][proto][port]['version']
                
                print(f"Port {port} : {state} | Service : {service} {product} {version}")

if __name__ == "__main__":
    quick_nmap_scan()