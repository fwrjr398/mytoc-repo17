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
##############################################
################################################
# progress and scale widgit
###############################################

progressbar = ttk.Progressbar(root, orient = HORIZONTAL, length = 200)
progressbar.pack()

#determinate vs indeterminate

progressbar.config(mode = 'indeterminate')
progressbar.start()
progressbar.stop()
# determinate
progressbar.config(mode = 'determinate', maximum = 11.0, value = 4.2)
progressbar.config(value = 8.0)

####### Step function
# increase it by 1
# increase with peremeter

progressbar.step() # increase by 1 step
progressbar.step(5) # beyond the max limit of 11

# update itself from value variable

value = DoubleVar()
progressbar.config(variable = value)

scale = ttk.Scale( root, orient = HORIZONTAL, length = 400, variable = value, from_ = 0.00, to = 11.0)
scale.pack()

# change the value by setting it
scale.set(4.2)
# getthe value
scale.get()

#######################
# setting FRAMES
#######################

# USED FOR ORNANIZE LARGE GUYS
# CONTROL USER WIDGITS


frame = ttk.Frame(root)
frame.pack()
frame.config(height = 100, width = 200)
frame.config(relief =RIDGE)

# ADD WIDGET TO IT

ttk.Button(frame, text = 'CLICK ME!').grid()# frame channges its size to fit the button
frame.config(padding = (30 , 15))
ttk.LabelFrame(root, height = 100, width = 200, text = 'My Frame!').pack()
# for label frame you cannot modify the release property
#
#######################################
# top level widgits

####################################

window = Toplevel(root)
window.tittle('New Window')
window.lower()
window.lift(root)
window.state('zoomed')
window.state('withdrawn') # hidden from users
window.state('iconic')
window.state('normal')

window.iconify() # ssend it down to taskbar
window.deiconify()

# geometry method
#####################################


window.geometry('640*480 +50+100')

# aalowwing user to resize edges of window

window.resize(False, False)

window.maxsize(640, 480) # pixs
window.minsize(200, 200)
window.resizable(True, True)

# close //destroy method  and for all child widgits
################################

root.destroy()
#########################################################

# Panned window >>>>>>

panedwindow = ttk.Panedwindow(root, orient = HORIZONTAL)
panedwindow.pack(fill = BOTH, expand =True)

# create frames for it

frame1 = ttk.Frame(panedwindow, width = 100, height = 300, relief = SUNKEN)
frame2 = ttk.Frame(panedwindow, width = 400, height = 400, relief = SUNKEN)
panedwindow.add(frame1, weight = 1)
panedwindow.add(frame2, weight = 4)


























































