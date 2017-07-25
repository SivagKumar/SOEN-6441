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
def findPIByNilakantaInfiniteSeries(terms):
    # base case
    if terms == 0:
        return 3
    else:
        seriesValue = 1
        value = 4.0 / ((terms * 2) * ((terms * 2) + 1) * ((terms * 2) + 2))
        if terms % 2 == 0:
            # negative value
            seriesValue = seriesValue * -1 * value
        else:
            # positive value
            seriesValue = seriesValue * value
        return seriesValue + findPIByNilakantaInfiniteSeries(terms - 1)

'''
Find the power of X

E.g: x^4 = x*x*x*x
'''
def computePowerOf(radians, terms):
    # base case
    if terms == 0:
        return 1
    else:
        return radians * computePowerOf(radians, terms-1)

'''
Find the factorial of X

E.g: 5! = 5*4*3*2*1
'''
def factorialOf(number):
    # base case
    if number == 1 or number == 0:
        return 1
    else:
        return number * factorialOf(number-1)



'''
Function to find the sine using taylor series

sin(x) = x- x^3/3! + x^5/5! - x^7/7! + ...


To get accurate values upto 12 digits, the infinite series is called for 85 times.
'''
def taylorSeriesForSine(radians, terms):
    # base case
    if terms == 0:
        return radians
    else:
        seriesValue = 1.0
        value = computePowerOf(radians, ((2*terms)+1))
        if terms%2 == 0:
            # positive value
            seriesValue = seriesValue * (value / factorialOf((2*terms)+1))
        else:
            # negative value
            factorial=factorialOf((2*terms)+1)
            float(factorial)
            value=value/factorial
            seriesValue = seriesValue * -1 * value
    return seriesValue + taylorSeriesForSine(radians, terms-1)

'''def findSine(degrees):
    print "the degree is", degrees
    radians = findRadians(degrees)
    return taylorSeriesForSine(radians, 85)'''


def alphaValue(iterations):
    lowerLimit=0
    upperLimit=findPIByNilakantaInfiniteSeries(500)
    iterations=1
    while(iterations<9):
        midPoint=(lowerLimit+upperLimit)/2
        valueofLowerlimit=lowerLimit-taylorSeriesForSine(lowerLimit,80)-(findPIByNilakantaInfiniteSeries(500)/2)
        valueofmidPoint=midPoint-taylorSeriesForSine(midPoint,80)-(findPIByNilakantaInfiniteSeries(500)/2)
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

def main():

     sineValue=taylorSeriesForSine((findPIByNilakantaInfiniteSeries(500)/2),80)
     print "The sine Value is", sineValue
     alpha=alphaValue(9)
     print "The alpha Value is", alpha

main()







