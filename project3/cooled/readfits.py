# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 08:32:22 2016

@author: rwatkins
"""
# This program illustrates how to open and read fits files using Python

from astropy.io import fits
import numpy as np

biaslist=[]      
for i in range(1,10):
    hdulist = fits.open('Bias-'+str(i)+'.fit') #this opens the set of 9 Bias files using the index i to put the number in the filename
    biasframe = hdulist[0].data
    biaslist.append(biasframe)
    hdulist.close()
    
print(np.shape(biaslist)) #biaslist is now a list of the 9 frames, with each frame being a 2D array of pixel values

#to open a single file

hdulist = fits.open('Dark-10s.fit')
dark10 = hdulist[0].data
hdulist.close()
# dark10 is now a 2D array of pixel values


