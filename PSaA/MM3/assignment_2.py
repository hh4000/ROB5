from assignment_1 import yield_strength,E_MPa
import numpy as np

#yield strength to account for no permanent deformation
length_mm = 500 
#if max elongation is 1 mm and length is 500 mm, that is 0.002 strain
max_stress = E_MPa*0.002

print("Max stress based on allowed elongation is",max_stress)
print("Max stress is lower than yield strength?")
print(max_stress<=yield_strength)
if max_stress<=yield_strength:
    print("Elongation of 1 mm does not exceed yield strength. Elongation is driving")
else:
    print("Elongation of 1 mm exceeds yield strength. Yield strength is driving")#This is the case
    
max_force = 10000 #N

needed_area = max_force/yield_strength
print("Needed cross section area", needed_area, "mm^2")
needed_diameter = 2*np.sqrt(needed_area/np.pi)
print("Ø",needed_diameter,"mm")