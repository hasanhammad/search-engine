# Importing the necessary libraries
import tkinter as tk
from tkinter import *
from search_algo import *
import webbrowser

# to store the matched pages
matched = []

# if an item selected
def on_click(event):

    widget = event.widget

    # get the item which was selected
    if widget.curselection():
        selection = widget.curselection()
        # get the value of that item
        value = widget.get(selection[0])
        # open the link in default browser
        webbrowser.open_new(value[2:])



# if the "Search" button is pressed
def getQuery(searchBox, win):
    global matched
    # get the query
    query = searchBox.get()
    # print the query
    print(query)
    # get the matched files
    matched = search_al(query)
    # print the matched files
    drawMatched(win)


# to draw the main window
def drawMainWindow(win):
    # draw a search box
    searchBox = Entry(win, bd=2, width=60)
    # draw a button
    searchButton = tk.Button(win, text="Search",width = 15,height = 2, command=lambda: getQuery(searchBox, win))
    # place the button in position
    searchButton.place(x=600, y=15)
    # draw the name of the program
    nameLable = Label(win, text="SEARCHY", font=("Lucida Handwriting", 22))
    # place it in position
    nameLable.place(x=10, y=15)
    return searchBox


# draw the matched pages
def drawMatched(win):
    # make a new frame
    home_page = tk.Frame(win, width=746, height=420)
    # place the frame in position
    home_page.place(x=0, y=80)
    # creating a Listbox and
    # attaching it to the frame
    listbox = Listbox(home_page, width=74, height=16, font=("Segoe UI", 14), fg="blue")

    # adding Listbox to the left
    # side of the frame
    listbox.pack(side=LEFT, fill=BOTH)

    # creating a Scrollbar and
    # attaching it to the frame
    scrollbar = Scrollbar(home_page)
    # adding Scrollbar to the right
    # side of the frame
    scrollbar.pack(side=RIGHT, fill=BOTH)
    # insert elements into the listbox

    for page in matched:
        page = "• " + page
        listbox.insert(END, page)
        listbox.bind("<<ListboxSelect>>", on_click)

    # attaching Listbox to Scrollbar
    # since we need to have a vertical
    # scroll we use yscrollcommand
    listbox.config(yscrollcommand=scrollbar.set)
    # setting scrollbar command parameter
    # to listbox.yview method its yview because
    # we need to have a vertical view
    scrollbar.config(command=listbox.yview)
