import pickle
from athletelist import AthleteList


def getCoachData( file_name):
    try:
        with open(file_name) as f:
            data = f.readline()
            data_list = data.split(',')
            data_list = [t.strip() for t in data_list]
            return AthleteList(data_list.pop(0), data_list.pop(0), data_list)
    except IOError as ioe:
        print(str(ioe))
        return None


def put_to_store(files_list):
    all_athletes = {}
    try:
        for each_file in files_list:
            athlete = getCoachData(each_file)
            all_athletes[athlete.name] = athlete
        with open('athlete.pickle', 'wb') as apk:
            pickle.dump(all_athletes, apk)
    except IOError as ioe:
        print(str(ioe))
    return all_athletes


def get_from_store():
    all_athletes = {}
    try:
        with open('athlete.pickle', 'rb') as apk:
            all_athletes = pickle.load(apk)
    except IOError as ioe:
        print(str(ioe))
    return all_athletes


print(dir())
the_files = ['sarah2.txt', 'james2.txt', 'mikey2.txt', 'julie2.txt']
data = put_to_store(the_files)
print(data)
for each_athlete in data:
    print(each_athlete +'\t'+ 'for each key') # dictionary key
    print(data[each_athlete].name + '\t' + data[each_athlete].dob + '\t' + str(data[each_athlete]), end='\n')

data = get_from_store()
for each_athlete in data:
    print(each_athlete +'\t'+ 'for each key') # dictionary key
    print(data[each_athlete].name + '\t' + data[each_athlete].dob + '\t' + str(data[each_athlete]), end='\n')