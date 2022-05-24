import matplotlib.pyplot as plt
from scipy.ndimage.filters import gaussian_filter1d
import numpy as np

def line_of_best_fit(x1, x2, y1, y2):
    b = (y2/y1)**(1/(x2-x1))
    a = y1/b**x1
    print(f"y = {a}*{b}^x")
    
    values = [a*b**i for i in range(x2)]
    return values

file = open("tests/hash_times_20000.txt", "r")
times = file.read().split()
times = [float(i) for i in times]

times_smoothed = gaussian_filter1d(times, sigma=25)
lineofbestfit = line_of_best_fit(0, len(times_smoothed), times_smoothed[0], times_smoothed[-1])

plt.plot(times_smoothed)
plt.plot(lineofbestfit)
ax = plt.gca()

ax.set_yticks(ax.get_yticks()[::1])
plt.grid(False)
plt.ylabel("Time")
plt.show()