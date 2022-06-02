#!/usr/bin/python3.7

import sys

alpha = 0.9
beta = 0.9

def double_exponential_smoothing(series, alpha, beta):
    result = [series[0]]
    
    for n in range(1, len(series)+1):
        if n == 1:
            level, trend = series[0], series[1] - series[0]
        if n >= len(series): # we are forecasting
            value = result[-1]
        else:
            value = series[n]

        last_level, level = level, alpha*value + (1-alpha)*(level+trend)
        trend = beta*(level-last_level) + (1-beta)*trend
        result.append(level+trend)

    return round(result[-1], 1)

series = []

for i in range(1, len(sys.argv)):
    series.append(round(float(sys.argv[i]) * 10.0, 1))

print("a " + str(double_exponential_smoothing(series, alpha, beta)) + " c")
