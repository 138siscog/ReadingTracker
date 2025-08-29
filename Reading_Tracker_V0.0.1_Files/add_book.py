import customtkinter as ctk
from tkcalendar import Calendar

class AddBookPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.some_attribute = "Hello from AddBookPage"
        self.entry = ctk.CTkEntry(self, placeholder_text="Book Title")
        self.entry.pack(pady=10)
        self.entry = ctk.CTkEntry(self, placeholder_text="Number of pages")
        self.entry.pack(pady=10)
        self.entry = ctk.CTkEntry(self, placeholder_text="Start Date")
        self.entry.pack(pady=10)