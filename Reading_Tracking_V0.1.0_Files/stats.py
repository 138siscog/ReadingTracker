import customtkinter as ctk

class StatsPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.some_attribute = "Hello from StatsPage"
        self.entry = ctk.CTkEntry(self, placeholder_text="test3")
        self.entry.pack(pady=10)
        self.entry = ctk.CTkEntry(self, placeholder_text="test4")
        self.entry.pack(pady=10)