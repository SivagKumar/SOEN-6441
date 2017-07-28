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
FUNCTION findPIByNilakantaInfiniteSeries(terms):
    # base case
    IF terms = 0:
        RETURN 3
    ELSE:
        seriesValue <- 1
        value <- 4.0 / ((terms * 2) * ((terms * 2) + 1) * ((terms * 2) + 2))
        IF terms % 2 = 0:
            # negative value
            seriesValue <- seriesValue * -1 * value
        ELSE:
            # positive value
            seriesValue <- seriesValue * value
        ENDIF
        RETURN seriesValue + findPIByNilakantaInfiniteSeries(terms - 1)
    ENDIF
ENDFUNCTION

'''
Find the power of X
E.g: x^4 <- x*x*x*x
'''
FUNCTION computePowerOf(radians, terms):
    # base case
    IF terms = 0:
        RETURN 1
    ELSE:
        RETURN radians * computePowerOf(radians, terms-1)
    ENDIF
ENDFUNCTION

'''
Find the factorial of X
E.g: 5! <- 5*4*3*2*1
'''
FUNCTION factorialOf(number):
    # base case
    IF number = 1 OR number = 0:
        RETURN 1
    ELSE:
        RETURN number * factorialOf(number-1)
    ENDIF
ENDFUNCTION

'''
Function to find the sine using taylor series
sin(x) <- x- x^3/3! + x^5/5! - x^7/7! + ...
To get accurate values upto 12 digits, the infinite series is called for 85 times.
                                                                     ENDFOR
'''
FUNCTION taylorSeriesForSine(radians, terms):
    # base case
    IF terms = 0:
        RETURN radians
    ELSE:
        seriesValue <- 1.0
        value <- computePowerOf(radians, ((2*terms)+1))
        IF terms%2 = 0:
            # positive value
            seriesValue <- seriesValue * (value / factorialOf((2*terms)+1))
        ELSE:
            # negative value
            factorial=factorialOf((2*terms)+1)
            float(factorial)
            value=value/factorial
            seriesValue <- seriesValue * -1 * value
    ENDIF
        ENDIF
    RETURN seriesValue + taylorSeriesForSine(radians, terms-1)
ENDFUNCTION

'''def findSine(degrees):
    OUTPUT "the degree is", degrees
    radians <- findRadians(degrees)
    RETURN taylorSeriesForSine(radians, 85)'''
   ENDFUNCTION

FUNCTION alphaValue(iterations):
    lowerLimit=0
    upperLimit=findPIByNilakantaInfiniteSeries(500)
    iterations=1
    while(iterations<9):
        midPoint=(lowerLimit+upperLimit)/2
        valueofLowerlimit=lowerLimit-taylorSeriesForSine(lowerLimit,80)-(findPIByNilakantaInfiniteSeries(500)/2)
        valueofmidPoint=midPoint-taylorSeriesForSine(midPoint,80)-(findPIByNilakantaInfiniteSeries(500)/2)
        IF ((valueofLowerlimit>0 AND valueofmidPoint<0) OR (valueofLowerlimit<0 AND valueofmidPoint>0)):
                upperLimit=midPoint
                OUTPUT lowerLimit
                OUTPUT upperLimit
                iterations=iterations+1
        ELSE:
                lowerLimit=midPoint
                OUTPUT lowerLimit
                OUTPUT upperLimit
                iterations=iterations+1
        ENDIF
    ENDWHILE
    RETURN ((lowerLimit+upperLimit)/2)
ENDFUNCTION

FUNCTION main():
     sineValue=taylorSeriesForSine((findPIByNilakantaInfiniteSeries(500)/2),80)
     OUTPUT "The sine Value is", sineValue
     alpha=alphaValue(9)
     OUTPUT "The alpha Value is", alpha
ENDFUNCTION

main()
