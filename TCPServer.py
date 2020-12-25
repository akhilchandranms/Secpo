import socket
class TCPServer:
    def server_connect():

        socketObject=socket.socket()
        hostname = socket.gethostname()    
        ipAddr= socket.gethostbyname(hostname)
        print('Starting TCPDream Server...')   
        port=int(input('[+] Enter the port number to listen:'))
        socketObject.bind((ipAddr,port))
        socketObject.listen(1)
        print('[+] Started listeing in %d' %(port))
        conn, addr=socketObject.accept()
        print('[+] Incoming connection from :',addr)

        while True:
            command=input("Shell>")
            if ':q' in command:
                conn.send(':q'.encode())
                conn.close()
                break
            elif '':
                pass
            else:
                conn.send(command.encode())
                print(conn.recv(1024).decode())