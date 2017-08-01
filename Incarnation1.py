from pip._vendor.distlib.compat import raw_input


'''
findPIByNilakantaInfiniteSeries

This function finds the pi value using the famous infinite series
called Nilakantha Series. The more the number of series, more accurate
the value is. Here the series depth is 500 to get 10 accurate decimal digits

The series is:
3 + 4/(4*5*6) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) + ...
'''


def find_pi_nilakanta_infinite_series(terms):
    # Base case
    if terms == 0:
        return 3
    else:
        seriesValue = 1
        value = 4.0 / ((terms * 2) * ((terms * 2) + 1) * ((terms * 2) + 2))
        if terms % 2 == 0:
            # Negative value
            seriesValue = seriesValue * -1 * value
        else:
            # Positive value
            seriesValue = seriesValue * value

        # Recursive function
        return seriesValue + find_pi_nilakanta_infinite_series(terms - 1)

'''
Function that returns the pi value
'''


def pi():
    return find_pi_nilakanta_infinite_series(500)


'''
Converts degrees to radians
radians = (degress/180) * pi
'''


def find_radians(degrees):
    # Find the radians for the degrees.
    return (degrees / 180) * pi()


'''
Find the power of X
E.g: x^4 = x*x*x*x
'''


def compute_power_of(radians, terms):
    # base case
    if terms == 0:
        return 1
    else:
        # Recursive function
        return radians * compute_power_of(radians, terms-1)


'''
Find the factorial of X

E.g: 5! = 5*4*3*2*1
'''


def factorial_of(number):
    # base case
    if number == 1 or number == 0:
        return 1
    else:
        # Recursive function
        return number * factorial_of(number-1)


'''
Function to find the sin using taylor series

sin(x) = x- x^3/3! + x^5/5! - x^7/7! + ...
To get accurate values up to 12 digits, the infinite series is called
for 80 times.
'''


def taylor_series_sine(radians, terms):
    # base case
    if terms == 0:
        return radians
    else:
        seriesValue = 1.0
        value = compute_power_of(radians, ((2*terms)+1))
        if terms % 2 == 0:
            # positive value
            seriesValue = seriesValue * (value / factorial_of((2*terms)+1))
        else:
            # negative value
            seriesValue = seriesValue * -1 * (value /
                                              factorial_of((2*terms)+1))

    # Recursive function
    return seriesValue + taylor_series_sine(radians, terms-1)

'''
Function that calculates the sine value in alpha function
'''


def sine(radians):
    return taylor_series_sine(radians, 80)


'''Function to find the cosine using taylor series

cos(x) = 1 - x^2/2! + x^4/4! - x^6/6! + ...

To get accurate values up to 12 digits, the infinite series is called for
80 times.
'''


def taylor_series_cosine(radians, terms):
    # base case
    if terms == 0:
        return 1
    else:
        seriesValue = 1
        value = compute_power_of(radians, terms*2)
        if terms % 2 == 0:
            # positive value
            seriesValue = seriesValue * (value / factorial_of(terms*2))
        else:
            # negative value
            seriesValue = seriesValue * -1 * (value / factorial_of(terms*2))
    return seriesValue + taylor_series_cosine(radians, terms-1)

'''
Function that calculates the cosine value for alpha/2
'''


def cosine(degrees):

    radians = find_radians(degrees)
    return taylor_series_cosine(radians, 80)


'''
Function to calculate the alpha value using Bisection method
No.of iterations>logbase2((lowerLimit-upperLimt)/error tolerance level)
'''


def alpha_value(iterations):

    # LowerLimit and upperLimit values are based on assumptions.
    lowerLimit = 0
    upperLimit = pi()
    baseValue = 1

    while(baseValue < iterations):
        midPoint = (lowerLimit+upperLimit)/2

        # f(x)=x-sin(x)-pi/2
        valueofLowerlimit = lowerLimit-sine(lowerLimit) - (pi()/2)
        valueofmidPoint = midPoint-sine(midPoint) - (pi()/2)

        # Onelimit should be in positive range and other in negative range.
        if ((valueofLowerlimit > 0 and valueofmidPoint < 0)or
           (valueofLowerlimit < 0 and valueofmidPoint > 0)):

                upperLimit = midPoint  # Manipulating limits for next iteration
                baseValue = baseValue+1
        else:
                lowerLimit = midPoint  # Manipulating limits for next iteration
                baseValue = baseValue+1

    return ((lowerLimit+upperLimit)/2)


def main():

    # Accepting user input.
    inputValue = raw_input("Enter the radius of the circle: ")

    try:
        radiusOfCircle = float(inputValue)

        # Call alpha function
        alpha = alpha_value(35)
        print ("The alphavalue is"), alpha
        print ("cos(alpha/2) value is"), cosine(alpha/2)
        # length of the segment = 2R(1- cos(alpha/2))
        lengthOfSegment = 2 * radiusOfCircle * (1.0 - cosine(alpha/2))
        print ("The length of the segment is"), lengthOfSegment

    # Handling exceptions.
    except ValueError:
        print ("Please enter an integer or float")
    except OverflowError:
        print ("Please enter a smaller value")
    except ZeroDivisionError:
        print ("Division by zero:Please enter another value")

main()
