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


sarah = got_coach_data('sarah2.txt')
(sarah_name, sarah_dob) = sarah.pop(0), sarah.pop(0)
print(sarah_name + "'s fastest times are: ")
print((sorted(set(sanitize(t) for t in sarah)))[0:3])