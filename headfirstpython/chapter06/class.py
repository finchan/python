class Athlete:
    def __init__(self, a_name='', a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

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
        return str(sorted(set([self.sanitize(t) for t in self.times]))[0:3])

    def got_coach_data(self, filename):
        try:
            with open(filename) as f:
                data = f.readline()
                temple = data.strip().split(',')
                self.name = temple.pop(0)
                self.dob = temple.pop(0)
                self.times = temple
                return self
                # return Athlete(temple.pop(0), temple.pop(0), temple)
        except IOError as err:
            print(str(err))
            return None

    def add_time(self, time_value):
        self.times.append(time_value)

    def add_times(self, list_of_times):
        self.times.extend(list_of_times)


vera = Athlete('vera vi')
vera.add_time('1.31')
print(vera.top3())
vera.add_times(['2.22', '1-21', '2:22'])
print(vera.top3())


sarah = Athlete('Sarah Sweeney', '2002-6-17', ['2:58', '2.58', '1.56'])
james = Athlete('James Jones')
print(type(sarah))
print(type(james))
print(sarah)
print(james)
print(sarah.name)
print(james.name)
print(sarah.dob)
print(james.dob)
print(sarah.times)
print(james.times)
james = Athlete().got_coach_data("james2.txt")
print(james.name + "'s best records: " + str(james.top3()))
julie = Athlete().got_coach_data("julie2.txt")
print(julie.name + "'s best records: " + str(julie.top3()))
mikey = Athlete().got_coach_data("mikey2.txt")
print(mikey.name + "'s best records: " + str(mikey.top3()))
sarah = Athlete().got_coach_data("sarah2.txt")
print(sarah.name + "'s best records: " + str(sarah.top3()))