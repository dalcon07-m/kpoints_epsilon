#!/usr/bin/env python
# coding: utf-8

#########################################################################################
##############                                                        ###################
##############  Program to generate kpoints and  weights for scf to   ###################
##############                  epsilon.x evaluation                  ###################
##############                                                        ###################
#########################################################################################

import math
import re
import pandas as pd
import numpy as np
import csv


#########################################################
#############   input ###################################
#########################################################

kx=8 #kpoints
ky=8
kz=8

########################################################
########################################################


tk=kx*ky*kz #total kpoints
w=round(1/(tk),5) #weight


kps=[]

for x in range(kx):
    for y in range(ky):
        for z in range(kz):
            px=round(x/kx,5)
            py=round(y/ky,5)
            pz=round(z/kz,5)
            kps.append([px,py,pz,w])
print('kpoints=', 'kx:',kx,'ky:', ky,'kz:', kz, ', tot kpoints=',tk, ', weight=', w, ':' )

with open('k_points.dat', 'w') as archivo:
    for kp in zip(kps):
        print(kp[0][0], kp[0][1], kp[0][2],kp[0][3], file=archivo) # print the kpoints with the weight for epsilon.x


