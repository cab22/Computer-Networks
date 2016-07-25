from socket import *
from pathlib import Path
import os
##import sendfile

#!/usr/bin/python


s = socket(AF_INET,SOCK_STREAM)
s.bind(("",9002)) # Connect
s.listen(5)
while True:
        c, a =s.accept()
        data=c.recv(10000)
        request= data.split(b'\r\n',1)[0]
        print(request)
        comando, resto = request.split(b' ',1)
        objeto, r1 = resto.split(b' ',1)
        print(comando)
        if comando==b'GET':
            print("OK")
            print(objeto.decode("utf-8"))
           
            offset=0
            p= Path(objeto.decode("utf-8"))
            print (p.exists())
            if p.exists():
                print("enviando..")
                
                file= open(objeto.decode("utf-8"), "rb")
                print(file.closed)
                c.send(b'HTTP/1.1 200 OK\r\nConnection: close\r\n\r\n')
                while True:
                        print("enviando2..")
                        chunk = file.read(655536)
                        if not chunk:
                                break
                                c.close()
                        c.send(chunk)
                        
            else:
                    print("Nao Encontrado")
                    c.sendall(b"404 Nao Encontrado")
                    c.close()

                
                
        else:
                print("Comando Desconhecido")
        print ("Received connection from", a)
        print (data)
       
        c.close



