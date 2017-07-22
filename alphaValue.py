#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Siva Kumar
#
# Created:     21-07-2017
# Copyright:   (c) Siva Kumar 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/python
import math

def alphaValue(iterations):
    lowerLimit=0
    upperLimit=math.pi
    iterations=1
    while(iterations<9):
        midPoint=(lowerLimit+upperLimit)/2
        valueofLowerlimit=lowerLimit-math.sin(lowerLimit)-(math.pi/2)
        valueofmidPoint=midPoint-math.sin(midPoint)-(math.pi/2)
        if ((valueofLowerlimit>0 and valueofmidPoint<0) or (valueofLowerlimit<0 and valueofmidPoint>0)):
                upperLimit=midPoint
                print lowerLimit
                print upperLimit
                iterations=iterations+1
        else:
                lowerLimit=midPoint
                print lowerLimit
                print upperLimit
                iterations=iterations+1

    return ((lowerLimit+upperLimit)/2)









