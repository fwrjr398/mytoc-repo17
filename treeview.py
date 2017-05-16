
from tkinter import *
from tkinter import ttk
root = Tk()

treeview = ttk.Treeview(root)
treeview.pack()
treeview.insert('', '0','item1', text = 'First Item')
treeview.insert('', '1','item2', text = 'Second Item')
treeview.insert('', '2','item3', text = 'Third Item')
treeview.insert('', '3','item4', text = 'Fourth Item')
logo = PhotoImage(file="C:\\Users\\rjr398\\Desktop\\ExerciseFiles\\animated-bird-image-0461.gif").subsample(20,20) # size it 
#label.config(image = logo)
treeview.insert('item2', 'end', 'python', text = 'python', image = logo)

treeview.config(height = 5)

# move items
treeview.move('item2', 'item1', 'end')
treeview.item('item1', open = True)
treeview.detach('item3') # deterch but dont delete
treeview.move('item3', 'item2', '0')
# complete delete from view
treeview.delete('item3') # completely deleted & cannot be readded 


#########################################
#adding columns
# create column properties

treeview.config(columns = ('version'))
treeview.column('version', width = 50, anchor = 'center')
treeview.column('# 0', width  = 150)
treeview.heading('version', text = 'Version')
treeview.set('python', 'version', '3.4.1')

#########################
# adding tags
#####################################

treeview.item('python', tags = ('software'))
treeview.tag_configure('software', background = 'yellow')

# ####################################################
# PRINT OUT A LIST OF SELECTED ITEMS
##########################################################
def callback(event):
    print(treeview.selection())

treeview.bind('<<TreeviewSelect>>', callback)



treeview.config(selectmode = 'browse')
treeview.config(selectmode = 'none') # wont show any selected items

treeview.selection_add('python')
treeview.selection_toggle('python') # sellected again

##############################################
# DROP DOWN MENUS
####################################################

# standard menubar
############################################################33
























































