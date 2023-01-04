import tkinter as tk
from tkinter import ttk
import time

class DigitalClock(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Digital Clock")
        self.resizable(False, False)
        self.geometry("500x160+750+400")
        self["bg"] = "black"

        self.style = ttk.Style(self)
        self.style.configure(
            "TLabel",
            background = "black",
            foreground = "red"
        )

        self.label = ttk.Label(
            self,
            text = self.timeString(),
            font = ("Digital-7", 80)
        )
        self.label.pack(expand = True)

        self.label.after(1000, self.update)

    def timeString(self):
        return time.strftime("%H:%M:%S")

    def update(self):
        self.label.configure(text = self.timeString())
        self.label.after(1000, self.update)


if __name__ == "__main__":
    clock = DigitalClock()
    clock.mainloop()
