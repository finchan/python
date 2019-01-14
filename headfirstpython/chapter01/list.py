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
print(movies[4][1][3])
print(movies)
for each_item in movies:
    print(each_item)

print('---------------------------')

for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            print(nested_item)
    else:
        print(each_item)

names = ["Michael", "Terry"]
print(isinstance(names, list))
num_names = len(names)
print(isinstance(num_names, list))

# ----Check all BIFs - IDE - type
# dir(__builtins__)
# help(specified builtin) to check specified builtin
print('---------------------------')
movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
          ["Graham Chapman", ["Michael Palin", "John Cleese",
                              "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            if isinstance(nested_item, list):
                for deeper_item in nested_item:
                    print(deeper_item)
            else:
                print(nested_item)
    else:
        print(each_item)

print('###############')


def print_lol(a_list):
    for _each_item in a_list:
        if isinstance(_each_item, list):
            print_lol(_each_item)
        else:
            print(_each_item)


print_lol(movies)
