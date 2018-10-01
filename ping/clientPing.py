import socket
import time

udp_ip_send = "177.105.60.80"
udp_port_send = 5002

clientSocket= socket.socket(socket.AF_INET, # Internet 
                      socket.SOCK_DGRAM)    # UDP

clientSocket.settimeout(0.250)

numberLosts = 0
sumRtt = 0
numberConfirmed = 0

for i in range(0,20):
    sequence_number = i
    start = time.time()
    clientSocket.sendto("Ping " + str(i) + "\n", (udp_ip_send, udp_port_send))

    try:
        message, address = clientSocket.recvfrom(1024)
    except socket.timeout:
        numberLosts += 1
        time.sleep(1)
        print("Timeout!\n")
        continue

    end = time.time()
    
    if message != '':
        rtt = end - start
        sumRtt += rtt
        numberConfirmed += 1
        print(message + "RTT = " + str(rtt) + "\n")

    time.sleep(1)

print("RTT medio = " + str(sumRtt/numberConfirmed))
print("Numero de pacotes perdidos = " + str(numberLosts))