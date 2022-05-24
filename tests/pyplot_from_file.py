from statistics import fmean
import matplotlib.pyplot as plt
from scipy.ndimage.filters import gaussian_filter1d
import numpy as np
from scipy.optimize import curve_fit

def objective(x, a, b, c):
    return a * x + b * x**2 + c

def horizontal_line(limit, y):
    return [y for i in range(limit)]

# Exponential formula
def exponential(x, a, b):
    return a*np.exp(b*x)

# My usual line of best fit for exponential
def line_of_best_fit(x1, x2, y1, y2):
    b = (y2/y1)**(1/(x2-x1))
    a = y1
    print(f"y = {a}*{b}^x")
    
    values = [a*b**i for i in range(x2)]
    return values, f"y = {a}({b})^x"

def average_graphs(y_val1, y_val2):
    average_graph = []
    for i in range (len(y_val1)):
        average_graph.append(fmean([y_val1[i], y_val2[i]]))
    return average_graph

########### Data Preparation ###########

# File reading
file = open("tests/hash_times_50000.txt", "r")
times = file.read().split()
times = [float(i) for i in times]

# Smooth the data with a gaussian filter
times_smoothed = gaussian_filter1d(times, sigma=25)


########### Line of Best Fit ###########

# Find line of best fit with usual formula
lineofbestfit1, equation = line_of_best_fit(0, len(times), times_smoothed[0], times_smoothed[-1])

# Find line of best fit with curve_fit
pars, cov = curve_fit(f=exponential, xdata=range(len(times_smoothed)), ydata=times_smoothed, p0=[0, 0], bounds=(-np.inf, np.inf))
lineofbestfit2 = exponential(range(len(times_smoothed)), *pars)

# Find line of best fit by averaging the two lobfs
average_lobf = average_graphs(lineofbestfit1, lineofbestfit2)


########### Difference Graphs ###########

# Find difference between parent graph and first line of best fit
difference_graph1 = []
for i in range(len(times_smoothed)):
    difference_graph1.append(times_smoothed[i] - lineofbestfit1[i])

# Find difference between parent graph and second line of best fit
difference_graph2 = []
for i in range(len(times_smoothed)):
    difference_graph2.append(times_smoothed[i] - lineofbestfit2[i])

difference_graph3 = []
for i in range(len(times_smoothed)):
    difference_graph3.append(times_smoothed[i] - average_lobf[i])


########### Plotting Graphs ###########

print(f"differnce_graph1: {fmean(difference_graph1)} \ndifference_graph2: {fmean(difference_graph2)} \ndifference_graph3: {fmean(difference_graph3)}")
print(min(abs(fmean(difference_graph1)), abs(fmean(difference_graph2)), abs(fmean(difference_graph3))))

# Plot the data graphs
plt.plot(times_smoothed, color="black")
plt.plot(lineofbestfit1, color="green")
plt.plot(lineofbestfit2, linestyle=':', linewidth=2, color='blue')
plt.plot(average_lobf, color="red")

# Plot the difference graphs
plt.text(500, difference_graph1[0]+0.005, "Difference Graphs", fontsize=8)
plt.plot(difference_graph1, color="green")
plt.plot(difference_graph2, color="blue")
plt.plot(difference_graph3, color="red")
plt.plot(horizontal_line(len(times_smoothed), 0), linestyle=':')
plt.text(-100, times_smoothed[-1], equation)

# Formatting
ax = plt.gca()
ax.set_yticks(ax.get_yticks()[::1]) # Set y-ticks to every second value
plt.grid(False) # Remove grid
plt.ylabel("Time")
plt.show()