

from pip._vendor.distlib.compat import raw_input
import math
import xml.etree.ElementTree as ET
import ctypes

'''
Function to calculate the aplha value using Bisection method
'''
def alphaValue(iterations):
    lowerLimit=0
    upperLimit=math.pi
    baseValue=1
    while(baseValue<iterations):
        midPoint=(lowerLimit+upperLimit)/2
        valueofLowerlimit=lowerLimit-math.sin(lowerLimit)-(math.pi/2)
        valueofmidPoint=midPoint-math.sin(midPoint)-(math.pi/2)
        if ((valueofLowerlimit>0 and valueofmidPoint<0) or (valueofLowerlimit<0 and valueofmidPoint>0)):
                upperLimit=midPoint
                baseValue=baseValue+1
        else:
                lowerLimit=midPoint
                baseValue=baseValue+1

    return ((lowerLimit+upperLimit)/2)

'''
Function to calculate the length of the segment X1X2
'''

def lengthOfSegment(radiusOfCircle):
      alpha = math.radians(alphaValue(9))
      # length of the segment = 2R(1- cos(alpha/2))
      lengthOfSegment = 2 * radiusOfCircle * (1.0 - math.cos(alpha/2))

      return lengthOfSegment

def main():
    inputValue = raw_input("Enter the radius of the circle: ")

    try:
        radiusOfCircle = float(inputValue)
        length=lengthOfSegment(radiusOfCircle)
        root = ET.Element('Output')
        root.text = str(length)
        ET.dump(root)
        tree= ET.ElementTree(root)
        tree.write('Output.xml')
        #print ("The length of the segment is"), length

        tree = ET.parse('Output.xml')
        root = tree.getroot()
        return ctypes.windll.user32.MessageBoxA(None, root.text, "Length of the segment", 0)


    except ValueError:
        print ("Please enter an integer or float")
    except OverflowError:
        print ("Please enter a smaller value")
    except ZeroDivisionError:
        print ("Division by zero:Please enter another value")

main()