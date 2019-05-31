#!/usr/bin/env python3
import socket
import subprocess, os, ast
# from werkzeug import exceptions

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 32923   # Port to listen on (non-privileged ports are > 1023)

directory = "/home/adnan/Documents/Networks_Uni/testFiles"

def list_handler(directory):
    response = os.listdir(directory)

    return response

def cat_handler(chosen_file, files_list):
    if chosen_file in files_list:
        try:
            file_path = directory+'/'+chosen_file
            with open(file_path,'r') as f:
                content = f.read()
                return content
        except IOError as e:
            print("Internal file error occurred: %s", e)
            exit(1)
    else:
        print("File not in list!")
        exit(2)



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            action = conn.recv(1024).decode('utf-8')
            print('--------Recieved Data-----------')
            if action == "list":
                ##Handle request and return response
                response = list_handler(directory)
                print(response)
                response = bytes(response.__str__(), 'utf-8')
                conn.send(response)
                # exit(0)
            elif action == "cat":
                ##sending the list for the client to choose a file
                files_list = list_handler(directory)
                print(files_list)
                files_list_bytes = bytes(files_list.__str__(), 'utf-8')
                conn.send(files_list_bytes)

                ##Parsing the chosen file
                chosen_file = conn.recv(1024).decode('utf-8')
                print(chosen_file)
                content = cat_handler(chosen_file,files_list)
                conn.send(bytes(content.__str__(), 'utf-8'))
                # exit(0)