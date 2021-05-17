months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "nov", "dec"]


first_half = months[:6]
print(first_half)


print(len(first_half))
print(len(months))


print('cat' in months)
print(3.14 in months)


# lists are mutable
names = ["bob", "ernie", "will", "fred"]
print(names)


names[2] = "changed_name_to_rufus"
print(names)

# remove/pop the name fred off the end of the list
names.pop(3)
print(names)

# add/append the name ricardinho to the end of the list
names.append("ricardinho")
print(names)

# remove the name ernie
names.remove("ernie")
print(names)


# append a list inside another list - a list of lists
names.extend(months)
print(names)


# should show you the value that .pop just popped of the list - now the last value is 'nov'
popped = names.pop()
print(popped)

# reverse the contents of the list
names.reverse()
print(names)

# sort in numerical or alpabetical order - depends on datatype
names.sort()
print(names)

# ------------
nums = [3, 7, 10, 2, 1, 6, 9, 5, 2, 4, 0]

# sort in revers alpha or numerical order
names.sort(reverse=True)
print(names)

# countdown in decending order
nums.sort(reverse=True)
print(nums)