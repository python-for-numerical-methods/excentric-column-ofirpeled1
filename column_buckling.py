import numpy as np
from scipy.optimize import bisect

def find_critical_load(L, E, A, r, c, sigma_allow):
    def f(P):
        # מומנט משוער עקב אי-מרכוז
        M = P * c
        
        # מאמץ כולל
        sigma = P / A + (M * r) / (A * r**2)
        
        return sigma - sigma_allow

    # עומס אוילר
    P_euler = (np.pi**2 * E * A * r**2) / (L**2)

    return float(bisect(f, 0.01, P_euler * 0.99, xtol=1e-4))
    
