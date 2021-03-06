from multiprocessing import Pool
import multiprocessing
import socket

from local_machine_info import print_machine_info
import datetime

def scan(x):
    target_ip, port = x

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)

    try: 
        sock.connect((target_ip, port))
        sock.close()

        return port, True

    except (socket.timeout, socket.error):
        return port, False

if __name__ == '__main__':
    start_time = datetime.datetime.now()

    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print('Vrijeme pokretanja programa: ' , datetime.datetime.now())
    print('Program se izvodi na ovom računalu: ')
    print_machine_info()

    print('--------------------------------------------------------------')

    hostAddress = input('Molimo unesite adresu hosta: ')
    ipAddress = socket.gethostbyname(hostAddress)
    print ('Skeniram host: ', hostAddress, ' IP adresa: ', ipAddress)

    portNum1 = int(input('Početni port >> '))
    portNum2 = int(input('Završni port >> '))


    ports = range(int(portNum1), int(portNum2))
    scanlist = [(hostAddress, port) for port in ports]

    pool = Pool(multiprocessing.cpu_count()*2)

    for port, status in pool.imap(scan, scanlist):
        if status:
            print("Port: ", port, " je otvoren.")
    print("Završeno skeniranje ", hostAddress)

    end_time = datetime.datetime.now()
    print(f"Gotovo za {(end_time-start_time).total_seconds()} sekundi.")