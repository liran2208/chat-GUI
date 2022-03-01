import tkinter as tk
  
# Top level window
frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('400x200')
# Function for getting Input
# from textbox and printing it 
# at label widget
  
def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    lbl.config(text = "Provided Input: " + inp)
    
# TextBox Creation
inputtxt = tk.Text(frame, height = 5,
                   width = 20)
  
inputtxt.pack()
  
# Button Creation
printButton = tk.Button(frame,
                        text = "Print", 
                        command = printInput)
printButton.pack()
  
# Label Creation
lbl = tk.Label(frame, text = "")
lbl.pack()
frame.mainloop()

"""
import tkinter as tk

window = tk.Tk()
window.title("Chat")
window.geometry("400x500")
# window.rowconfigure([0, 1, 2, 3, 4, 5], minimize = 50)
# window.columnconfigure( [0, 1], minsize=50)

def send_message():
    message = inputLine.get(1.0, "end-1c") 
    lbl.config(text = lbl.cget("text") + message + "\n")
    # inputLine.delete(0, tk.END)


lbl = tk.Label(height = 20, width = 40, background="#D3D3D3")
lbl.place(x = 50)

inputLine = tk.Text(height = 2, width = 25)
inputLine.place(x = 110, y = 320)


sendButton = tk.Button(text = "Send", cursor = "hand2", height = 2, width = 6, command = send_message)
sendButton.place(x = 50, y = 320)


window.mainloop()

"""
"""
from doctest import master
from operator import index
import tkinter as tk

    


window = tk.Tk()
window.title("Chat")
window.geometry('400x500')

def send_message():
    message = inputLine.get()
    lbl.config(text = message + "/n")

lbl = tk.Label(text="hello world", background="#D3D3D3").pack()
inputLine = tk.Entry(master)
inputLine.insert(index = 0,string = "enter message")
sendButton = tk.Button(text = "Send", command = send_message)
inputLine.pack()


window.mainloop()

"""