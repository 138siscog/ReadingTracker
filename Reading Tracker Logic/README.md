## Reading Tracker (Logic)

- This project provides the core logic for a Reading Tracker application. It is designed to track   books read, log reading sessions, and calculate the time spent reading.

- Note: This repository only contains the logic portion. The GUI for the tracker is being developed in a separate file and will be integrated later into a complete application.

## Features

- Add new reading sessions

* Input date, book title, start time, and end time.

* Automatically calculates total reading time (including handling overnight sessions).

- Persistent storage

* Data is saved to a CSV file (database.csv) that keeps a running history of all logged reading sessions.

- Time calculation

* Converts entered times into datetime format.

* Computes the difference between start and end times in HH:MM format.

- Data visualization (Jupyter Notebook)

* A companion notebook (ReadingTracker.ipynb) includes logic for plotting your data.

* Provides scatter and bar charts of reading time by date, with formatted axes for clarity.

## Files

- main.py → The core logic for reading session input and CSV management

- database.csv → Stores reading history in tabular format (Date, Book Title, Start, End, Total Time).

- ReadingTracker.ipynb → Notebook with data analysis and visualization logic (plots, formatting, exploration).

## How It Works

- Run main.py.

## Enter:

- Date (MM/DD/YYYY or similar format)

- Book title

- Start time (HH:MM AM/PM)

- End time (HH:MM AM/PM)

## The script calculates total reading time and appends a new row to database.csv.

## Use ReadingTracker.ipynb to visualize your reading habits over time.

## Next Steps

- Merge with GUI → The logic here will be integrated with a user-friendly interface.

- Expand functionality → Possible additions:

* Tracking pages read or percentage complete.

* Exporting summaries/reports.

* Daily/weekly reading goals.