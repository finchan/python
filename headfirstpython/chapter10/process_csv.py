
with open("PaceData.csv") as file:
    headers = file.readline().strip().split(',')
    headers_title = headers.pop(0)
    dataset = {}
    for each_line in file:
        datarow = each_line.strip().split(',')
        rowname = datarow.pop(0)
        inner_dict = {}
        for i in range(len(headers)):
            inner_dict[datarow[i]] = headers[i]
        dataset[rowname] = inner_dict
column_heading = dataset['15k']['43:24']
print(column_heading)

prediction = [k for k in dataset['20k'].keys() if dataset['20k'][k] == column_heading]
print(prediction)

distance_run = input("Enter the distance attempted:")
recorded_time = input("Enter the recording time:")
predicted_distance = input("Enter the distance you want a prediction for:")

print(dataset[distance_run][recorded_time])