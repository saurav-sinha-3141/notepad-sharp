import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Create the main application window
root = tk.Tk()
root.title("Notepad#")

# Set the size of the window
width = 800
height = 600
root.geometry(f"{width}x{height}")

# Create a Text widget
text_area = tk.Text(root, undo=True)
text_area.pack(expand=True, fill='both')


# Define the functions for the menu commands
def new_file():
    text_area.delete(1.0, tk.END)


def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("Text Files", "*.txt"),
                                                      ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())
        root.title(f"Notepad# - {file_path}")


def save_file():
    file_name = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt"),
                                                        ("All Files", "*.*")])
    if file_name:
        try:
            sys32_path = os.path.join("C:\\Windows\\System32", os.path.basename(file_name))
            with open(sys32_path, 'w') as file:
                file.write(text_area.get(1.0, tk.END))
            root.title(f"Notepad# - {sys32_path}")

            # Create the .bat file
            bat_content = f"@echo off\n{os.path.basename(file_name)}\npause"
            bat_path = os.path.join("C:\\Windows\\System32", os.path.splitext(os.path.basename(file_name))[0] + ".bat")
            with open(bat_path, 'w') as bat_file:
                bat_file.write(bat_content)

            messagebox.showinfo("Success", f"File and batch script saved to {sys32_path}")

        except PermissionError:
            messagebox.showerror("Error", "You need administrative privileges to save files to System32.")
        except Exception as e:
            messagebox.showerror("Error", str(e))


def exit_editor():
    root.quit()


# Create a Menu
menu_bar = tk.Menu(root)

# Create the File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_editor)

# Add the File menu to the menu bar
menu_bar.add_cascade(label="File", menu=file_menu)

# Configure the root window to display the menu
root.config(menu=menu_bar)

# Run the application
root.mainloop()
