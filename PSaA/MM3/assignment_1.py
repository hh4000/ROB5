import numpy as np
import matplotlib.pyplot as plt

len_mm  = np.array([75.0,75.025,75.05,75.075,75.113,75.15,75.225,75.375,75.525,75.75,76.5,78.0,79.5,81.0,82.5,84.0,85.5,87.0,88.725])
force_N = np.array([0,4740,9140,12920,16540,18300,20170,22900,25070,26800,28640,30240,31100,31280,30820,29180,27190,24140,18970])

area_mm2=8.5*8.5
stress_MPa = force_N/area_mm2#N/mm2


len_0=len_mm[0]
strain = (len_mm-len_0)/len_0
def estimate_coef(x, y):
    # number of observations/points
    n = np.size(x)
 
    # mean of x and y vector
    m_x = np.mean(x)
    m_y = np.mean(y)
 
    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x
 
    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x
 
    return (b_0, b_1)





_,E_MPa = estimate_coef(strain[0:3],stress_MPa[0:3])


yield_strength = 289

UTS = max(stress_MPa)




if __name__=="__main__":
    plt.plot(strain,stress_MPa)
    plt.plot([0.002,0.002+300/E_MPa],[0,300])
    plt.show()

    print("E",E_MPa,"MPa")
    print("yield strength",yield_strength,"MPa")
    print("Ultimate Tensile Strength",UTS,"MPa")