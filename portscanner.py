from socket import *
def conScan(targetHost, targetPort):
    try:
        connectSocket = socket(AF_INET, SOCK_STREAM)
        connectSocket.connect(targetHost, targetPort)
        print('[+]%d/tcp open'%targetPort)
        connectSocket.close()
    except:
        print('[-]%d/tcp close'%targetPort)

def portScan(targetHost, targetPorts):
    try:
        targetIP = gethostbyname(targetHost)
    except:
        print('[-] Cannot resolve %d'%targetHost)
        return
    try:
        targetName = gethostbyaddr(targetIP)
        print('\n[-] Scan result of: %s'%targetName[0])
    except:
        print('[-] Cannot resolve %s'%targetIP)
    setdefaulttimeout(1)
    for targetPort in targetPorts:
        print('Scanning Port: %d'%targetPort)
        conScan(targetHost, int(targetPort))

if __name__ == '__main__':
    portScan('google.com',[80,22])