
with open('james.txt') as jaf:
    data = jaf.readline()
    james = data.strip().split(",")
with open('julie.txt') as juf:
    data = juf.readline()
    julie = data.strip().split(",")
with open('mikey.txt') as mif:
    data = mif.readline()
    mikey = data.strip().split(",")
with open('sarah.txt') as saf:
    data = saf.readline()
    sarah = data.strip().split(",")

print(james)
print(julie)
print(mikey)
print(sarah)

data = [6,3,1,2,4,5]
# in-place sorting
data.sort()
print(data)
data = [6,3,1,2,4,5]
# copied sorting
data2 = sorted(data)
print(data2)
print(data)

print(sorted(james))
print(sorted(julie))
print(sorted(mikey))
print(sorted(sarah))