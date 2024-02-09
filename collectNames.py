import csv

def getNames(lst):
    with open('names.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(lst)