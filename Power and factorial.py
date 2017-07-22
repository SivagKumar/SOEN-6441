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