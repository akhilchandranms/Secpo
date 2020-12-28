import socket
import subprocess

def client_connect():
    socketObject=socket.socket()
    servIP=input("Enter the server IP:")
    servPORT=input("Enter the port number:")
    socketObject.connect((servIP,servPORT))
    while True:
        command=socketObject.recv(1024)
        if ':q' in command.decode():
            print("exiting...")
            socketObject.close()
            break
        else:
            CMD=subprocess.Popen(command.decode(),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            socketObject.send(CMD.stdout.read())
            socketObject.send(CMD.stderr.read())
            