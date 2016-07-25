from socket import *
import ssl
import base64


#Dados necessarios para enviar o email
msg = b'\r\nI love computer networks!'
endmsg = '\r\n.\r\n'
mailserver = 'smtp.gmail.com'
login=b'jorge.santos@ee.ufcg.edu.br'
senha=b'Santos21111464'
destinatario=b'dossantosjorgehenrique@gmail.com'



clientSocket = socket(AF_INET, SOCK_STREAM)

# Número de porta pode mudar conforme servidor de e-mail
clientSocket.connect((mailserver, 587))
recv = clientSocket.recv(1024)
print(recv)
clientSocket.sendall(b'EHLO 192.168.25.6\r\n')
recv = clientSocket.recv(1024)
print(recv)


command = b'STARTTLS\r\n'
clientSocket.send(command)
recvdiscard = clientSocket.recv(1024)
print (recvdiscard)

clientSocketSSL = ssl.wrap_socket(clientSocket)

# clientSocket.sendall(b'HELO 192.168.25.6\r\n')
# recv = clientSocket.recv(1024)
# print(recv)

clientSocketSSL.sendall(b'EHLO 192.168.25.6\r\n')
recv = clientSocketSSL.recv(1024)
print(recv)


encoded = base64.b64encode(b'\000'+login+b'\000'+senha)

clientSocketSSL.send(b'AUTH PLAIN ' +encoded + b'\r\n')
recv = clientSocketSSL.recv(1024)
print(recv)

clientSocketSSL.send(b'MAIL FROM: <'+login+b'>\r\n')
recv = clientSocketSSL.recv(1024)
print(recv)

clientSocketSSL.send(b'RCPT TO: <'+destinatario+b'>\r\n')
recv = clientSocketSSL.recv(1024)
print(recv)

clientSocketSSL.send(b'DATA\r\n')
recv = clientSocketSSL.recv(1024)
print(recv)

clientSocketSSL.send(b'From: login\r\nTO: '+destinatario+b'\r\nSubject: Teste\r\n')
clientSocketSSL.send(msg+b'\r\n')
clientSocketSSL.send(b'.\r\n')

recv = clientSocketSSL.recv(1024)
print(recv)




# clientSocket.sendall(b'MAIL FROM: <dossantosjorgehenrique@gmail.com>\r\n')
# recv = clientSocket.recv(1024)
# print(recv)

