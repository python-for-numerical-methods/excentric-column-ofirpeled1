import numpy as np
from scipy.optimize import bisect

def find_critical_load(L, E, A, r, c, sigma_allow):

    def f(P):

        angle = (L / (2 * r)) * np.sqrt(P / (E * A))

        sigma_max = (P / A) * (1 + ((c * r) / (r**2)) * (1 / np.cos(angle)))

        return sigma_max - sigma_allow

    P_euler = (np.pi**2 * E * A * r**2) / (L**2)

    return float(bisect(f, 0.01, P_euler * 0.99, xtol=1e-4))
    
