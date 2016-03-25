from tkinter.filedialog import *
import tkinter as tk
import config
import base.handler
import base.net
import base.text
import base.clientServer

def clientLaunch(destination, window):
    window.destroy()
    base.clientServer.Client(destination, config.port).start()

def connectClient():
    window = tk.Toplevel(root)
    window.title("Connect")
    window.grab_set()
    tk.Label(window, text="Server IP:").grid(row=0)
    destination = tk.Entry(window)
    destination.grid(row=0, column=1)
    go = tk.Button(window, text="Connect", command=lambda: clientLaunch(destination.get(), window))
    go.grid(row=1, column=1)

def parseText(event):
    data = textInput.get()
    base.text.echoText(data)
    textInput.delete(0, tk.END)

root = tk.Tk()
root.title("p2p Chat")

mainFrame = tk.Frame(root)
mainBody = tk.Frame(mainFrame, height=20, width=50)
inputFrame = tk.Frame(mainFrame, height=20, width=50)

config.mainText = tk.Text(mainBody)

menuBar = tk.Menu(root)

fileMenu = tk.Menu(menuBar, tearoff=0)

fileMenu.add_command(label="Connect", command=lambda: connectClient())
fileMenu.add_command(label="Disconnect", command=lambda: base.handler.eventHandler("-001"))
fileMenu.add_command(label="Exit", command=lambda: root.destroy())
menuBar.add_cascade(label="Options", menu=fileMenu)
root.config(menu=menuBar)


bodyScroll = tk.Scrollbar(mainBody)
config.mainText.focus_set()
bodyScroll.pack(side=tk.RIGHT, fill=tk.Y)
config.mainText.pack(side=tk.LEFT, fill=tk.Y)
bodyScroll.config(command=config.mainText.yview)
config.mainText.config(yscrollcommand=bodyScroll.set)
mainBody.pack(side=tk.TOP)
config.mainText.config(state=tk.DISABLED)

textInput = tk.Entry(inputFrame, width=60)
textInput.bind("<Return>", parseText)
textInput.pack()
inputFrame.pack(side=tk.BOTTOM)

mainFrame.pack(side=tk.LEFT)
