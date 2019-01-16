import pickle
from headfirstpython.chapter02.nester import *

man = []
other = []
try:
    data = open("sketch.txt")
    try:
        for each_line in data:
            (role, line_spoken) = each_line.split(":", 1)
            line_spoken = line_spoken.strip()
            if role == "Man":
                man.append(line_spoken)
            elif role == "Other Man":
                other.append(line_spoken)
    except ValueError:
        pass
except IOError:
    print("No file found")
try:
    man_file = open("man_data.txt", "w")
    other_file = open("other_data.txt", "w")
    print(man, file=man_file)
    print(other, file=other_file)
except IOError:
    print("File Error")
finally:
    if man_file in locals():
        man_file.close()
    if other_file in locals():
        other_file.close()


try:
    with open('man_data.txt', 'w') as man_file, open('other_data.txt', 'w') as other_file:
        print_lol4(man, fn=man_file)
        print_lol4(other, fn=other_file)
except IOError as err:
    print("File Error: " + str(err))

try:
    with open('man_data.txt') as mf:
        print(mf.readline())
except IOError as err:
    print(str(err))

try:
    with open('man_data.txt', 'wb') as man_file, open('other_data.txt', 'wb') as other_file:
        pickle.dump(man, man_file)
        pickle.dump(other, other_file)
except IOError as err:
    print('File Error: ' + str(err))
except pickle.PickleError as pirr:
    print('Pickling Error - Dump Error: ' + str(pirr))

try:
    with open('man_data.txt', 'rb') as man_file:
        man = pickle.load(man_file)
        print_lol4(man)
except IOError as err:
    print("File Error: " + str(err))
except pickle.PickleError as pirr:
    print("Pickling Error: " + str(pirr))
print(man[0])
print(man[-1])
