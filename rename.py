# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 15:40:08 2016

@author: sondes
"""

import os,sys
folder = "/home/sondes/project/FAstpssm_jackhmmer"
for filename in os.listdir(folder):
       infilename = os.path.join(folder,filename)
       if not os.path.isfile(infilename): continue
       oldbase = os.path.splitext(filename)
       newname = infilename.replace('.', '.')
       output = os.rename(infilename, newname)    
