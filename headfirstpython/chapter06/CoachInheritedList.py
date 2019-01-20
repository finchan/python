import athletelist
# from athletelist import AthleteList
vera = athletelist.AthleteList('Vera Vi')
vera.append('1.31')
print(vera.top3())
vera.extend(['2.22', '1-21', '2:22'])
print(vera.top3())
sarah = athletelist.AthleteList()
sarah = sarah.getCoachData('sarah2.txt')
print(sarah.name + "\t" + sarah.dob + "\t" + str(sarah))