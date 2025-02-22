import threading
import socket

Target = input("IP: ")

socket.setdefaulttimeout(5)

def ScanPort(port):
    SocketConnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SocketConnection.settimeout(0.5)
    try:
        Connection = SocketConnection.connect((Target, port))
        print(f"Port {port} is open.")
        Connection.close()
    except:
        pass

PortNumber = 1
for _ in range(1, 10000):
    Thread = threading.Thread(target = ScanPort, kwargs = {'port' : PortNumber})
    PortNumber += 1
    Thread.start()