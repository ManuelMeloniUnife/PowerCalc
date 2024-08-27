import tkinter as tk
from tkinter import StringVar
from tkinter import Entry
from tkinter import Frame


def create_widgets(root):
    data = StringVar()
    # creazione dell'area "display", dove verranno inseriti i numeri da tastiera.

    display = Entry(root, font="verdana 18", fg="white", bg="#22252d",
                    justify="right", insertbackground="#abbab1", cursor="arrow")
    display.pack(expand="true", fill="both")

    # creazione tastierino tramite righe dove verranno inseriti i singoli buttons
    # PRIMA RIGA
    btnrow1 = Frame(root, bg="#282c35")
    btnrow1.pack(expand="true", fill="both")

    # SECONDA RIGA
    btnrow2 = Frame(root, bg="#282c35")
    btnrow2.pack(expand="true", fill="both")
    # TERZA RIGA
    btnrow3 = Frame(root, bg="#282c35")
    btnrow3.pack(expand="true", fill="both")
    # QUARTA RIGA
    btnrow4 = Frame(root, bg="#282c35")
    btnrow4.pack(expand="true", fill="both")
