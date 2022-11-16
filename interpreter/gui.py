import tkinter as tk
from tkinter import ttk, BOTH, LEFT


class Gui:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("DeskTable")

        lbl1 = tk.Label(self.root, text="Top level entities", width=6)
        lbl1.pack(side=LEFT, padx=5, pady=5)



        #self.create_messages_list()
        tab_control = ttk.Notebook(self.root)
        # tab_invoices = ttk.Frame(tabControl)
        # tab_clients = ttk.Frame(tabControl)
        self.root.mainloop()

    def add_log(self, message):
        self.messages_list.insert(0, message)

    def create_messages_list(self):
        self.messages_list = tk.Listbox(self.root)
        self.messages_list.pack()


if __name__ == "__main__":
    Gui()
