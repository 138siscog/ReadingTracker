from tkinter import *
import customtkinter as ctk


app = ctk.CTk()

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

app.title("Reading Tracker")
icon_path = ("Logo_Icon.ico")
app.iconbitmap(str(icon_path))
app.geometry("800x600") # Width x Height

def button_event_add():
    print("Add Book button pressed")

def button_event_load():
    print("Load Book button pressed")

def button_event_stats():
    print("stats button pressed")

def button_event_settings():
    print("Settings button pressed")

add_book_button = ctk.CTkButton(app, text="Add Book", command=button_event_add)
add_book_button.grid(row=1, column=0, padx=10, pady=8, sticky="ew")

load_book_button = ctk.CTkButton(app, text="Load Book", command=button_event_load)
load_book_button.grid(row=2, column=0, padx=10, pady=8, sticky="ew")

stats_button = ctk.CTkButton(app, text="Stats", command=button_event_stats)
stats_button.grid(row=3, column=0, padx=10, pady=8, sticky="ew")

setting_button = ctk.CTkButton(app, text="Settings", command=button_event_settings)
setting_button.grid(row=4, column=0, padx=10, pady=8, sticky="ew")

app.mainloop()
