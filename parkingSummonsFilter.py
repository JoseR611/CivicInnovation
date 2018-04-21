import csv
import json

readers = open('Parking_Summons.csv', "rb")
text = (next(readers).decode("utf-8"))
arr = []
num = 1
for i in range(1048575):
    newtext = (next(readers).decode("utf-8")).split(',')
    if ('42' in newtext[10]) and ('-78' in newtext[11]):
        if (float(newtext[10]) > 42.9220) and (float(newtext[10]) < 42.9281) and (float(newtext[11]) > -78.8774) and (float(newtext[11]) < -78.8673):
            print(num)
            num = num + 1
            arr.append(newtext)

print (arr[0])
print (type(arr[0]))

print (arr[0][10])
print (type(arr[0][10]))

print (arr[0][11])
print (type(arr[0][11]))

out_file = open("parkingSummon.json", 'w')
json.dump(arr, out_file)
out_file.close()
