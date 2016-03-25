import config
import tkinter as tk
import base.net

def echoText(text):
    echoScreen(text, config.username)
    for person in config.sendArr:
        base.net.sendData(person, text)

def echoScreen(text, username=""):
    config.mainText.config(state=tk.NORMAL)
    config.mainText.insert(tk.END, '\n')
    if username:
        config.mainText.insert(tk.END, username + ": ")
    config.mainText.insert(tk.END, text)
    config.mainText.yview(tk.END)
    config.mainText.config(state=tk.DISABLED)
