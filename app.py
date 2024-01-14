import os
import shutil
import tkinter as tk
from tkinter import messagebox
from sys import exit


class MainGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.label_path = tk.Label(self.root, text="Path", font=('Arial', 13))
        self.label_path.pack(padx=10, pady=10)

        self.textbox_path = tk.Entry(self.root, font=('Arial', 13))
        self.textbox_path.pack(padx=10, pady=10)

        self.label_extensions = tk.Label(
            self.root, text="Extensions seperated by comma. Eg. png, jpg", font=('Arial', 13))
        self.label_extensions.pack(padx=10, pady=10)

        self.textbox_extensions = tk.Entry(self.root, font=('Arial', 13))
        self.textbox_extensions.pack(padx=10, pady=10)

        self.btn_organize = tk.Button(
            self.root, text="Organize!", font=('Arial', 15), command=self.organize)
        self.btn_organize.pack(padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def on_closing(self):
        if messagebox.askyesno(title="Quit", message="Do you really want to quit?"):
            self.root.destroy()

    def organize(self):
        entered_path = self.textbox_path.get()
        entered_extensions = self.textbox_extensions.get()
        extension_list = []
        is_path_ok = False
        is_extensions_ok = False

        if (entered_path and os.path.exists(entered_path) and os.path.isdir(entered_path)):
            print(f'Path {entered_path} OK')
            is_path_ok = True
        else:
            print('Invalid Path')

        if (entered_extensions):
            extension_list = entered_extensions.replace(" ", "").split(",")
            print(f'Extensions {extension_list} OK')
            is_extensions_ok = True
        else:
            print('Invalid Extensions')

        if (is_path_ok and is_extensions_ok):
            files = os.listdir(entered_path)
            for file in files:
                filename, extension = os.path.splitext(file)
                extension = extension[1:]
                if (extension in extension_list):
                    print(f"I need to move {filename}")
                    destination_dir = f"{entered_path}/{extension}"
                    from_file = f"{entered_path}/{file}"
                    to_file = f"{destination_dir}/{file}"
                    if os.path.exists(destination_dir):
                        print(f"moving {from_file} to {to_file}")
                        shutil.move(from_file, to_file)
                    else:
                        print(f"creating dir {destination_dir}")
                        os.makedirs(destination_dir)
                        print(f"moving {from_file} to {to_file}")
                        shutil.move(from_file, to_file)
            messagebox.showinfo(
                title="Message", message=f"Organized Done at {entered_path}")
        else:
            messagebox.showinfo(
                title="Message", message=f"Invalid Path or Extensions")


MainGUI()
