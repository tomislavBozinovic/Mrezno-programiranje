import socket
import datetime
from local_machine_info import print_machine_info
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
start = datetime.datetime.now()

print('Vrijeme pokretanja programa: ' , datetime.datetime.now())
print('Program se izvodi na ovom računalu: ')
print_machine_info()

print('--------------------------------------------------------------')

hostAddress = input('Molimo unesite adresu hosta: ')
ipAddress = socket.gethostbyname(hostAddress)
print ('Skeniram host: ', hostAddress, ' IP adresa: ', ipAddress)

portNum1 = int(input('Početni port >> '))
portNum2 = int(input('Završni port >> '))

def scanner(port):
    try:
        sk.connect((hostAddress, port))
        return True
    except:
        return False

for portNumber in range(portNum1,portNum2):
    print("Skeniram port: ", portNumber)
    if scanner(portNumber):
        print('Port', portNumber, 'je otvoren')

print ('Skeniranje portova završeno!!!')

end = datetime.datetime.now()
print ('Vrijeme potrebno za završetak skeniranja: %s' % (end-start))

# https://linuxhint.com/python-for-hacking-port-scanner/