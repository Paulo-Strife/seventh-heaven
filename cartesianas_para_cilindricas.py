import math

def cartesianas_para_cilindricas(x, y, z):

    p = math.sqrt(x**2 + y**2)
    teta = math.atan2(x, y)

    if z > 1:
        z_eh_positivo =  True
    else:
        z_eh_positivo = False

    return (p, teta, z)