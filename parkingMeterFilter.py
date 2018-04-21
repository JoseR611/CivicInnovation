import csv
import json

readers = open('Bike_Lanes_data.csv', "rb")
text = (next(readers).decode("utf-8"))
arr = []
num = 1
for i in range(2533):

    newtext = (next(readers).decode("utf-8")).split(',')
    coords = newtext[17].replace('POINT (', '').replace(')','')
    latAndLon = coords.split(' ')###latitude and longitude are reversed
    if (len(latAndLon) is 2 and '42' in latAndLon[1]) and ('-78' in latAndLon[0]):
        numLat = float(latAndLon[1])
        numLon = float(latAndLon[0])
        if (numLat > 42.9220) and (numLat < 42.9281) and (numLon > -78.8774) and (numLon < -78.8673):
            print(num)
            num = num + 1
            arr.append(newtext)

out_file = open("meterOut.json", 'w')
json.dump(arr, out_file)
out_file.close()
