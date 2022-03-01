from cgitb import text
from distutils.log import error
from textwrap import fill
import tkinter as tk
from tkinter import BOTH, Entry, scrolledtext
from tkinter.tix import COLUMN
import client
from tkinter.ttk import *
import threading



window = tk.Tk()
window.title("Register")
window.geometry("250x150")
# window.rowconfigure([0, 1, 2, 3, 4, 5], minimize = 50)
# window.columnconfigure( [0, 1], minsize=50)

def send_message(new_window, username):
    message = new_window.inputLine.get(0, tk.END)
    if message != "":
        message = message.strip()
        new_window.text_area.config(state='normal')
        new_window.text_area.insert(tk.INSERT, message + "\n")
        new_window.text_area.config(state='disabled')
        new_window.inputLine.delete("1.0", "end")
"""
def connect_to_server():
    IP = IP_entry.get(1.0, "end-1c")
    port = port_entry.get(1.0, "end-1c")
    connection = client.connect_to_server(IP, port)
    if connection:
        return
    else:
        error_lbl.grid(row = 0, 
            column = 0)
"""

def open_new_window(username):
    window.destroy()
    chat_window = tk.Tk()
    chat_window.title("Chat")    

    text_area = scrolledtext.ScrolledText(chat_window, 
                            height = 20,
                            width = 50,
                            font = ("Times New Roman", 15),
                            bg = "#D3D3D3")
    text_area.pack(side=tk.TOP)
    text_area.insert(tk.INSERT, "Connected. Welcome To This Chatroom,", username)
    text_area.config(state='disabled')

    inputLine = tk.Text(chat_window, 
                    height = 2, 
                    width = 25)
    inputLine.pack(side=tk.TOP)
    sendButton = tk.Button(chat_window, 
                    text = "Send", 
                    cursor = "hand2", 
                    height = 2, 
                    width = 6, 
                    command = send_message(chat_window, username))
    sendButton.pack(side=tk.TOP)
    
def connect_to_server():
    ip = IP_entry.get()
    port = int(port_entry.get())
    username = username_entry.get()
    print (username)
    if username:
        connection = client.connect_to_server(ip, port)
        if connection:
            open_new_window(username)
        else:
            error_lbl['text'] = "IP/Port not found. please try again"
            error_lbl.grid(row = 4, column = 0, columnspan = 2)
    else:
        error_lbl['text'] = "please enter username"
        error_lbl.grid(row = 4, column = 0, columnspan = 2)
    

IP_label = tk.Label(text = "Enter IP adress:")
IP_label.grid(row = 0, 
            column = 0)

IP_entry = tk.Entry()
IP_entry.grid(row = 0, 
            column = 1)

port_label = tk.Label(text = "Enter port:")
port_label.grid(row = 1,
            column = 0)

port_entry = tk.Entry()
port_entry.grid(row = 1, 
            column = 1)

username_label = tk.Label(text = "Enter username:")
username_label.grid(row = 2,
            column = 0)
username_entry = tk.Entry()
username_entry.grid(row = 2, 
            column = 1)

confirm_button = tk.Button(text = "Confirm", command = connect_to_server)
confirm_button.grid(row = 3, 
            column = 1)

error_lbl = tk.Label()




window.mainloop()
