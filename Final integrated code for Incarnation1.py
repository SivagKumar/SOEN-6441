from pip._vendor.distlib.compat import raw_input
'''
findPIByNilakantaInfiniteSeries

This function finds the PI value using the famous infinite series
called Nilakantha Series. The more the number of series, more accurate
the value is. Here the series depth is 500 to get 10 accurate decimal digits

The series is:
3 + 4/(4*5*6) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) + ...
'''


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


def PI():
    return findPIByNilakantaInfiniteSeries(500)


'''
Converts degrees to radians
radians = (degress/180) * pi
'''
def findRadians(degrees):
    # Find the radians for the number
    return (degrees / 180) * PI()


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

def Sine(radians):
    return taylorSeriesForSine(radians, 80)

'''Function to find the cosine using taylor series

cos(x) = 1 - x^2/2! + x^4/4! - x^6/6! + ...

To get accurate values upto 12 digits, the infinite series is called for 85 times.
'''
def taylorSeriesForCosine(radians, terms):
    # base case
    if terms == 0:
        return 1
    else:
        seriesValue = 1
        value = computePowerOf(radians, terms*2)
        if terms%2 == 0:
            # positive value
            seriesValue = seriesValue * (value / factorialOf(terms*2))
        else:
            # negative value
            seriesValue = seriesValue * -1 * (value / factorialOf(terms*2))
    return seriesValue + taylorSeriesForCosine(radians, terms-1)

'''
Function that calculates the cosine value for alpha/2
'''
def Cosine(degrees):
    #print "the degree is", degrees
    radians = findRadians(degrees)
    return taylorSeriesForCosine(radians, 80)


'''
Function to calculate the aplha value using Bisection method
'''
def alphaValue(iterations):
    lowerLimit=0
    upperLimit=PI()
    baseValue=1
    while(baseValue<iterations):
        midPoint=(lowerLimit+upperLimit)/2
        valueofLowerlimit=lowerLimit-Sine(lowerLimit)-(PI()/2)
        valueofmidPoint=midPoint-Sine(midPoint)-(PI()/2)
        if ((valueofLowerlimit>0 and valueofmidPoint<0) or (valueofLowerlimit<0 and valueofmidPoint>0)):
                upperLimit=midPoint
                baseValue=baseValue+1
        else:
                lowerLimit=midPoint
                baseValue=baseValue+1

    return ((lowerLimit+upperLimit)/2)

def main():
    inputValue = raw_input("Enter the radius of the circle: ")

    try:
        radiusOfCircle = float(inputValue)
        # length of the segment = 2R(1- cos(alpha/2))
        print "The alphavalue is", alphaValue(9)
        alpha = alphaValue(9)
        lengthOfSegment = 2 * radiusOfCircle * (1.0 - Cosine(alpha/2))
        print ("The length of the segment is"), lengthOfSegment
    except ValueError:
        print ("Please enter an integer or float")
    except OverflowError:
        print ("Please enter a smaller value")
    except ZeroDivisionError:
        print ("Division by zero:Please enter another value")

main()