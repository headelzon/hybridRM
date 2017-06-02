import numpy


y = [1 for i in range(100)]
x = list(numpy.linspace(0, 10, 100))

integral = numpy.trapz(y, x)
print(integral)