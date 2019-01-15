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

movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
          ["Graham Chapman", ["Michael Palin", "John Cleese",
                              "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

print(movies)

for each_item in movies:
    print(each_item)

for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            print(nested_item)
    else:
        print(each_item)

print('_____________________________')
for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            if isinstance(nested_item, list):
                for deeper_item in nested_item:
                    if isinstance(deeper_item, list):
                        for deepest_item in deeper_item:
                            print(deepest_item)
                    else:
                        print(deeper_item)
            else:
                print(nested_item)
    else:
        print(each_item)

movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
          ["Graham Chapman", ["Michael Palin", "John Cleese",
                              "Terry Gilliam", "Eric Idle", "Terry Jones"]]]


def print_lol(a_list):
    for each_item in a_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)


print_lol(movies)
