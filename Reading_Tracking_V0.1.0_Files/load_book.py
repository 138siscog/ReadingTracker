import customtkinter as ctk
import tkcalendar

class LoadBookPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.label = ctk.CTkLabel(self)
        self.label.grid(row=0, column=0, padx=20, pady=20)

    def get_selected_date(self):
        return self.calendar.get_date()