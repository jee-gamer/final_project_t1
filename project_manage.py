# import database module
import random

from database import Table, Database, read_csv
import csv, os, copy
# start by adding the admin related code

# create an object to read an input csv file, persons.csv

# create a 'persons' table
persons_table = Table('persons', read_csv('persons.csv'))

# add the 'persons' table into the database
Database1 = Database()
Database1.insert(persons_table)

# create a 'login' table
login_table = Table('login', [])

for person in persons_table.table:
    dictionary = {"person_id": person["ID"],
                  "username": f'{person["first"]}.{person["last"][-1]}',
                  "password": str(random.randrange(1000, 10000)),
                  "role": person["type"]
    }
    login_table.insert(dictionary)

Database1.insert(login_table)
print(login_table)


def login():
    username = input('Username: ')
    password = input('Password: ')

    if len(password) != 4:
        print("Password have to be 4 digit integers!")
        return
    try:
        password = int(password)
    except ValueError as e:
        print(e, "// Password have to be 4 digit integers!")

    if username not in [x["username"] for x in login_table.table]:
        print("The username doesn't exist.")
        return None
    for _person in login_table.table:
        if _person["username"] == username:
            if _person["password"] == str(password):
                print("Login successful")
                return [_person["person_id"], _person["role"]]
            else:
                print("Wrong password!")
                return None


login()

# the 'login' table has the following keys (attributes):
# person_id
# username
# password
# role

# a person_id is the same as that in the 'persons' table
# let a username be a person's fisrt name followed by a dot and the first letter of that person's last name
# let a password be a random four digits string
# let the initial role of all the students be Member
# let the initial role of all the faculties be Faculty

# you create a login table by performing a series of insert operations; each insert adds a dictionary to a list

# add the 'login' table into the database

# add code that performs a login task; asking a user for a username and password; returning [person_id, role] if valid, otherwise returning None

