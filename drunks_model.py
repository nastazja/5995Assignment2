#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file contains the main model for GEOG5995 Assignment 2

Planning for drunks

@author: nastazjalaskowski
"""

# Import all the required packages for the programme

import csv # for reading and writing files
import matplotlib
matplotlib.use('TkAgg') # allows selection of backend needed for graphics to work
import matplotlib.animation # for making animations
import matplotlib.pyplot as plt # for plotting figures
import drunks_framework # for the Drunk class 
import pandas # for exploring the dataframe
import tkinter # builds GUI
from time import perf_counter # to time the code


'''
sys.argv can be used to run the file from command line with custom parameters.
eg. 'drunks_model.py 25 1000' for 25 drunks and 1000 iterations. In which case
the code below would need to be inserted instead of defining the parameters 
within the code:
    
    import sys
    num_of_drunks = int(sys.argv[1])
    num_of_iterations = int(sys.argv[2])
    
The following programme defines the parameters within the code:
    
'''

# Start timing the code

start = perf_counter()

# List all variables that can be altered within the code at the top

num_of_drunks = 25
num_of_iterations = 1000

# Create the main empty lists

town = []
densitymap = []
drunks = []


# SET UP ENVIRONMENT

# Begin by reading in the data for the environment that will act as a town 
# for drunks to wander around when leaving the pub in search of their home

f1 = open('drunk.plan.txt', newline='') # create text file to input data

reader = csv.reader(f1, quoting=csv.QUOTE_NONNUMERIC) # read in town data

for row in reader:				
    rowlist = [] 
    for value in row:		
        rowlist.append(value)
    town.append(rowlist)
f1.close() # close text file

# Visualise data to check if it has been read in

#plt.xlim(0, 300)
#plt.ylim(0, 300)
#plt.title('House Map')
#plt.imshow(town)
#plt.show()

print('town created') # to verify this step was carried out


# SET UP EMPTY DENSITY MAP 

f2 = open('drunk.plan.txt', newline='') # create new text file again

reader = csv.reader(f2, quoting=csv.QUOTE_NONNUMERIC)

for row in reader:				
    rowlist = [] 
    for value in row:		
        rowlist.append(0) # setting the value to 0 creates an empty environment
    densitymap.append(rowlist)
f2.close() # close text file

print('density template created') # to verify this step was carried out


# LOCATE THE PUB & DISPLAY THE TOWN WITH PUB AND HOUSES

# pandas documentation taken from pandas.pydata.org

df = pandas.read_csv('drunk.plan.txt')
pubrow = []
pubcolumn = []
for row in range(df.shape[0]): # reading the file into a dataframe
    for col in range(df.shape[1]):
        if df.iat[row,col] == 1: # finding the 1s representing the pub
            pubrow.append(row) # putting 1s into lists to visualise pub
            pubcolumn.append(col)
            
plt.xlim(0, 300)
plt.ylim(0, 300) 
plt.title('Pub and house locations')  # now both pub and houses are shown         
plt.imshow(town)
plt.scatter(pubrow, pubcolumn)
plt.show()

print('pub located') # to verify this step was carried out


# ESTABLISH START COORDINATES

# enumerate provides another way to search rows and values for 1s 
# (taken from docs.python.org)

for y, row in enumerate(town):
    for x, num in enumerate(row):
        # makes sure the drunks start with x and y coordinates at the pub 
        # by inserting startx and starty into Drunk class
        if num == 1:
            startx = x 
            starty = y

print('starting point set') # to verify this step was carried out


# CREATE THE DRUNKS

for i in range(num_of_drunks):
    # assign home number, use i+1 because i in range(num_of_drunks) is 0 to 24 
    # and house numbers are 10 to 250
    home_num = ((i+1)*10) 
    # use Drunk class from drunks_framework to add drunks into drunks list
    drunks.append(drunks_framework.Drunk(densitymap, drunks, home_num, startx, starty))
    
    
print('agents created') # to verify this step was carried out 


# CREATE ANIMATION AND GUI OF DRUNKS WANDERING AROUND

# Determine variables 

carry_on = True # to keep animation going
counter = 0 # to track number of iterations
fig = plt.figure(figsize=(7, 7)) # sets the y and x axes
ax = fig.add_axes([0, 0, 1, 1])
#ax.set_autoscale_on(False)
    

def update(misc): # to keep animation going
    
    fig.clear()
    global carry_on
    global counter 
    global num_of_iterations
    
    
    for drunk in drunks: 
       if town[drunk.y][drunk.x] == home_num: # if drunk reaches home
           drunks.remove(drunk) # remove from the town
           print('A drunk reached home!') # notify that a drunk reached home
           print(drunk.home_num) # print which home number
       else:
           drunk.move() # else move the drunk using Drunk class
           drunk.density() # add to the densitymap where the drunk is
            
    
    if counter == (num_of_iterations): # if specified number of iterations reached
        carry_on = False # stop drunks wandering around
        print("Iterations finished") # notify that iterations are finished
    else:
        counter +=1 # else keep adding +1 to the counter each iteration
        
    if len(drunks) == 0: # if all the drunks were removed from the town
        carry_on = False # finish the drunks wandering process
        print("All drunks reached home") # notify that they all reached home
        
    plt.xlim(0, 300) # set axes
    plt.ylim(0, 300)
    # clarify what the figure is showing once drunks are overlayed using title
    plt.title('Drunks Wandering') 
    plt.imshow(town)
    plt.scatter(pubrow, pubcolumn)
    
    for i in range(len(drunks)): # each drunk is a red dot on the animation
        plt.scatter(drunks[i].x, drunks[i].y, s=40, c='red', label = 'drunk')
        
def gen(b = [0]): # supplies data to the update function for each frame of the animation
    
    a = 0
    global carry_on
    while (a < 10000000000) & (carry_on) :
           yield a
           a = a + 1

# Uncomment the code directly below if you want animation without GUI and comment
# out GUI code:     
# animation = matplotlib.animation.FuncAnimation(fig, update, interval=10, frames=gen)
# plt.show() 

# MAKING A GUI (code taken from the lectures, creates a pop-up. Sometimes glitchy 
# and creates two pop ups, please remember to press 'Run Model' in the menu). 
      
def run(): # will initiate the animation when Menu -> Run model is clicked.
    animation = matplotlib.animation.FuncAnimation(fig, update, interval=10, frames=gen, repeat=False)
    canvas.draw()

# Build the layers and labels of the GUI and link it to the run method.

root = tkinter.Tk()   
root.wm_title("Model") # title of the GUI pop-up
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu) # click on menu
model_menu.add_command(label="Run model", command=run) # then click on Run model
tkinter.mainloop()

# SAVE DENSITY MAP AS TEXT FILE

with open('densitymap.txt', 'w', newline='') as f3:
    csvwriter = csv.writer(f3, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    # write all the density data stored through the Drunk class and densitymap 
    # list when drunks move
    for row in densitymap: 
        csvwriter.writerow(row)
        

'''
Alternatively, comment out all the code relevant to the animation & GUI, insert 
the code below for a figure of all drunks at their homes and to supply the density 
map text file with the data of where the drunks stepped to get there.



for i in range(num_of_drunks):
    while (town[drunks[i].y][drunks[i].x] != drunks[i].home_num):
        drunks[i].move()
        drunks[i].density()
    print('A drunk reached home!')
    print(drunks[i].home_num)
        
           
plt.xlim(0, 300)
plt.ylim(0, 300)
plt.title('Drunks all home')
plt.imshow(town)
plt.scatter(pubrow, pubcolumn)
    
for i in range(len(drunks)):
    plt.scatter(drunks[i].x, drunks[i].y, s=40, c='red', label = 'drunk')
    
# SAVE DENSITY MAP AS TEXT FILE

with open('densitymap.txt', 'w', newline='') as f3:
    csvwriter = csv.writer(f3, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    # write all the density data stored through the Drunk class and densitymap 
    # list when drunks move
    for row in densitymap: 
        csvwriter.writerow(row)        
'''

# Finish timing the code

end = perf_counter()
print("time = " + str(end - start))        

"""
End of the 'Planning for drunks' model for GEOG5995 Assignment 2
"""
