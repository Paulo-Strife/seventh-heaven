import math

def esfericas_para_cilindricas(r, theta, phi):
    rho = r * math.sin(phi)
    z = r * math.cos(phi)
    return rho, theta, z