##########################
###### List / Array ######
##########################

lst = ["dog", "cat", "fish"]
print(lst)

lst.append("hamster")
print(lst)

lst.remove("fish")
print(lst)

lst.sort()
print(lst)

##########################
########## Sets ##########
##########################

st = {"Michael", "John", "Willie", "Mark"}
st.add("Bert")
st.add("Bert")
st.add("Bert")
print(st)


###########################
######## Dictonary ########
###########################


d = {
    'bob': 1,
    'sarah': 2,
}
print(d['bob'])
d['bob'] += 1
print(d['bob'])
print(d)
d['michael'] = 7
print(d)


###################################
#### PYTHON 3 STANDARD LIBRARY ####
###################################


FirstName = 'Michael'
LastName = 'Kennedy'

print(len(FirstName))
print(len(LastName))

# Because it has the len property, we can use the len function
FirstName.__len__()


###################################
#### Length ####
###################################


ages = [12, 13, 14, 21, 18, 17, 19, 16]
print(len(ages))

print('------- Iterate through the list -------')

for iterate in range(0, len(ages)):
    print(ages[iterate])


###################################
#### Collection ####
###################################


CandyCollection = {'Bob': 10, 'mary': 5, 'Bert': 2}
print(len(CandyCollection))


#########################################
############ Range & List ###############
#### List func outputs data as tuple ####
#########################################


KeepInMindThingsStartAtZeroInCompScience = range(10)
print(list(KeepInMindThingsStartAtZeroInCompScience))

#### Start at one by ... specifing that you want 1 through 20 (1, 20)

ClassSize = range(1, 20)
print(list(ClassSize))

for student in list(ClassSize):
    print('Student ' + str(student) + ' is here today')


#########################################
############ Min & Max ###############
#########################################


miles = [10, 20, 30, 40, 50]

print("Get the max amount of miles from miles list")
print(max(miles))

print("Get the min amount of miles from miles list")
print(min(miles))


letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
           "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
           "u", "v", "w", "x", "y", "z"]

print("Here is the letters list")
print(letters)
print(len(letters))

print("Min & Max also works with letters")

print("Print min letters")
print(min(letters))

print("Print max letters")
print(max(letters))

AmountOfMelon = 1
AmountOfBanana = 2
AmountOfApples = 3

print(max(AmountOfMelon, AmountOfApples, AmountOfBanana))
print()

#########################################
########## Rounding & Abs  #############
#########################################

myGPA = 3.6
CupOfWater = 0.5
CupOfFlour = 0.4
temp = -5.2

print("Rounds GPA up to 4")
print(round(myGPA))
print()

print("Rounds Cup of Water up to 1")
print(round(CupOfWater))
print()

print("Rounds Cup of Flour down to 0")
print(round(CupOfFlour))
print()

print("Rounds negative numbers too - down to 5")
print(round(temp))
print()

#### abs ####

accountValue = -13
print(abs(accountValue))
print()

#### pow - to the power of ####

print(pow(3, 2))  # 3x3=9
print(pow(9, 2)) # 9x9=81
print()

chancesOfHeadsTails = 0.5
threeInARow = 3

print(pow(chancesOfHeadsTails, threeInARow))
print()

#########################################
########## sorting  #############
#########################################

pointsInGame = [79, 78, 77, 80, 81, 82]
sortedPoints = sorted(pointsInGame)
print(sortedPoints)
print()

print(max(sortedPoints))
print(min(sortedPoints))
print()

# Alphabetical
namesOfDogs = ["Rufus", "Bingo", "Pete"]
print(sorted(namesOfDogs))
print()

## One big issue ...
namesOfCats = ["lady", "furry", "Whiskers"]
print(sorted(namesOfCats))
print()
# ...case matter -- capitalized will always go before lowercase

# to fix this ...
namesOfCats = ["lady", "furry", "Whiskers"]
print(sorted(namesOfCats))
print()

aplha = ["a", "B", "c", "D", "e", "f"]
print(str(aplha) + " with no formatting")
print()

stringAlpha = (sorted("The Roof is on fire".split(), key=str.upper))
print(stringAlpha)
print()

print(sorted(pointsInGame, reverse=True))
print()

## Sorted Dictionary ...

leaderboard = {"Bob": 123,
               "Jack": 132,
               "Rob": 152
               }

print(sorted(leaderboard, reverse=True))


print()



numbs = [73, 43, 95, 17, 22]

the_avg = sum(numbs) / len(numbs)
print(int(the_avg))