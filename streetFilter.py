import csv
import json

readers = open('Railroads_data.csv', "rb")
text = (next(readers).decode("utf-8")) # firstline

arr = []
num = 1

for i in range(13000):
    newline = (next(readers).decode("utf-8"))
    store = ""
    parentheses = 0
    for char in newline:
        if char is ')':
            break
        if parentheses is 2:
            store = store + char
        if char is '(':
            parentheses = parentheses + 1
    newtext = store.split(', ')
    holdCoords = []
    for coords in newtext:
        holdCoords.append(coords.split(' '))
    latAndLon = holdCoords[0]
    if ('42' in latAndLon[1]) and ('-78' in latAndLon[0]):###latitude and longitude are reversed
        if (float(latAndLon[1]) > 42.9220) and (float(latAndLon[1]) < 42.9281) and (float(latAndLon[0]) > -78.8774) and (float(latAndLon[0]) < -78.8673):
            remove = ""
            quotes = 0
            for char in newline:
                if char is "\"":
                    quotes = quotes + 1
                if quotes is 1:
                    remove = remove + char
                if quotes is 2:
                    remove = remove + char
                    break
            replaceWithSpace = newline.replace(remove, ' ')
            splitElems = replaceWithSpace.split(',')
            num = num + 1
            splitElems[0] = holdCoords
            arr.append(splitElems)

out_file = open("streetInfo.json", 'w')
json.dump(arr, out_file)
out_file.close()
