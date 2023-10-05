data1 = (("1", "Bogdan"), ("2", "Abulkhair"))
data2 = {1: "Bogdan", 2: "Abulkhair"}

dict1 = {}
for i in data1:
    #              0       1
    # print(i)  # ('1', 'Bogdan')
    dict1[int(i[0])] = str(i[1])
print(dict1)  # {1: 'Bogdan', 2: 'Abulkhair'}
