import customtkinter as ctk

class LoadBookPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.some_attribute = "Hello from LodBookPage"
        self.entry = ctk.CTkEntry(self, placeholder_text="test")
        self.entry.pack(pady=10)
        self.entry = ctk.CTkEntry(self, placeholder_text="test2")
        self.entry.pack(pady=10)