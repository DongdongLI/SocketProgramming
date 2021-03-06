#!/usr/bin/python

"""client.py - A Python code for simulating a client which can handle GET and PUT requests."""
'''
__name__ = "client"
__author__ = "Naveen Mysore <nmysore@uncc.edu>"
'''

import socket
import sys

par = str(sys.argv)
#-------------------------------- Fetching the host name/address
arguments = par.split()
#------------------------ Server
end = len(arguments[1])
start = 1
end =  end -2
server = arguments[1][start:end]
#-------------------------------
#------------------------ Port
end = len(arguments[2])
start = 1
end =  end -2
port = int(arguments[2][start:end])
#-----------------------------
#------------------------ Command
end = len(arguments[3])
start = 1
end =  end -2
com = arguments[3][start:end]
#-----------------------------
#------------------------ File
end = len(arguments[4])
start = 1
end =  end -2
filead = arguments[4][start:end]
#-----------------------------
permission = 1;
#---------------------------------
#--------------------------- Connecting the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server, port))
#---------------------------------GET method implemented
if com == "GET" :
	recvd = ''
	request = "GET "+filead+" "+"HTTP/1.0\r\n\r\n"
	s.send(request)
        data = s.recv(9024)
	print data
	data = s.recv(9024)
	print data
	s.close()
#--------------------------------- PUT method implemented
if com == "PUT":
	try:
    		f = open(filead, "rb")
	except IOError:
    		print 'No such file exists'
    		permission = 0
    		filead = "400"
    		request = "PUT "+filead+" "+"HTTP/1.0\r\n\r\n"
    		s.send(request)
    		data = s.recv(1024)
		print data
    	if(permission):
    		print "found file: " + filead
    		request = "PUT "+filead+" "+"HTTP/1.0\r\n\r\n"
    		s.send(request)
    		data = s.recv(1024)
		print data
		data = f.read()
		f.close()
		s.sendall(data)
		s.sendall(data)
		s.close()
	
if com != "PUT" and com != "GET":
	print "Invalid request"
#------------------------------------------------------------
