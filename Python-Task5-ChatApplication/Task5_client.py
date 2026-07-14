import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

HOST = '127.0.0.1'
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NAME':
                client.send(name_var.get().encode('utf-8'))
            else:
                chat_box.insert(tk.END, message + '\n')
        except:
            chat_box.insert(tk.END, "Disconnected from server\n")
            client.close()
            break

def send():
    message = msg_entry.get()
    if message:
        client.send(message.encode('utf-8'))
        msg_entry.delete(0, tk.END)

# GUI
window = tk.Tk()
window.title("Client - Chat App Advanced")
window.geometry("500x400")

name_var = tk.StringVar()
tk.Label(window, text="Enter Name:").pack()
tk.Entry(window, textvariable=name_var).pack()

chat_box = scrolledtext.ScrolledText(window)
chat_box.pack(padx=20, pady=10)

msg_entry = tk.Entry(window)
msg_entry.pack(pady=5)
tk.Button(window, text="Send", command=send).pack()

thread = threading.Thread(target=receive)
thread.daemon = True
thread.start()

window.mainloop()
