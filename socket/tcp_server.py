from socket import *
import random


host = '127.0.0.1'
port = 8080

greetings = ['Zhang san','Li si','Wang wu']

socket_srv = socket(AF_INET, SOCK_STREAM)

address = (host, port)

socket_srv.bind(address)

socket_srv.listen(1)

print 'Server listen at %d \n' % port

socket_cli,cli_info = socket_srv.accept()

print 'Server:a client connected. info=', cli_info

while 1:
	data = socket_cli.recv(1024)
	data = data.rstrip()
	if data == 'chat':
		idx = random.randint(0,len(greetings) - 1)
		socket_cli.send('Server:' + greetings[idx] + '\n')
	elif data == 'exit':
		socket_cli.send('Server:Bye bye!\n')
		print 'Gracefully exit'
		break
	else:
		print 'no op'

socket_cli.close()
socket_srv.close()

