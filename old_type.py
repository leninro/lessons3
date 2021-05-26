import csv

user_list = [
        {'name': 'MASHA', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'VASIA', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'EDUARD', 'age': 48, 'job': 'Big boss'},
]

with open('export.csv', 'w', encoding='utf-8', newline='') as f:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(f, fields, delimiter=',')
    writer.writeheader()
    for user in user_list:
        writer.writerow(user)