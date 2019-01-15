import os
if os.path.exists('sketch.txt'):
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, words) = each_line.split(":", 1)
            print(role, end='')
            print(' said: ', end='')
            print(words, end='')
        except:
            pass
    data.close()
else:
    print('The data file is missing!')


try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, words) = each_line.split(":", 1)
            print(role, end='')
            print(' said: ', end='')
            print(words, end='')
        except:
            pass
    data.close()
except:
    print('The data file is missing!')

try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, words) = each_line.split(":", 1)
            print(role, end='')
            print(' said: ', end='')
            print(words, end='')
        except ValueError:
            pass
    data.close()
except IOError:
    print('The data file is missing!')