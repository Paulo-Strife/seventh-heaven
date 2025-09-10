import math as mt

def cilindricas_para_esféricas(p, teta, z):
    r = mt.sqrt(p**2 + z**2)
    phi = mt.atan2(p, z)
    return r, teta, phi