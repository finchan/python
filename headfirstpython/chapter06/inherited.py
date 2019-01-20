class NameList(list):
    def __init__(self, a_name):
        list.__init__([])
        self.name = a_name


johny = NameList("John Paul Jones")
print(type(johny))
print(dir(johny))

johny.append('Bass Player')
johny.extend(['Composer', 'Arranger', 'Musician'])
print(johny)
print(johny.name)

for attr in johny:
    print(johny.name + "is a " + attr + ".")