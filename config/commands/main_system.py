import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
from colorama import init, Fore
import utils

# Colorama'yı başlat
init(autoreset=True)

def resize_image(input_path, output_path, user_size):
    img = Image.open(input_path)
    original_width, original_height = img.size

    # User-specified dimensions
    user_width, user_height = user_size

    # Original aspect ratio
    original_ratio = original_width / original_height
    user_ratio = user_width / user_height

    # Resize the image maintaining aspect ratio
    if original_ratio > user_ratio:
        new_width = user_width
        new_height = int(user_width / original_ratio)
    else:
        new_height = user_height
        new_width = int(user_height * original_ratio)

    # Resize the image with LANCZOS filter
    resized_img = img.resize((new_width, new_height), Image.LANCZOS)

    # Save the resized image
    resized_img.save(output_path)

def open_file_dialog():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(
        title="Select an image file",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )
    return file_path

def save_file_dialog(default_save, input_file):
    if not default_save:
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        # Output path, same directory as input file
        directory = os.path.dirname(input_file)
        save_path = filedialog.asksaveasfilename(
            title="Select the save location",
            initialdir=directory,  # Set initial directory to the input file's directory
            defaultextension=os.path.splitext(input_file)[1],  # Preserve the original extension
            filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png"), ("BMP", "*.bmp"), ("GIF", "*.gif")]
        )
    else:
        save_path = os.path.join(os.path.dirname(input_file), "output" + os.path.splitext(input_file)[1])  # Save with original extension

    return save_path

def ask_default_save():
    return messagebox.askyesno("Save Option", "Do you want to save the file as 'output' with the original extension?")

def get_resize_dimensions():
    while True:
        try:
            user_width = int(input("Enter the width in pixels: "))
            user_height = int(input("Enter the height in pixels: "))
            return (user_width, user_height)
        except ValueError:
            utils.warning("Invalid input! Please enter valid numbers.")

def execute():
    # Ask the user if they want to use the automatic GUI
    utils.info("Do you want to use the automatic file picker dialog? (Y/N): ")
    gui_choice = input().strip()

    if gui_choice.lower() == "y":
        # Open file dialog
        input_file = open_file_dialog()
        if not input_file:
            utils.warning("No file selected. Exiting...")
            return
    elif gui_choice.lower() == "n":
        # Manually enter file path
        input_file = input("INFO: Enter the image file path: ")
        if not os.path.isfile(input_file):
            utils.error("File not found! Please try again.")
            return
    else:
        utils.error("Invalid input! Please enter either 'y' or 'n'. Exiting...")
        return

    utils.info(f"Selected image: {input_file}")

    # Get the resize dimensions
    user_size = get_resize_dimensions()

    # Ask the user if they want to use the default save location
    default_save = ask_default_save()

    # Allow the user to specify the save location
    output_file = save_file_dialog(default_save, input_file)

    if output_file:
        try:
            # Resize and save the image
            resize_image(input_file, output_file, user_size)
            messagebox.showinfo("Success", f"INFO: Image saved successfully: {output_file}")
        except Exception as e:
            messagebox.showerror("Error", f"ERROR: Failed to save the image. {str(e)}")
    else:
        messagebox.showwarning("Cancelled", "WARNING: The save operation was cancelled.")

if __name__ == "__main__":
    execute()
