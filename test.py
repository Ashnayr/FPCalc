#--------------------------
# FPCALC v 0.1 DEV Edition
#--------------------------
import sys

MDRE = input("Enter the MDRE: ")
 
NDS = input("Enter the NDS: ")

LTR = input("Enter the LTR: ")

LWR = input("Enter the LWR: ")

#is MDRE > LTR ?
#input MDRE and LTR, calculate. Output SAFE/WARNING

if MDRE >= LTR:
    print "Safe"
else:
    print "Warning"


#is LTR < LWR ?
#input LTR and LWR, calculate. Output SAFE/WARNING

if LTR <= LWR:
    print "Safe"
else:
    print "Warning"

VD = (MDRE / NDS)
print "Each setting increases drag by:", VD
TAD = (VD * NDS)
print "The maximum drag that can be applied is:", TAD



