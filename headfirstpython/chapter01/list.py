movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]
print(movies[1])

cast = ["Cleese", "Palin", "Jones", "Idle"]
print(cast)

print(len(cast))

print(cast[1])

# append to add a new data at the end of list
cast.append("Gilliam")
print(cast)

# pop to remove the last data from a list
value = cast.pop()
print(value)
print(cast)

# extend to add a list to the end of the existing list
cast.extend(["Gilliam", "Chapman"])
print(cast)

# remove to delete a specified data from list
cast.remove("Chapman")
print(cast)

# insert to add a data to the corresponding index
cast.insert(1, "Chapman")
print(cast)

for each_cast in cast:
    print(each_cast)

count = 0
while count < len(cast):
    print(cast[count])
    count = count + 1