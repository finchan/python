data = open('sketch.txt')
print(data.readline(), end='')
print(data.readline(), end='')
data.seek(0)
for each_line in data:
    if not each_line.find(":") == -1:
        (role, words) = each_line.split(":", 1)
        print(role, end="")
        print(" said: ", end="")
        print(words, end="")
data.close()