def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return mins + '.' + secs


def got_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            return data.strip().split(',')
    except IOError as err:
        print(str(err))
        return None


def got_coach_data2(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            temple = data.strip().split(',')
            return {'Name': temple.pop(0), 'DOB': temple.pop(0), 'Times': str(sorted(set([sanitize(t) for t in temple]))[0:3])}
    except IOError as err:
        print(str(err))
        return None

sarah = got_coach_data('sarah2.txt')
(sarah_name, sarah_dob) = sarah.pop(0), sarah.pop(0)
print(sarah_name + "'s fastest times are: ")
print((sorted(set(sanitize(t) for t in sarah)))[0:3])

sarah = got_coach_data('sarah2.txt')
sarah_data = {}
sarah_data['Name'] = sarah.pop(0)
sarah_data['DOB'] = sarah.pop(0)
sarah_data['TImes'] = sarah
print(sarah_data['Name'] + "'s fastest times are: " +
      str(sorted(set([sanitize(t) for t in sarah_data['TImes']]))[0:3]))

print('------------------------------------------------------------------------')
sarah_data = got_coach_data2('sarah2.txt')
print(sarah_data['Name'] + "'s fastest times are: " + sarah_data['Times'])
james_data = got_coach_data2('james2.txt')
print(james_data['Name'] + "'s fastest times are: " + james_data['Times'])
julie_data = got_coach_data2('julie2.txt')
print(julie_data['Name'] + "'s fastest times are: " + julie_data['Times'])
mikey_data = got_coach_data2('mikey2.txt')
print(mikey_data['Name'] + "'s fastest times are: " + mikey_data['Times'])
print('------------------------------------------------------------------------')

cleese = {}
palin = dict()
print(type(cleese))
print(type(palin))
cleese['Name'] = 'John Cleese'
cleese['Occupations'] = ['actor', 'comedian', 'writer', 'film producer']
palin ={'Name': 'Michael Palin', 'Occupations': ['comedian', 'actor', 'writer', 'tv']}
print(palin['Name'])
print(cleese['Occupations'][-1])
palin['Birthplace'] = 'Broomhill, Sheffield, England'
cleese['Birthplace'] = 'Weston-super-Mare, North Somerset, England'
print(palin)
print(cleese)