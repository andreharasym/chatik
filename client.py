# client.py
import socket
import threading


nickname = input("Choose your nickname : ").strip()
while not nickname:
    nickname = input("Your nickname should not be empty : ").strip()
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ""
port = 5555
my_socket.connect((host, port))


def thread_sending():
    while True:
        message_to_send = input()
        if message_to_send:
            message_with_nickname = nickname + " : " + message_to_send
            # cezar.myencode(message_with_nickname)
            my_socket.send(bytes(message_with_nickname, 'utf-8'))


def thread_receiving():
    # import cezar
    while True:
        message = my_socket.recv(1024)
        # cezar.mydecode(message)                     #дишифруєм повідомлення що отримуєм
        print(message.decode())


thread_send = threading.Thread(target=thread_sending)
thread_receive = threading.Thread(target=thread_receiving)
thread_send.start()
thread_receive.start()




