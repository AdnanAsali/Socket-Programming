# Socket-Programming

The primary socket API functions and methods in this module are:
socket(), bind(), listen(), accept(), connect(), send(), recv(), close().
The flow of the project was run as follows :

On The Server Side :

It starts with a connecting socket.socket() creates a socket object after we imported the the library in the intial lines. Two args are passed to the socket() which are → socket.AF_INET, socket.SOCK_STREAM, the first one socket.AF_INET, is the Internet address family for IPv4, the second argument sent is responsible for identifying that we are currently dealing with TCP it is the main protocol for sending and receiving the data between the client and the server.

Then we used the bind() is used to associate the socket with a specific network interface and port number. The values passed to bind() depend on the address family of the socket.

Then the function listen() was used so the server would start listening on the port and checks if there is anything it wants to receive, and this function gives the server the ability to accept any connection coming to its way and this is where we used the function of s.accept().

After getting the client socket object conn from accept(), an infinite while loop is being done to loop over calls to conn.recv(). This reads whatever data the client sends and echoes it back using conn.sendall(). 



On The Client Side :

The initialization process of the client side is a little bit the same when it comes to the socket object using the socket.socket(), then connects to the server and calls s.sendall() to send its message. Lastly, it calls s.recv() to read the server’s reply and then prints it.

Running the Python Scripts :

Running the script is rather easy yet the only step before executing it in the Linux machine would be to use the command “chmod +x” before interpreting the python script.

Steps of code :
The first step of the project starts in the client side where the user has to choose the value the user wants to enter (which is a static “ls” command) that is being send to the server using the s.sendall() function, this fucntion only deals with bytes so casting the data sent to the server is a needed process, and the casting operation was done using the statement  “ valInBytes = bytes(val, 'utf-8') “ the parameter val is the value the user has entered which is the “ls” command, and the second parameter is the encoding scheme the function is using which is “utf-8”.

After the operation of sending the “ls” command to the server, the server’s turn comes where it has to receive the data that was send to it, and that is by the statement 
data = conn.recv(1024) , The bufsize argument of 1024 used above is the maximum amount of data to be received at once. It doesn’t mean that recv() will return 1024 bytes.

The next step in the flow would be by using the python library OS using the statement “import os” this library helps us in making python execute unix commands in terminal and that happened when we execute the command “ls” in the unix shell using the statement “response = os.listdir("/home/adnan/Documents/Networks_Uni/testFiles")” where it used the listdir() function that takes the path it wants to list.

Following up is the step where we have to send the “ls” output to the client side from the server, and that is being handled by the statement 
 “ response = bytes(response.__str__(), 'utf-8') ” , this way you cast the list in python to bytes using the last statement.

And this process keeps following up when dealing between the client and the server in exchanging data and manipulating it using bytes lists and integers.

A sample Run of the program :

# Client Side :

![image](https://user-images.githubusercontent.com/36306586/58715483-a159da00-83cf-11e9-9322-1ed91b4a5910.png)

# Server Side :

![image](https://user-images.githubusercontent.com/36306586/58715569-d0704b80-83cf-11e9-9295-2f78fbe93150.png)

On the right side of the screen you see the server side terminal on my ubuntu machine
and on the left side of the screen you can see the client side.

As you can see its synchronized with each other and the results being shared between the server and the client can be seen on both terminals whether it was on the server side or the client side 
