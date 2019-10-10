import math

def circleArea(arg1):
    area = math.pi * arg1**2
    return area


def mpgMeasure(arg1, arg2):
    mpg = arg1/arg2
    return mpg;


def temperature(t):
    c = (t - 32) * 5/9
    return c;


def calculateDistanceBetweenPoints(a, b, a1, b1):
    d = float(math.sqrt((b-a)**2 + (b1-a1)**2))
    return d
