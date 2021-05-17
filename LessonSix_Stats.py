import math
import statistics

agesData = [10, 13, 14, 10, 11, 13, 9, 15]

# mean = average of all numbers
print(statistics.mean(agesData))

# median = the most middle number
print(statistics.median(agesData))

# mode = the number that occurs the most
print(statistics.mode(agesData))

# the sum of all ages
print(sum(agesData))

# sorts data into numerical order
print(sorted(agesData))

# sorts data in reverse numerical order
print(sorted(agesData, reverse=True))

print()
print()

# variance = a lot of math but basically how varied is our data - peak to trough
print(statistics.variance(agesData))
print()

# standard deviation = square root of the variance
print(statistics.stdev(agesData))

# to check yourself ... just import the math lib and
# square the variance yourself and it will = stdev
print(math.sqrt(statistics.variance(agesData)))