#--------------------------
# FPCALC v 0.2 DEV Edition
#--------------------------
import sys

MaxDragReel = input("What is the Drag Rating of your selected reel: ")
 
NumDragSettings = input("Does the Reel support 6, 8, or 12 Drag Settings?:")

LineTestRating = input("What is the Test Rating of your line: ")

RodLineWeightRating = input("What is the Line Rating of your rod?: ")

#The maximum drag of the reel should be higher than the test (maximum sustainable load) of the line. 
#input MDRE and LTR, calculate. Output SAFE/WARNING

if MaxDragReel >= LineTestRating:
    print "Your Reel and Line combo is matched appropriately"
else:
    print "Warning! The Drag Rating of your Reel is lower than the Line Test Rating"

#The test of the line should be lower than the maximum line weight of the rod.
#input LTR and LWR, calculate. Output SAFE/WARNING

if LineTestRating <= RodLineWeightRating:
    print "Your selected Line is matched to your Rod appropriately"
else:
    print "Warning your Line is not matched to your rod"

#Divide the maximum drag of the reel by the number of drag settings the reel has. 
#This will tell you how much the reel will increase/decrease drag by every time you raise/lower the drag setting. 
DragValue = (MaxDragReel / NumDragSettings)
print "Each setting increases drag by:", DragValue

MaxAppliedDrag = (DragValue * NumDragSettings)
print "The maximum drag that can be applied is:", MaxAppliedDrag


#Multiply this number by the number of the drag setting you wish to use. 

UserDrag = input("What level is drag set to?: ")
AppliedDrag = (DragValue * UserDrag)
print "Applied Drag totals", AppliedDrag

if AppliedDrag > LineTestRating:
    print "You have too much Drag applied, you risk breaking the line"
else:
    print "Your current Drag setting is within safe operating limits"









