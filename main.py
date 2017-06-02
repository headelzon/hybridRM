# AGH Space Systems 2017

import math
from matplotlib import pyplot
import numpy


# Fuel: Paraffin-Al-PE
# Oxidant: Nitrous Oxide N2O
a = 0.000155           # m/sec
n = 0.5

t_burn = 5          # sec (burn time)
no_points = 3000
t = list(numpy.linspace(0, t_burn, no_points))

R_init = 0.045      # m         (port initial radius)
mo_dot = 1.4459     # kg/sec    (oxidizer mass flow)
mf_dot = 0.3615     # kg/sec    (fuel mass flow)
N = 1               #           (no of ports)
ro = 1116           # kg/m3     (fuel density)
# OF_ratio = 4      #           (oxidizer/fuel ratio)


R = []
for i in range(len(t)):
    R.append(
        (a * (2 * n + 1) * ((mo_dot / (math.pi * N)) ** n) * t[i] + R_init ** (2 * n + 1)) ** (1 / (2 * n + 1)))

for i in range(len(t)):
    R[i] = R[i] * 1000

Go = mo_dot / (N * (math.pi * (R_init ** 2)))       # kg/(s*m^2)

r_dot_init = a * (Go ** n)

L = (mf_dot / N) / (2 * math.pi * R_init * ro * r_dot_init)

r_dot_init = r_dot_init * 1000
R_init = R_init * 1000

line = list(numpy.linspace(45, R[2999], 3000))
# RESULTS
print('\nMotor length = {} m\n'.format(round(L, 2)))
print('Port R initial = {} mm'.format(R_init))
print('Port Diameter initial = {} mm\n'.format(2*R[0]))
print('Port R final = {} mm'.format(round(R[len(R)-1]), 2))
print('Port Diameter final = {} mm\n'.format(round(2*R[len(R)-1]), 2))
print('Initial regression rate = {} mm/s'.format(round(r_dot_init, 2)))
print('G0 = {} kg/s*m2'.format(round(Go, 2)))

# GRAPHS
# Port diameter
fig = pyplot.figure(1)
pyplot.title('Port radius over time')
markers_on = [0, 2999]
pyplot.plot(t, R, '-rx', markevery=markers_on)
pyplot.plot(t, line, '--k', linewidth=0.5)
pyplot.xlabel('Burn time [s]')
pyplot.ylabel('R [mm]')
pyplot.grid(True)
pyplot.yticks(numpy.arange(min(R), max(R)+1, 1.0))
pyplot.show()
