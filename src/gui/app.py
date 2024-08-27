import tkinter as tk


class CalculatorApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("650x400+300+300")
        self.root.title("PowerCalc v1.00")
        self.display = tk.Entry(self.root, font="Verdana 20",
                                fg="black", bg="#22252d", bd=4, justify=tk.RIGHT)
        self.display.pack(expand=True, fill=tk.BOTH)

    def run(self):
        self.root.mainloop()
