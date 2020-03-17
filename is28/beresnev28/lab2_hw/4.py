import math 
andle=float(input("andle="))
rad=andle/(180/math.pi)
rad_s="%.1f" % math.sin(rad)
rad_c="%.1f" % math.cos(rad)
print("sin=%s cos=%s" % (rad_s,rad_c))