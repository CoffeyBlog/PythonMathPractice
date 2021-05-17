import random

print("----------------")
print("My guessing game")
print("----------------")


print("Try to guess the number!")
print()


mm_count = random.randint(1, 100)
print(mm_count)


attempt_limit = 5
attempts = 0

while attempts < attempt_limit:
    guess_text = input("What is your guess  ")
    guess = int(guess_text)

    print(guess)

    attempts += 1



print("bye")