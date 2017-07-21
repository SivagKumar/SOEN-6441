'''
findPIByNilakantaInfiniteSeries

This function finds the PI value using the famous infinite series
called Nilakantha Series. The more the number of series, more accurate
the value is. Here the series depth is 500 to get 10 accurate decimal digits

The series is:
3 + 4/(4*5*6) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) + ...
'''
from pip._vendor.distlib.compat import raw_input
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


def main():

    inputValue = raw_input("Enter the degree to be converted to radians: ")
    radianofvalue=float(inputValue)
    radianValue=findRadians(radianofvalue)
    print ("The value of pi is"), findPIByNilakantaInfiniteSeries(500)
    print ("The value of radians is"), radianValue

main()