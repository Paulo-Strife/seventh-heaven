import math

def cilindricas_para_cartesianas(rho, theta, z):
    x = rho * math.cos(theta)
    y = rho * math.sin(theta)
    return x, y, z