host = "scanme.nmap.org"
port = 80
def malware_scanner(host, port):
    malware_detection_socket = socket.socket()
    malware_detectionsockconnect.py_socket.settimeout(1)
    result = malware_detection_socket.connect_ex((host, port))
    if result == 0:
        print(f'Port {port} is open')
    else:
        print(f'Port {port} is closed')
    malware_detection_socket.close()
    return result

result1 = malware_scanner(host, port)

# 1400 - 1450
for port_we_care in range(1400,1451):
    malware_scanner(host, port_we_care)
