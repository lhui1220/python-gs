from ssl import *
from socket import *
from pprint import *

HOST = '127.0.0.1'
PORT = 4443

def new_sslsocket():
	sock = socket(AF_INET, SOCK_STREAM)
	ssl_socket = None
	ca_certs = None
	try:
#		ca_certs = '/usr/lib/ssl/certs/ca-certificates.crt'
#		ssl_socket = wrap_socket(sock, server_side=False,cert_reqs=CERT_REQUIRED,ca_certs=ca_certs)

#	pprint(get_default_verify_paths())
		ssl_ctx = create_default_context(Purpose.SERVER_AUTH)
		ssl_ctx.load_verify_locations(cafile='../certs/cert.pem')
		ssl_socket = ssl_ctx.wrap_socket(sock, server_hostname='liuhui')
		return ssl_socket
	except SSLError as e:
		if ssl_socket:
			sll_socket.close()
		raise e

ssl_socket = new_sslsocket()
if not ssl_socket:
	print 'new sslsocket fail'
	exit(1)
ssl_socket.connect((HOST, PORT))

cert = ssl_socket.getpeercert()

pprint(cert)

count = ssl_socket.sendall('Hello world!')
data = ssl_socket.recv(1024)
print data

ssl_socket.close()
