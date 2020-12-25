import TCPServer
if __name__=="__main__":
    slct=input("[+] Enter 1 for server 2 for client")
    if slct=='1':
        TCPServer.TCPServer.server_connect()
    elif slct=='2':
        clientObject=TCPClient.client_connect()        
    else:
        print("!!Wrong input, good bye !!")
        exit()
  

