from tkinter import Tk, Frame, Label, Button, StringVar, messagebox
from tkinter import ttk

class Window:
    def __init__(self, master):
        self.master = master
        self.master.title("Scrum Tool")
        self.master.geometry("600x400")

        self.create_widgets()

    def create_widgets(self):
        self.frame = Frame(self.master)
        self.frame.pack(fill="both", expand=True)

        self.label = Label(self.frame, text="Welcome to the Scrum Tool")
        self.label.pack(pady=10)

        self.button = Button(self.frame, text="Click Me", command=self.on_button_click)
        self.button.pack(pady=10)

    def on_button_click(self):
        messagebox.showinfo("Information", "Button clicked!")