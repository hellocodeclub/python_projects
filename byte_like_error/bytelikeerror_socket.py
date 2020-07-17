import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send(b'GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n'.encode())

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print (data);
mysock.close()

string_var = b'Hello'.decode('utf-8')
print(type(string_var))

bytes_var = 'Hello'.encode()
print(type(bytes_var))



# Update to mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')