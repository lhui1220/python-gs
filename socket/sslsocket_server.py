# encoding=utf-8

import ssl
import socket

'''
A ssl socket server for security communication
'''

HOST = '127.0.0.1'
PORT = 4443

# init ssl context
ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ctx.verify_mode = ssl.CERT_NONE # don't verify clients
ctx.load_cert_chain(certfile='../certs/cert.pem', keyfile='../certs/prikey.pem')

# init server socket
sock_srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_srv.bind((HOST,PORT))
sock_srv.listen(1)
print 'server listen at %d' % PORT

def deal_with_client(sock_cli):
	
	while True:
		data = sock_cli.recv(1024)
		print '[RECV] %r' % data
		sock_cli.sendall('Bye bye!')
		break

	sock_cli.close()

# handle client connection

while True:
	conn, addr = sock_srv.accept()
	print 'Connected by %s' % str(addr)
	sock_cli = ctx.wrap_socket(conn, server_side=True)
	deal_with_client(sock_cli)

# Finally,release the server socket.
sock_srv.close()
