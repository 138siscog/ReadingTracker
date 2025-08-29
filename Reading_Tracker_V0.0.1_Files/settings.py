import customtkinter as ctk
from tkcalendar import Calendar

class SettingsPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.some_attribute = "Hello from SettingsPage"
        dark_button = ctk.CTkButton(self, text="Dark Mode", command=lambda: ctk.set_appearance_mode("dark"))
        dark_button.pack(pady=10)
        light_button = ctk.CTkButton(self, text="Light Mode", command=lambda: ctk.set_appearance_mode("light"))
        light_button.pack(pady=10)