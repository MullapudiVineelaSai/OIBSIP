import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
import datetime

HOST = '127.0.0.1'
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
names = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            timestamp = datetime.datetime.now().strftime("%H:%M")
            full_msg = f"[{timestamp}] ".encode('utf-8') + message
            broadcast(full_msg)
        except:
            index = clients.index(client)
            clients.remove(client)
            name = names[index]
            broadcast(f'{name} left the chat!'.encode('utf-8'))
            names.remove(name)
            client.close()
            break

def receive():
    while True:
        client, address = server.accept()
        client.send('NAME'.encode('utf-8'))
        name = client.recv(1024).decode('utf-8')
        names.append(name)
        clients.append(client)

        log_box.insert(tk.END, f"{name} connected from {address}\n")
        broadcast(f"{name} joined the chat!".encode('utf-8'))
        client.send('Connected to server!'.encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

# GUI
window = tk.Tk()
window.title("Server - Chat App Advanced")
window.geometry("400x300")

log_box = scrolledtext.ScrolledText(window)
log_box.pack(padx=20, pady=10)
log_box.insert(tk.END, f"Server running on {HOST}:{PORT}\n")

thread = threading.Thread(target=receive)
thread.daemon = True
thread.start()

window.mainloop()
