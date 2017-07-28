from pip._vendor.distlib.compat import raw_input
import math
import xml.etree.ElementTree as ET  # For creating XML
import ctypes
import pdb  # For debugging


'''
Function to calculate the alpha value using Bisection method
No.of iterations>logbase2((lowerLimit-upperLimt)/error tolerance level)
'''


def alpha_value(iterations):

    # LowerLimit and upperLimit values are based on assumptions.
    lowerLimit = 0
    upperLimit = math.pi
    baseValue = 1

    while(baseValue < iterations):
        midPoint = (lowerLimit+upperLimit)/2

        # f(x)=x-sin(x)-pi/2
        valueofLowerlimit = lowerLimit-math.sin(lowerLimit)-(math.pi/2)
        valueofmidPoint = midPoint-math.sin(midPoint)-(math.pi/2)

        # Onelimit should be in positive range and other in negative range.
        if ((valueofLowerlimit > 0 and valueofmidPoint < 0)or
           (valueofLowerlimit < 0 and valueofmidPoint > 0)):

                upperLimit = midPoint  # Manipulating limits for next iteration
                baseValue = baseValue+1
        else:

                lowerLimit = midPoint  # Manipulating limits for next iteration
                baseValue = baseValue+1

    return ((lowerLimit+upperLimit)/2)

'''
Function to calculate the length of the segment X1X2
'''


def length_of_segment(radiusOfCircle):
    # Calculating alpha value in terms of radians
    alpha = math.radians(alpha_value(35))
    print (" The alphavalue is"), alpha_value(35)
    # length of the segment = 2R(1- cos(alpha/2)).
    lengthOfSegment = 2 * radiusOfCircle * (1.0 - math.cos(alpha/2))

    return lengthOfSegment


def main():

    # Accepting user input.
    inputValue = raw_input("Enter the radius of the circle: ")

    try:
        radiusOfCircle = float(inputValue)
        pdb.set_trace()  # Set trace point
        length = length_of_segment(radiusOfCircle)

        # Creating XML.
        root = ET.Element('Output')
        root.text = str(length)
        ET.dump(root)
        tree = ET.ElementTree(root)
        tree.write('Output.xml')  # Writing to an XML file

        tree = ET.parse('Output.xml')  # Reading from an XML file
        root = tree.getroot()

        # GUI to print length of the segment.
        return ctypes.windll.user32.MessageBoxA(None,
                                                root.text,
                                                "Length of the segment", 0)
    # Handling exceptions.
    except ValueError:
        print ("Please enter an integer or float")
    except OverflowError:
        print ("Please enter a smaller value")
    except ZeroDivisionError:
        print ("Division by zero:Please enter another value")

main()
