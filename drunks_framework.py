#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file defines the class Drunk for the GEOG5995 Assignment 2

Planning for drunks

@author: nastazjalaskowski
"""

# Import all the required packages first

import random

# Define the Drunk class and its attributes, so that it becomes possible to 
# create functions for the drunks behaviours (move and density).


'''
The parent class used to represent a Drunk.

...
    
Attributes are described in the constructor method.

Methods
-------
1. constructor
2. move
3. density
   
Methods are defined within themselves.
'''

class Drunk:
    def __init__(self, densitymap, drunks, home_num, startx, starty):
        '''
         Parameters
         ----------
         densitymap : list
             The list for recording density data about where drunks have stepped
         drunks : list
             The list containing 25 drunks
         home_num : int
             The home number assigned to the drunks in the pub
         x:
             Set the initial x coordinate in the pub
         y:
             Set the initial y coordinate in the pub
        '''
        
        self.densitymap = densitymap # feeds in the densitymap
        self.drunks = drunks # feeds in the drunks list
        self.home_num = home_num # feeds in the house numbers
        self.x = startx # sets starting x at pub
        self.y = starty # sets starting y at pub
        
        
    def move(self):
        '''
        The move method will make drunks take a step of 5 with each iteration
        (until the model discovers that the drunk has found their home). The 
        direction of movement of the drunks is randomly generated.
        % 300 is the Torus boundary solution so drunks don't fall off the graph.
        '''
        
        if random.random() < 0.5: 
            self.x = (self.x + 5) % 300
        else:
            self.x = (self.x - 5) % 300
                
        if random.random() < 0.5:
            self.y = (self.y + 5) % 300
        else:
            self.y = (self.y - 5) % 300
            
          
    def density(self): 
        '''
        The density function will add 1 point of density to densitymap wherever 
        the drunks step
        '''
        self.densitymap[self.x][self.y] += 1
        
        
        