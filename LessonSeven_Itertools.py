
import itertools

# infinite counting
for n in itertools.count(50, 2):
    print(n)  # this would run infinitely
    if n == 100:
        break;

# infinite cycling:

x = 0
for c in itertools.cycle([1, 2, 3, 4, 5]):
    print(c)
    x = x + 1
    if x > 50:
        break;

# Infinite Repeating
for r in itertools.repeat(True):
    print(r)
    x = x + 1
    if x> 100:
        break;