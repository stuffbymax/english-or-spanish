import tkinter as tk
from tkinter import ttk, messagebox

import tkinter as tk
from tkinter import ttk, messagebox

def show_message():
    selected_language = language_var.get()
    if selected_language == "English":
        messagebox.showinfo("message", "you are gay")
    elif selected_language == "Spanish":
        messagebox.showinfo("mensaje", "Eres gay!")

# Create the main window
root = tk.Tk()
root.title("Language Selector")
root.geometry("300x200")  # Set the window size
root.configure(bg="#f0f0f0")  # Set a background color

# Style configuration
style = ttk.Style()
style.configure("TLabel", background="#f0f0f0", font=("Helvetica", 12))
style.configure("TButton", background="#007BFF", foreground="white", font=("Helvetica", 12))
style.map("TButton", background=[("active", "#0056b3")])
style.configure("TMenubutton", background="#007BFF", foreground="white", font=("Helvetica", 12))

# Create a variable to hold the selected language
language_var = tk.StringVar(value="English")

# Create a label
label = ttk.Label(root, text="Select your language:")
label.pack(pady=20)

# Create a dropdown menu for language selection
language_menu = ttk.Combobox(root, textvariable=language_var)
language_menu['values'] = ("English", "Spanish")
language_menu['state'] = 'readonly'  # Make it read-only
language_menu.pack(pady=10)

# Create a button to confirm selection
select_button = ttk.Button(root, text="Select", command=show_message)
select_button.pack(pady=20)

# Run the application
root.mainloop()

# Create the main window
root = tk.Tk()
root.title("Language Selector")
root.geometry("300x200")  # Set the window size
root.configure(bg="#f0f0f0")  # Set a background color

# Style configuration
style = ttk.Style()
style.configure("TLabel", background="#f0f0f0", font=("Helvetica", 12))
style.configure("TButton", background="#007BFF", foreground="white", font=("Helvetica", 12))
style.map("TButton", background=[("active", "#0056b3")])
style.configure("TMenubutton", background="#007BFF", foreground="white", font=("Helvetica", 12))

# Create a variable to hold the selected language
language_var = tk.StringVar(value="English")

# Create a label
label = ttk.Label(root, text="Select your language:")
label.pack(pady=20)

# Create a dropdown menu for language selection
language_menu = ttk.Combobox(root, textvariable=language_var)
language_menu['values'] = ("English", "Spanish")
language_menu['state'] = 'readonly'  # Make it read-only
language_menu.pack(pady=10)

# Create a button to confirm selection
select_button = ttk.Button(root, text="Select", command=show_message)
select_button.pack(pady=20)

# Run the application
root.mainloop()
