# add_book.py
import customtkinter as ctk
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from datetime import datetime

# --- Database setup (module-level, created once on import) ---
db = create_engine('sqlite:///./database/database_books.db', echo=False, future=True)
metadata = MetaData()

books = Table(
    "books",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("title", String, nullable=False),
    Column("number_of_pages", String),
    Column("start_date", String),
    Column("end_date", String),
)
metadata.create_all(db)

class AddBookPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=master.cget("fg_color"))
        self.some_attribute = "Hello from AddBookPage"
        
        # --- UI widgets on this page (all use .grid) ---
        self.title_entry = ctk.CTkEntry(self, placeholder_text="Book Title", width=320)
        self.title_entry.grid(row=0, column=0, padx=10, pady=8, sticky="w")

        self.pages_entry = ctk.CTkEntry(self, placeholder_text="Number of Pages", width=320)
        self.pages_entry.grid(row=1, column=0, padx=10, pady=8, sticky="w")

        self.start_entry = ctk.CTkEntry(self, placeholder_text="Start Date (MM/DD/YYYY)", width=320)
        self.start_entry.grid(row=2, column=0, padx=10, pady=8, sticky="w")

        self.status_label = ctk.CTkLabel(self, text="", fg_color="transparent")
        self.status_label.grid(row=3, column=0, padx=10, pady=8, sticky="w")

        self.submit_btn = ctk.CTkButton(self, text="Submit Book", command=self.submit_book)
        self.submit_btn.grid(row=4, column=0, padx=10, pady=10, sticky="w")

    def _parse_date_or_msg(self, date_str: str, field_name: str):
        s = date_str.strip()
        if not s:
            return ""  # allow blank
        try:
            dt = datetime.strptime(s, "%m/%d/%Y")
            return dt.strftime("%m/%d/%Y")
        except ValueError:
            self.status_label.configure(text=f"{field_name} must be MM/DD/YYYY.", text_color="red")
            return None

    def submit_book(self):
        title = self.title_entry.get().strip()
        pages = self.pages_entry.get().strip()
        start = self._parse_date_or_msg(self.start_entry.get(), "Start Date")

        if not title:
            self.status_label.configure(text="Please enter a book title.", text_color="red")
            return
        if start is None:
            return  # invalid date format

        try:
            with db.begin() as conn:
                conn.execute(books.insert().values(
                    title=title,
                    number_of_pages=pages,
                    start_date=start,
                    end_date=""  # not collected on this page yet
                ))
            self.status_label.configure(text=f"Saved: “{title}”", text_color="green")

            # clear fields so placeholders reappear
            self.title_entry.delete(0, "end")
            self.pages_entry.delete(0, "end")
            self.start_entry.delete(0, "end")
        except Exception as e:
            self.status_label.configure(text=f"Error saving book: {e}", text_color="red")
