
# this is tkinter training script

from tkinter import *
from tkinter import ttk

root = Tk()
checkbutton = ttk.Checkbutton(root, text = 'SPAM')
checkbutton.pack()
 
spam = StringVar()
spam.set('SPAM!')
spam.get()

checkbutton.config(variable = spam, onvalue = 'SPAM Please!', offvalue = 'Boo Spam')

breakfast = StringVar()
ttk.Radiobutton(root, text = 'SPAM', variable = breakfast, value = "SPAM").pack()
ttk.Radiobutton(root, text = 'EGGS', variable = breakfast, value = "EGGS").pack()
ttk.Radiobutton(root, text = 'MEAT', variable = breakfast, value = "MEAT").pack()
ttk.Radiobutton(root, text = 'TEA', variable = breakfast, value = "TEA").pack()

entry = ttk.Entry(root, width = 30) # controls size of gui
entry.pack()
entry.get()

#########################################
############SPINE BOX ---------
#################################@#

month =StringVar()
combobox = ttk.Combobox(root, textvariable = month)
combobox.pack()

combobox.config(values =('Jan', 'Feb', 'Mar', 'Apr', 'May','June', 'July', 'Aug', 'Sep', 'Oct', 'Nov','Dec'))

#spinbox
year = StringVar()
Spinbox(root, from_ = 1990, to = 2014, textvariable = year).pack()


##############
# progress bar widgit
# progress bar
##############################


progressbar = ttk.Progressbar(root, orient = HORIZONTAL, length = 200) 
progressbar.pack()

# determining time
# inditiminate


