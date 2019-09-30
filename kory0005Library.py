import math


def circleArea(arg1):
    area = math.pi * arg1**2
    return area

r = float(input('Please enter the radius of circle: '))
a = circleArea(r)

print('The circle area is {0}'.format(a))





def mpgMeasure(arg1, arg2):
    mpg = arg1/arg2
    return mpg;

m = float(input('Enter the number of miles driven: '))
g = float(input('Enter the number of gallons used: '))
f = mpgMeasure(m, g)
print('Your car consumption is equal to {0}'.format(f))





def temperature(t):
    c = (t - 32) * 5/9
    return c;

f = int(input('Enter the degrees fahrenheit: '))
c = temperature(f)
print('the temperature is ' + str(c) + ' degrees celsius.')





def calculateDistanceBetweenPoints(a, b, a1, b1):
    d = float(math.sqrt((b-a)**2 + (b1-a1)**2))
    return d

x = float(input('Please enter the first coordinate (x) of the first point (x, y): '))
y = float(input('Please enter the second coordinate (y) of the first point (x, y): '))
x1 = float(input('Please enter the first coordinate (x1) of the second point (x1, y1): '))
y1 = float(input('Please enter the second coordinate (y1) of the second point (x1, y1): '))

c = calculateDistanceBetweenPoints(x, x1, y, y1)
print('The distance between the two points is ' + str(c))
