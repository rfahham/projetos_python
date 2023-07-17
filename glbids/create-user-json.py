import csv
import json

users = []

with open('glbids.csv', newline='') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        user_id = row[0]
        autorization = row[1]
        users.append(
            {
                "userId": user_id,
                "autorization": autorization
            }
        )

with open('users.json', 'w') as json_file:
    json.dump(users, json_file)
