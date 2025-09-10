import math as mt

def cartesianas_para_esfericas(x, y, z):
    r = mt.sqrt(x**2 + y**2 + z**2)
    θ = mt.atan2(y, x)
    φ = mt.acos(z/r)

    return r, θ, φ