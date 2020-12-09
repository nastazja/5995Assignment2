# 5995Assignment2

## Welcome to Nastazja's repository for the 5995 assignment 2 independent project. 

**Nastazja had no coding experience prior to this course. Skills for these assignments were learnt from a 1-week intensive course, several readings of learning 
materials and a few run-throughs of the practicals. This repository contains a project build-up chosen from the list of suggested ideas, it is 'Planning for drunks'.**

## Description

There is a group of 25 drunks at an initial set of coordinates which represent the pub. The drunks leave one-by-one, when one drunk leaves the pub s/he wanders 
around randomly until s/he finds their own home and then the next drunk leaves the pub in search of their own home. They move freely within the boundaries of the 
environment, provided as drunk.plan.txt, and they can only enter their own home as assigned to them in the pub.

## Assignment criteria

1. Pull in the data file and finds out the pub point and the home points.
2. Draws the pub and homes on the screen.
3. Models the drunks leaving their pub and reaching their homes, and stores how many drunks pass through each point on the map.
4. Draws the density of drunks passing through each point on a map.
5. Saves the density map to a file as text.

## Details 

The model is composed of the core script in *drunks_model.py* and the *drunks_framework.py* containing the Class for the drunks. The environment is read in from 
*drunk.plan.txt* where the pub is denoted by 1s, the houses by numbers 10-250 and empty space by 0s. A density map of drunks passing through each point is created 
as an **output** called *density_map.txt*. A UML is also found in this repository showing the code structure. summary.txt details the intention of the software, issues during development and how these were overcome, general sources used, the thought processes going into the software design, and the software development process followed. 

## License 

MIT license, details in LICENSE.md
