from tkinter import Tk, Frame, Label, Button, StringVar, messagebox
from tkinter import ttk

class Window:
    def run(self, title: str, width: int, height: int):
        self.root =  Tk()
        self.root.title(title)
        self.frame = Frame(self.root)
        self.frame.pack(fill="both", expand=True)
        self.root.geometry(f"{width}x{height}")
        # self.login_screen()
        self.project_screen()
        self.root.mainloop()
        
    #screens

    def login_screen(self):
        self.frame.pack(fill="both", expand=True)
        self.addLabel("Login", 10)
        self.addEntry("Username", 10)
        self.addEntry("Password", 10)
        self.addButton("Login", self.login, 10)

    def project_screen(self):
        self.frame.pack(fill="both", expand=True)
        self.addLabel("Project", 10)
        self.addButton("Create Project", self.create_project, 10)


    ## widgets

    def addButton(self, text: str, command, pady: int):
        self.button = Button(self.frame, text=text, command=command)
        self.button.pack(pady=pady)

    def addLabel(self, text: str, pady: int):
        self.label = Label(self.frame, text=text)
        self.label.pack(pady=pady)

    def addEntry(self, text: str, pady: int):
        self.entry = StringVar()
        self.entry_widget = ttk.Entry(self.frame, textvariable=self.entry)
        self.entry_widget.pack(pady=pady)
        self.label = Label(self.frame, text=text)
        self.label.pack(pady=pady)

    def create_test_widgets(self):
        self.addLabel("Welcome to the Scrum Tool", 10)
        self.addButton("Click Me", self.on_button_click, 10)

    # button functions

    def on_button_click(self):
        messagebox.showinfo("Information", "Button clicked!")

    def login(self):
        print("Login button clicked")

    def create_project(self):
        print("Create Project button clicked")