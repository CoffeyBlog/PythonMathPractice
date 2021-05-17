import math
import random

# factorial
print(math.factorial(3))  # (3 x 2 x 1) = 6
print()

# square root
print(math.sqrt(64))  # 8 - what times its self is equal to nine
print()

# Greatest common denominator
print(math.gcd(52, 8))
print()

# random
print(random.random())
print()

# heads or tails
headsOrTails = random.randrange(2)
if headsOrTails == 0:
    print("Heads")
else:
    print("Tails")


print()
print()


# dice
dice = random.randrange(1, 7)
print(dice)


print()
print()


lotteryNumbers = random.sample(range(100), 5)
print(lotteryNumbers)


print()
print()


possibleOutcomes = ["Kentucky", "Duke", "North Carolina", "Kansas"]
print(random.choice(possibleOutcomes))


print()
print()

random.shuffle(possibleOutcomes)
print(possibleOutcomes)