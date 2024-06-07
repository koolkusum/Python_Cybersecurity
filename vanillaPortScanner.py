import socket

def get_local_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

def port_scan(ip, port_range):
    open_ports = []
    for port in range(port_range[0], port_range[1] + 1):
        #ipv4 socket and TCP stream
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

if __name__ == "__main__":
    local_ip = get_local_ip()
    print(f"Local IP Address: {local_ip}")

    #ssh, http, https, mysql
    common_ports = [22, 80, 443, 3306]
    #note to self run this command to serve HTTP on port 80
    #python -m http.server 80
    open_ports = port_scan(local_ip, (50, 100))
    
    print(f"Open Ports: {open_ports}")

    print(f"Scanning common ports on IP: {local_ip}")
    for port in common_ports:
        open_ports = port_scan(local_ip, (port, port))
        if open_ports:
            print(f"Port {port} is open")
