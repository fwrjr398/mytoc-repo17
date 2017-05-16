################MEUS ############
#################################

from tkinter import *
#from tkinter import ttk

root = Tk()
root.option_add('*tearOff', False)# tell the guy to not create bad menus
# must include in all menu codes


menubar = Menu(root)
root.config(menu = menubar)
file = Menu(menubar)
edit = Menu(menubar)
help_ = Menu(menubar)
menubar.add_cascade(menu = file, label = "File")
menubar.add_cascade(menu = edit, label = "Edit")
menubar.add_cascade(menu = file, label = "Help")
#menubar.add_cascade(menu = file, label = "FILE")
file.add_command(label = 'New', command = lambda: print('New File'))

# add seperator
file.add_separator()
file.add_command(label = 'Open...', command = lambda: print('Opening File...'))
file.add_command(label = 'Save...', command = lambda: print('Saving File...'))

######################
# add shortcuts
#########################

file.entryconfig('New', accelerator = 'Ctrl + N')
# ADD IMAGE TO MENU
###################
logo = PhotoImage(file="C:\\Users\\rjr398\\Desktop\\ExerciseFiles\\python2.gif").subsample(10,10) # size it 
#label.config(image = logo)
file.entryconfig('Open...', image = logo, compound = 'left')# added the image to the left of the view
# treeview.insert('item2', 'end', 'python', text = 'python', image = logo)

file.entryconfig('Open..', state = 'disabled')
file.delete('Save') # remove save from the menu

# create newfile child of save menu
save = Menu(file)
file.add_cascade(menu = save, label = 'Save As', command = lambda: print("Saving As..."))
file.add_cascade(menu = save, label = 'Save All', command = lambda: print("Saving All..."))




























