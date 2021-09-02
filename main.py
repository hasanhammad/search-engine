from crawler import *
from GUI import *


# https://aparat.com/v/XY0p1 #######


# call crawl function
crawl()
win = tk.Tk()   # make a main window and let's call it (win)
win.title('SEARCHY')  # add a title to the main window
win.minsize(700, 500)  # set the size of the main window

# function that gets called whenever
#the search box is clicked
def on_entry_click(event):
    global searchBox
    if searchBox.get() == 'Enter your boolean query...':
        # delete all the text in the entry
        searchBox.delete(0, "end")
        # insert blank for user input
        searchBox.insert(0, '')
        # set the color of the text
        searchBox.config(fg='black')

# function that gets called whenever
# another element is clicked
def on_focusout(event):
    global searchBox
    if searchBox.get() == '':
        # print text in to the search box
        searchBox.insert(0, 'Enter your boolean query...')
        # set the color of the text
        searchBox.config(fg='grey')


# draw the main window
searchBox = drawMainWindow(win)
# print a text inside the search box
searchBox.insert(0, 'Enter your boolean query...')
# what to do if the search box is clicked
# if the search box is clicked ==> remove the text
searchBox.bind('<FocusIn>', on_entry_click)
# if the search box is not clicked ==> print the text
searchBox.bind('<FocusOut>', on_focusout)
# set the color of the text
searchBox.config(fg='grey')
# place the search boc in position
searchBox.grid(row=0, column=2, padx=190, pady=16, ipady=10)
# to keep the main window open
win.mainloop()
