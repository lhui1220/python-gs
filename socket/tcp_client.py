from socket import *
from threading import *

HOST = '127.0.0.1'
PORT = 8080

socket_cli = socket(AF_INET,SOCK_STREAM)

socket_cli.settimeout(5)
socket_cli.connect((HOST, PORT))


def recv_msg(socket):
	msg = socket.recv(1024)
	print 'RECV:', repr(msg)
	

def start_recv(socket):
	thread = Thread(name='Thread-Recv', targe=recv_msg, args=socket)
	thread.start()
	return thread

print "let's chat"
while 1:
	in_str = raw_input()
	msg = in_str.split(':')
	if len(msg) != 2:
		print 'Usage: cmd:message \n e.g chat:hello,world'
		continue
	
	cmd = msg[0]
	content = msg[1]

	socket_cli.sendall(cmd)
	if cmd == 'exit':
		break

socket_cli.close()
print 'quit chat'

