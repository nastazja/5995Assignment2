#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 15:58:34 2020

@author: nastazjalaskowski
"""

# Import all the required packages first

import random

# Define the Drunk class and its attributes, so that it becomes possible to create
# functions for the drunks behaviours (move and add density)

class Drunk:
    # __init__ is the constructor 
    def __init__(self, densitymap, drunks, home_num, startx, starty):
        self.densitymap = densitymap # feeds in the densitymap
        self.drunks = drunks # feeds in awareness of drunks
        self.home_num = home_num # feeds in the house numbers
        self.x = startx # sets starting x at pub
        self.y = starty # sets starting y at pub
        
        
     # move function will make the drunks take 5 steps each iteration as they search for their home
    def move(self):
        
        if random.random() < 0.5: # direction of movement of the drunks is randomly generated
            self.x = (self.x + 5) % 300 # % 300 is the Torus boundary solution so drunks don't fall off the graph
        else:
            self.x = (self.x - 5) % 300
                
        if random.random() < 0.5:
            self.y = (self.y + 5) % 300
        else:
            self.y = (self.y - 5) % 300
            
     # density function will add 1 point of density to densitymap wherever the drunks step          
    def density(self): 
        self.densitymap[self.x][self.y] += 1
        
        
        