import csv

headers = ['Name', 'Age', 'Country']
data = [['John', 'Doe', 42], ['Jane', 'Doe', 37]]

with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(headers)
    writer.writerows(data)