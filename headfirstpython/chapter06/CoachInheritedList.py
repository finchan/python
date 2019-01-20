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

vera = AthleteList('Vera Vi')
vera.append('1.31')
print(vera.top3())
vera.extend(['2.22', '1-21', '2:22'])
print(vera.top3())
sarah = AthleteList()
sarah = getCoachData('sarah2.txt')
print(sarah.name + "\t" + sarah.dob + "\t" + str(sarah))