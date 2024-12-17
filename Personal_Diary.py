import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os

# Function to save diary entry
def save_entry():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
    )
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_widget.get(1.0, tk.END))
        messagebox.showinfo("Success", "Diary entry saved successfully!")

# Function to clear text
def clear_text():
    text_widget.delete(1.0, tk.END)

# Set up the main window
root = tk.Tk()
root.title("Personal Diary")
root.geometry("600x400")

# Create a Text widget
text_widget = tk.Text(root, wrap="word", width=60, height=20)
text_widget.pack(padx=10, pady=10)

# Create a Save button
save_button = tk.Button(root, text="Save Entry", command=save_entry)
save_button.pack(side="left", padx=10, pady=10)

# Create a Clear button
clear_button = tk.Button(root, text="Clear", command=clear_text)
clear_button.pack(side="right", padx=10, pady=10)

# Run the application
root.mainloop()
