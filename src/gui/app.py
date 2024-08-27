import tkinter as tk
from .widgets import create_widgets


class CalculatorApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("650x400+300+300")
        self.root.title("PowerCalc v1.00")
        create_widgets(self.root)

    def run(self):
        self.root.mainloop()
