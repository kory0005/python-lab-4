from kory0005Library import mpgMeasure

m = float(input('Enter the number of miles driven: '))
g = float(input('Enter the number of gallons used: '))
f = mpgMeasure(m, g)
print('Your car consumption is equal to {0}'.format(f))