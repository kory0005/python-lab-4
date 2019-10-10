from kory0005Library import calculateDistanceBetweenPoints

x = float(input('Please enter the first coordinate (x) of the first point (x, y): '))
y = float(input('Please enter the second coordinate (y) of the first point (x, y): '))
x1 = float(input('Please enter the first coordinate (x1) of the second point (x1, y1): '))
y1 = float(input('Please enter the second coordinate (y1) of the second point (x1, y1): '))

c = calculateDistanceBetweenPoints(x, x1, y, y1)
print('The distance between the two points is ' + str(c))