from socket import *
import sys


if len(sys.argv) <= 1:
  print 'Usage : "python proxyserver.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server]\n'

# Create a server socket, bind it to a port and start listening
tcpSerPort = 8888
tcpSerSock = socket(AF_INET, SOCK_STREAM)

tcpSerSock.bind(('', tcpSerPort))
tcpSerSock.listen(5)

while True:
  # Strat receiving data from the client
  print('Ready to serve...')
  tcpCliSock, addr = tcpSerSock.accept()
  print('Received a connection from:', addr)
  message = tcpCliSock.recv(1024) # Fill in start. # Fill in end.
  print(message)
  # Extract the filename from the given message
  print message.split()[1]
  filename = message.split()[1].partition("/")[2]
  print(filename)
  fileExist = "false"
  filetouse = "/" + filename
  print(filetouse)
  try:
	# Check whether the file exist in the cache
	f = open(filetouse[1:], "r")
	outputdata = f.readlines()
	fileExist = "true"
	# ProxyServer finds a cache hit and generates a response message
	tcpCliSock.send("HTTP/1.0 200 OK\r\n")
	tcpCliSock.send("Content-Type:text/html\r\n")
	for i in range(0, len(outputdata)):
	  tcpCliSock.send(outputdata[i])
	print 'Read from cache'
  
  except IOError:
	print 'File Exist: ', fileExist
	if fileExist == "false":
	  # Create a socket on the proxyserver
	  print 'Creating the socket on the proxyserver'
	  c = socket(AF_INET, SOCK_STREAM)
	  hostn = filename.replace("www.","",1)
	  print 'Host Name: ' + hostn
	  try:
		# Connect to the socket to port 80
		# Fill in start.
		# Fill in end.
		c.connect((hostn, 80))
		print 'Socket has connected'
		# Create a temporary file on this socket and ask port 80 for
		# the file requested by the client
		fileobj = c.makefile('r', 0)
		fileobj.write("GET "+"http://" + filename + " HTTP/1.0\n\n")
		# Read the response into buffer
		buff = fileobj.readlines()
		
		# Fill in start.
		# Fill in end.
		# Create a new file in the cache for the requested file.
		# Also send the response in the buffer to client socket and
		# the corresponding file in the cache
		tmpFile = open("./" + filename,"wb")
		for i in range(0, len(buff)):
		  tmpFile.write(buff[i])
		  tmpCliSock.send(buff[i])
		# Fill in start.
		# Fill in end.
	  except:
		print("Illegal request")
	else:
		print "404: File not found"
# Close the client and the server sockets
tcpCliSock.close()

if __name__ == '__main__':
	main()