import tkinter as tk
from tkinter import messagebox

class VirtualizationApp:
    def __init__(self, master):
        self.master = master
        master.title("Lite Virtualization App")

        self.label = tk.Label(master, text="Lite Virtualization Software")
        self.label.pack()

        self.create_vm_button = tk.Button(master, text="Create VM", command=self.create_vm)
        self.create_vm_button.pack()

    def create_vm(self):
        messagebox.showinfo("Message", "Creating Virtual Machine")

if __name__ == "__main__":
    root = tk.Tk()
    app = VirtualizationApp(root)
    root.mainloop()

