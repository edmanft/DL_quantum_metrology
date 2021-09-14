# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 19:43:56 2020

@author: Manuel
"""





"Imports"
import math
import numpy as np
import scipy 
import matplotlib.pyplot as plt
from random import random
from scipy import linalg
import timeit
from scipy import sparse
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import expm, expm_multiply
import pandas as pd
from numpy import loadtxt
from numpy import savetxt

"""Photodetection register generator

Ground state g is e_1 and excited e is e_2

n_Delta is the number of deltas (detunning) in our interval

n_clicks is how many clicks (photon times) we want per 
photodetection register

n_registers is the number of registers per value of delta"""

sigma=np.matrix('[0 1;0 0]')
sigma_daga=sigma.getH()
n_sigma = sigma_daga*sigma
dt=0.01
n_clicks=200 
n_register=1000 
n_Delta=100 
Delta_vec=np.linspace(1,10,n_Delta)
h_barra=1 #To remind us of the units we chose
Omega=3


deltas_and_clicks_matrix=np.zeros([n_register*n_Delta,n_clicks+1])

phi_matrix=np.matrix(np.zeros((2,1)),dtype=complex) 
Gamma=1. #gamma(rate of photon emission)

evolution_matrix_list=list()
for Delta_iter in range(n_Delta):
    Delta=Delta_vec[Delta_iter]
    "We build the effective Hamiltonian"
    H_A=Delta*sigma_daga*sigma+Omega*(sigma_daga+sigma) 
    J=n_sigma*Gamma/2
    H_eff=H_A-1j*J
    evolution_matrix=linalg.expm(-1j*H_eff*dt)
    evolution_matrix_list.append(evolution_matrix)
    
    
    
    
    
    


for register_iter in range(n_register):
    for Delta_iter in range(n_Delta):

        phi_matrix[0]=1.
        phi_matrix[1]=0.
        Delta=Delta_vec[Delta_iter] 
        
           
          
        population=0
        
        
       
        
        
        
        evolution_matrix=evolution_matrix_list[Delta_iter]
        photon_emmision_time=list() 
 
        
        
        time_integer=0
        

        
        
        
        while len(photon_emmision_time)<n_clicks:
            
            
        
          
          population=np.absolute(phi_matrix[1])**2 
          
          
          

          p_1=Gamma*dt*population
          
          if random()<1-p_1:
            
            aux=evolution_matrix*phi_matrix
            phi_matrix=aux/np.linalg.norm(aux)
            
            
          
        
          else:
            
            phi_matrix[0]=1.
            phi_matrix[1]=0.
            photon_emmision_time.append(time_integer*dt) 
            
          time_integer=time_integer+1 
        deltas_and_clicks_matrix[register_iter*n_Delta+Delta_iter,0]=Delta  
        deltas_and_clicks_matrix[register_iter*n_Delta+Delta_iter,1:]=photon_emmision_time[:]
        
        



clicks=np.asarray(deltas_and_clicks_matrix)





savetxt("archivos_registros/clicks_delta_1_10_omega_3.csv",clicks,delimiter=",")


