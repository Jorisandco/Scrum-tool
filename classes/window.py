from tkinter import Tk, Frame, Label, Button, StringVar, messagebox
from tkinter import ttk

class Window:
    def run(self, title: str, width: int, height: int):
        self.root =  Tk()
        self.root.title(title)
        self.frame = Frame(self.root)
        self.frame.pack(fill="both", expand=True)
        self.root.geometry(f"{width}x{height}")
        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        self.label = Label(self.frame, text="Welcome to the Scrum Tool")
        self.label.pack(pady=10)

        self.button = Button(self.frame, text="Click Me", command=self.on_button_click)
        self.button.pack(pady=10)

    def on_button_click(self):
        messagebox.showinfo("Information", "Button clicked!")