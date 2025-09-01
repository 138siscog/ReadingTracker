## This the first large project i am working on, this is going to be a reading tracket you will be able to type in the books you are reading the page count, select start and end date you will be able to see stats of how many days you read or how many books you have read in a year / month ect Still in super early stages. 

## I am learnign how to use Customer tkinter to build this app and will implement SQL for database use and matplot lib to plot out stats

## Librarys used so far CustomerTkinter, tkinter, PIL, ctypes

from add_book import AddBookPage, db, metadata
from settings import SettingsPage
from stats import StatsPage
from load_book import LoadBookPage
from tkinter import *
import customtkinter as ctk
from ctypes import windll
from PIL import Image
import pandas as pd

## Updates
## > Database features iplemented - now when you input the informatoin in the entry fields and click add it gets added to the database

## To Do List
## > Add Calendar to select date when adding a new book or leaving as is, it will auto sync with current date
## > Show list of books you are reading with stats like what page are you on % complete ect. 
## > Using the info from the load book page i want to generate charts using tkinter to keep track of reading progress
## > Ability to delete books from list 
## > Ability to show list and edit book entries on load book page


## This is still very early in development and im doing a lot of learning as im going 

