#!/usr/bin/env python3

import socket, ast

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 32923     # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	while True:
	    val = input("Enter your value either 'list' or 'cat' --->  ")
	    valInBytes = bytes(val, 'utf-8')
	    # print(valInBytes)
	    s.sendall(valInBytes) #there should be a recieve from server
	    print('Sending Command ... ')
	    if val == "list":
	        data = s.recv(1024).decode('utf-8')
	        #print(data)
	        data = ast.literal_eval(data)
	        for idx,item in enumerate(data):
	            print("%s --> %s" %(idx,item))
	    elif val == "cat":
	        data = s.recv(1024).decode('utf-8')
	        #print(data)
	        data = ast.literal_eval(data)
	        for idx,item in enumerate(data):
	            print("%s --> %s" %(idx,item))
	        filename = input("Please enter the file name you want to get its content ---> ")
	        print(filename)
	        filename = bytes(filename, 'utf-8')
	        s.sendall(filename)

	        ##Getting content of the chosen file
	        content = s.recv(1024).decode('utf-8')
	        print(content)
	    else:
	        print("Usage: Enter one of the two supported commands")
	        exit(1)