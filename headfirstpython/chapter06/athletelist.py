class AthleteList(list):
    def __init__(self, a_name='', a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def sanitize(self,time_string):
        if '-' in time_string:
            splitter = '-'
        elif ':' in time_string:
            splitter = ':'
        else:
            return time_string
        (mins, secs) = time_string.split(splitter)
        return mins + '.' + secs

    def top3(self):
        return sorted(set([self.sanitize(t) for t in self]))[0:3]

    def getCoachData(self, file_name):
        try:
            with open(file_name) as f:
                data = f.readline()
                data_list = data.split(',')
                data_list = [t.strip() for t in data_list]
                self.name = data_list.pop(0)
                self.dob = data_list.pop(0)
                self.extend(data_list)
                return self
        except IOError as ioe:
            print(str(ioe))
            return None