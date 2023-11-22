# import database module
import random

from database import Table, Database
import csv, os, copy
from roles import student, member, lead

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def read_csv(file_name):
    """
       # By now, you know how to read in a csv file and transform it into a list of dictionaries. For this project, you also need to know how to do the reverse, i.e., writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:

   # https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python
   DID NOT DO YET
    """
    read_list = []
    with open(os.path.join(__location__, file_name)) as f:
        rows = csv.DictReader(f)
        for r in rows:
            read_list.append(dict(r))
    print(read_list)
    return read_list

def write_csv(name, list_dict):  # working
    myFile = open(name, 'w')
    writer = csv.writer(myFile)
    row = [x for x in list_dict[0].keys()]
    writer.writerow(row)
    for dictionary in list_dict:
        writer.writerow(dictionary.values())
    myFile.close()

def exit():
    pass

def initializing():
    # create a 'persons' table
    persons_table = Table('persons', read_csv('persons.csv'))

    # add the 'persons' table into the database
    global Database1
    Database1 = Database()
    Database1.insert(persons_table)

    # create a 'login' table
    login_table = Table('login', read_csv('login.csv'))
    Database1.insert(login_table)
    print(login_table)

    project_table = Table('project',[])
    """
    Max member is 3
    member1 and member2 can be none
    """
    # TEST PROJECT
    project_dictionary = {"projectID": str(random.randrange(10, 100)), # THE ID IS VERY TEMPORARY
                          "title": f'Test',
                          "lead": "Lionel Messi",
                          "member1": None,
                          "member2": None,
                          "advisor": None,
                          "status": None
                          }
    project_table.insert(project_dictionary)
    Database1.insert(project_table)

    advisor_pending_request_table = Table('advisor_request', [])
    # stuff here
    Database1.insert(advisor_pending_request_table)

    member_pending_request_table = Table('member_pending', [])
    request_dict = {'projectID': 1,
                    'project_name': 'Test',
                    'to_be_member': "5662557",  # Manuel.N
                    'response': None,
                    'response_date': None}
    member_pending_request_table.insert(request_dict)
    Database1.insert(member_pending_request_table)

def login():
    """
    THE BANE OF EVERYTHING IN THIS PROJECT
    # the 'login' table has the following keys (attributes):
    # person_id
    # username
    # password
    # role

    # add code that performs a login task; asking a user for a username and password; returning [person_id, role] if valid, otherwise returning None
    """
    login_table = Database1.search("login")

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
                return [_person["ID"], _person["role"]]
            else:
                print("Wrong password!")
                return None


initializing()
val = login()

if val[1] == 'admin':
    pass

elif val[1] == 'student':
    request_table = Database1.search('member_pending')
    student = student.Student(val[0], request_table.table)
    accept = student.read_request()
    if accept:
        project_list = Database1.search('project')
        for project in project_list.table:
            if project["ID"] == accept:  # start adding student to be a member
                if not project["member1"]:
                    project["member1"] = val[0]
                elif not project["member2"]:
                    project["member2"] = val[0]
                else:
                    print("The project is already full.")

elif val[1] == 'member':
    pass
elif val[1] == 'lead':
    pass
elif val[1] == 'faculty':
    pass
elif val[1] == 'advisor':
    pass

exit()


