import socket
import datetime
import threading
from queue import Queue
from local_machine_info import print_machine_info
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
start = datetime.datetime.now() #pocetak rada skripte
printLock = threading.Lock()

print('Vrijeme pokretanja programa: ' , start)
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
        connection = sk.connect((hostAddress, port))
        with printLock:
            print("Port", port, " je otvoren.")
        connection.close()
    except:
        pass
def threader():
    while True:
        worker = q.get()
        scanner(worker)
        q.task_done()

q = Queue()

for i in range(30):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range(portNum1,portNum2):
    q.put(worker)

q.join()

print ('Skeniranje portova završeno!!!')

end = datetime.datetime.now()
print ('Vrijeme potrebno za završetak skeniranja: %s' % (end-start))