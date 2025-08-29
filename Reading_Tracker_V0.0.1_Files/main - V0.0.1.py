from add_book import AddBookPage
from settings import SettingsPage
from stats import StatsPage
from load_book import LoadBookPage
from tkinter import *
import customtkinter as ctk
from ctypes import windll
from PIL import Image

windll.shcore.SetProcessDpiAwareness(2)

app = ctk.CTk()
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")
app.title("Reading Tracker")
icon_path = ("Logo_Icon.ico")
app.iconbitmap(str(icon_path))
app.geometry("600x400")

bg_image = Image.open("images/Logo_Transparent.png").convert("RGBA")

# Resize the image to fit the window

bg_photo = ctk.CTkImage(light_image=bg_image, dark_image=bg_image, size=(700, 600))
bg_label = ctk.CTkLabel(app, image=bg_photo, text="")
bg_label.place(x=50, y=-50)  # Example: position at (50, 50)

# Configure button event functions
def button_event_add():
    print(pages["add_book"].some_attribute)  # Access the attribute from the existing page
    show_page("add_book")  # Show the AddBookPage

def button_event_load():
    print(pages["load_book"].some_attribute)  # Access the attribute from the existing page
    show_page("load_book")  # Show the LoadBookPage

def button_event_stats():
    print(pages["stats"].some_attribute)  # Access the attribute from the existing page
    show_page("stats")  # Show the StatsPage

def button_event_settings():
    print(pages["settings"].some_attribute)  # Access the attribute from the existing page
    show_page("settings")  # Show the AddBookPage

#sidebad Fram Buttons

sidebar = ctk.CTkFrame(app)
sidebar.grid(row=0, column=0, rowspan=5, sticky="ns", padx=0, pady=0)

add_book_button = ctk.CTkButton(sidebar, text="Add Book", command=button_event_add)
add_book_button.pack(padx=10, pady=8, fill="x")

load_book_button = ctk.CTkButton(sidebar, text="Load Book", command=button_event_load)
load_book_button.pack(padx=10, pady=8, fill="x")

stats_button = ctk.CTkButton(sidebar, text="Stats", command=button_event_stats)
stats_button.pack(padx=10, pady=8, fill="x")

setting_button = ctk.CTkButton(sidebar, text="Settings", command=button_event_settings)
setting_button.pack(padx=10, pady=8, fill="x")

# Page Management
pages = {}

def show_page(page_name):
    for page in pages.values():
        page.grid_forget()
    pages[page_name].grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

# Create Pages
pages["add_book"] = AddBookPage(app)
pages["load_book"] = LoadBookPage(app)  # Placeholder for LoadBookPage
pages["stats"] = StatsPage(app)      # Placeholder for StatsPage
pages["settings"] = SettingsPage(app)
# Add more pages as needed, e.g. pages["stats"] = StatsPage(app)


# Run the application
app.mainloop()