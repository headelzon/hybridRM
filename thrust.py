from matplotlib import pyplot
import numpy


t_total = 10
impulse = 20560

f = open('curve.txt', 'r')

curve = []
for line in f:
    curve.append(int(line.rstrip()))
f.close()

curve = curve[201:260]
curve = numpy.interp(curve, [min(curve), max(curve)], [0, 1])
t = list(numpy.linspace(0, t_total, len(curve)))

t_burn = t[23]          # Liquid oxidizer flow time (manually defined)

F_max, I_total = 0, 0   # Thrust [N]
while I_total < impulse:
    thrust_curve = []
    for i in range(len(curve)):
        thrust_curve.append(F_max * curve[i])
    I_total = numpy.trapz(thrust_curve, t)
    F_max += 10

F_av = numpy.mean(thrust_curve)

# RESULTS
t_burn = t[23]
print('Liquid oxidizer flow for {} seconds.\n'.format(round(t_burn, 2)))
print('Total impulse:\t{}\tNs'.format(round(I_total, 2)))
print('Max thrust:\t\t{}\t\tN'.format(round(F_max, 2)))
print('Average thrust:\t{}\t\tN'.format(round(F_av, 2)))

pyplot.figure()
pyplot.plot(t, thrust_curve)
pyplot.title('Thrust curve')
pyplot.xlabel('Time [s]')
pyplot.ylabel('Thrust [N]')
pyplot.yticks(numpy.arange(min(thrust_curve), max(thrust_curve)+10, (max(thrust_curve)-min(thrust_curve))/15))
pyplot.grid(True)
pyplot.show()