import pandas as pd


travel_doc = pd.read_excel('./cities.xlsx')
cities = travel_doc.to_dict('records')

print(travel_doc)
print()
print()
for i in range(0, len(cities)):
    print(str(i) + ':')
    for key in cities[i]:
        print("     " + key + ':' + str(cities[i][key]))
    print()