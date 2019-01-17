def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return mins+'.' + secs

def got_coach_data(filename) :
    try:
        with open(filename) as f:
            data = f.readline()
            return data.strip().split(',')
    except IOError as err:
        print(str(err))
        # python uses None as null
        return None

james = got_coach_data('james.txt')
julie = got_coach_data('julie.txt')
mikey = got_coach_data('mikey.txt')
sarah = got_coach_data('sarah.txt')

# list comprehension
clean_james = sorted([sanitize(each_t) for each_t in james])
clean_julie = sorted([sanitize(each_t) for each_t in julie])
clean_mickey = sorted([sanitize(each_t) for each_t in mikey])
clean_sarah = sorted([sanitize(each_t) for each_t in sarah])
unique_james = []
unique_julie = []
unique_mickey = []
unique_sarah = []
for t in clean_james:
    if t not in unique_james:
        unique_james.append(t)
for t in clean_julie:
    if t not in unique_julie:
        unique_julie.append(t)
for t in clean_mickey:
    if t not in unique_mickey:
        unique_mickey.append(t)
for t in clean_sarah:
    if t not in unique_sarah:
        unique_sarah.append(t)


print(clean_james)
print(clean_julie)
print(clean_mickey)
print(clean_sarah)

print(unique_james)
print(unique_julie)
print(unique_mickey)
print(unique_sarah)

print(unique_james[0:3])
print(unique_julie[0:3])
print(unique_mickey[0:3])
print(unique_sarah[0:3])

print(sorted(set(clean_james))[0:3])
print(sorted(set(clean_julie))[0:3])
print(sorted(set(clean_mickey))[0:3])
print(sorted(set(clean_sarah))[0:3])

data = [6,3,1,2,4,5]
# in-place sorting
data.sort()
print(data)
data = [6,3,1,2,4,5]
# copied sorting
data2 = sorted(data)
print(data2)
print(data)

mins = [1, 2, 3]
secs = [60*m for m in mins]
print(secs)

meters = [1, 10, 3]
feet = [m*3.281 for m in meters]
print(feet)

lower = ["I", "don't", "like", "spam"]
upper = [s.upper() for s in lower]
print(upper)

dirty = ["2-22", "2:22", "2.22"]
clean = [float((sanitize(t))) for t in dirty]
print(clean)

