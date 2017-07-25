
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

'''
Converts degrees to radians
radians = (degress/180) * pi
'''
def findRadians(degrees):
    # Find the radians for the number
    return (degrees / 180) * findPIByNilakantaInfiniteSeries(500)


'''
Function to find the cosine using taylor series

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
def findCosine(degrees):
    print "the degree is", degrees
    radians = findRadians(degrees)
    return taylorSeriesForCosine(radians, 85)
