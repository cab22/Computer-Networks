# Uso: "python ProxyServer.py server_ip", em que server_ip é o endereço IP do servidor proxy

from socket import *
import sys
import threading

# if len(sys.argv) <= 1:
#     print('Uso: "python ProxyServer.py server_ip"\n[server_ip : Endereço IP do servidor proxy')
#     sys.exit(2)


def core_thread (client):

    message=client.recv(1024)

    print(message)
    hostline= message.split(b'\r\n')[1]

    tcpSerSock2 = socket(AF_INET, SOCK_STREAM)

    host = hostline.split(b' ')[1]

    print(host)

    tcpSerSock2.connect((host, 80))

    tcpSerSock2.sendall(message+ b'\r\n\r\n')

    while 1:
        # receive data from web server
        data = tcpSerSock2.recv(4096)
        print(data)

        if (len(data) > 0):
            # send to browser
            tcpCliSock.sendall(data)
            print("enviando")
        else:
            print("acabou")
            break
    tcpSerSock2.close()
    tcpCliSock.close()


if __name__ == '__main__':

    tcpSerSock = socket(AF_INET, SOCK_STREAM)
    tcpSerSock.bind(("", 8889))
    tcpSerSock.listen(100)

    while 1:
        tcpCliSock, addr =tcpSerSock.accept()


        t=threading.Thread(target=core_thread, args=(tcpCliSock,))
        t.start()

    tcpSerSock.close()




