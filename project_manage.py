# import database module

import csv
import os
import glob
import time
from datetime import date

from database import Table, Database
from roles import student, lead, faculty, member

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def read_csv(file_name):
    """
       # By now, you know how to read in a csv file and transform it into a list of dictionaries. For this project, you also need to know how to do the reverse, i.e., writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:

   # https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python
    """
    read_list = []
    with open(os.path.join(__location__, file_name)) as f:
        rows = csv.DictReader(f)
        for r in rows:
            read_list.append(dict(r))
    return read_list


def write_csv(name, list_dict):
    if not list_dict:
        with open(name, 'w', newline='', encoding='utf-8') as myFile:
            return  # replace with nothing

    with open(name, 'w', newline='', encoding='utf-8') as myFile:
        writer = csv.writer(myFile)
        row = [x for x in list_dict[0].keys()]
        writer.writerow(row)
        for dictionary in list_dict:
            writer.writerow(dictionary.values())


DB = Database()


def check_write_csv(file_name):
    csv_file = glob.glob(os.path.join(__location__, f'{file_name}.csv'))
    if csv_file:
        table = Table(file_name, read_csv(f'{file_name}.csv'))
    else:
        table = Table(file_name, [])
    DB.insert(table)


def log_out():
    write_csv("persons.csv", DB.search('persons').table)
    write_csv("login.csv", DB.search('login').table)
    write_csv("project.csv", DB.search('project').table)
    write_csv("advisor_request.csv", DB.search('advisor_request').table)
    write_csv("member_request.csv", DB.search('member_request').table)
    write_csv("pending_project.csv", DB.search('pending_project').table)
    write_csv("assigned_project.csv", DB.search('assigned_project').table)
    write_csv("proposal.csv", DB.search('proposal').table)
    write_csv("report.csv", DB.search('report').table)
    exit()


def initializing():
    persons_table = Table('persons', read_csv('persons.csv'))
    DB.insert(persons_table)

    _login_table = Table('login', read_csv('login.csv'))
    DB.insert(_login_table)

    check_write_csv("project")
    check_write_csv("advisor_request")
    check_write_csv("member_request")
    check_write_csv("pending_project")
    check_write_csv("assigned_project")
    check_write_csv("proposal")
    check_write_csv("report")


# def testing():
#     project_dictionary = {"projectID": "1",  # THE ID IS VERY TEMPORARY
#                           "title": 'Test',
#                           "lead": "1",
#                           "member1": None,
#                           "member2": None,
#                           "advisor": "2",
#                           "status": None}
#     DB.search('project').insert(project_dictionary)


# def reset():
#     persons_table = Table('persons', read_csv('persons.csv'))
#     DB.insert(persons_table)
#
#     _login_table = Table('login', read_csv('login.csv'))
#     DB.insert(_login_table)
#     print(_login_table)
#
#     write_csv("project.csv", [])
#     write_csv("advisor_request.csv", [])
#     write_csv("member_request.csv", [])
#     write_csv("pending_project.csv", [])
#     write_csv("assigned_project.csv", [])
#     write_csv("proposal.csv", [])
#     write_csv("report.csv", [])
#     exit()


def login():
    """
    THE BANE OF EVERYTHING IN THIS PROJECT
    # the 'login' table has the following keys (attributes):
    # person_id
    # username
    # password
    # role

    # this code performs a login task; asking a user for a username and password; returning [person_id, role] if valid, otherwise returning None
    """
    while True:
        username = input('Username: ')
        if username not in [x["username"] for x in login_table.table]:
            print("The username doesn't exist.")
            continue

        while True:
            password = input('Password: ')

            if len(password) != 4:
                print("Password have to be 4 digit integers!")
                continue
            try:
                password = int(password)
            except ValueError as e:
                print(e, "// Password have to be 4 digit integers!")
                continue

            for _person in login_table.table:
                if _person["username"] == username:
                    if _person["password"] == str(password):
                        print("Login successful\n")
                        return [_person["ID"], _person["role"]]  # string
                    else:
                        """
                        log out right away if entered wrong password
                        """
                        print("Wrong password!")
                        return


initializing()

request_table = DB.search('member_request')
ad_request_table = DB.search('advisor_request')
login_table = DB.search('login')
project_table = DB.search('project')
pending_project_table = DB.search('pending_project')
assigned_project_table = DB.search('assigned_project')
proposal_table = DB.search('proposal')
report_table = DB.search('report')


class Admin:
    def __init__(self, ID):
        self.ID = ID
        self.database_list = DB.database
        self.this_database = DB

    def choose_table(self):
        print("There are following tables:\n")
        for index, table in enumerate(self.database_list):
            print(index, table.table_name)
        print()
        choose = input("Enter the name of table you want to choose: ")
        print(f"Chosen table '{choose}'")
        check = self.this_database.search(choose)
        if not check:
            print(f"Table '{choose}' doesn't exist.\n")
            return
        return choose

    def clear_table(self, table_name):
        clear_this = self.this_database.search(table_name)
        self.database_list.remove(clear_this)
        empty_table = Table(table_name, [])
        self.this_database.insert(empty_table)
        print(f"Successfully cleared the table {table_name}\n")

    def update_table(self, table_name):
        this_table = self.this_database.search(table_name)
        for index, row in enumerate(this_table.table):
            print(index, row)

        while True:
            update = input("Enter the row index you want to update: ")
            try:
                update = int(update)
            except TypeError as e:
                print(e, "// row index must be integers!\n")
                continue
            try:
                print(this_table.table[update])
            except IndexError as e:
                print("That row doesn't exist")
                continue
            break

        column = input("Enter the column name you want to update: ")
        new_value = input("Enter the new value: ")
        for index, row in enumerate(this_table.table):
            if index == update:
                name_list = []
                for name in row.keys():
                    name_list.append(name)

                if column not in name_list:
                    print("That column doesn't exist.")
                    return
                else:
                    row[column] = new_value
                    print(f"Successfully updated the table '{table_name}'\n")

    def insert_row(self, table_name):
        this_table = self.this_database.search(table_name)
        new_dict = {}

        for column in this_table.table[0].keys():
            print(column)
            new_value = input("Enter value for this column: ")
            new_dict[column] = new_value

        print(new_dict)
        this_table.insert(new_dict)

        print('Successfully inserted the row.\n')

    def delete_row(self, table_name):
        this_table = self.this_database.search(table_name)

        for index, row in enumerate(this_table.table):
            print(index, row)
        print()

        removed_row = ""
        while True:
            delete_row = input("Enter row index you want to remove: ")
            try:
                delete_row = int(delete_row)
            except TypeError as e:
                print(e, "// row index must be integers!\n")
                continue
            try:
                removed_row = this_table.table.pop(delete_row)
            except IndexError as e:
                print("That row doesn't exist.")
                continue
            break

        print(f"Successfully removed the row {removed_row}\n")


def check_pending(projectID):
    for request in request_table.table:
        if request["projectID"] == projectID and not request["response"]:
            # If there is a pending request
            return True
    for request in ad_request_table.table:
        if request["projectID"] == projectID and not request["response"]:
            # If there is a pending request
            return True
    return False


def check_choice(choice_number):
    while True:
        choice = input("Enter your choice: ")
        if not choice:
            continue
        try:
            choice = int(choice)
        except TypeError as e:
            print(e, "// Choice must be integers!")
        if choice > choice_number or choice < 1:
            print("That choice doesn't exist.")
            continue
        return choice


val = login()


def login_check(person_ID, role):
    today = date.today()
    if role == 'admin':
        while True:
            print("You can choose the following:\n"
                  "1.Update Table\n"
                  "2.Clear Table\n"
                  "3.Insert data\n"
                  "4.Delete row\n"
                  "5.Exit\n"
                  )

            choice = check_choice(5)
            this_admin = Admin(person_ID)
            if choice == 1:
                chosen_table = this_admin.choose_table()
                if not chosen_table:
                    continue
                this_admin.update_table(chosen_table)

            elif choice == 2:
                chosen_table = this_admin.choose_table()
                if not chosen_table:
                    continue
                this_admin.clear_table(chosen_table)

            elif choice == 3:
                chosen_table = this_admin.choose_table()
                if not chosen_table:
                    continue
                this_admin.insert_row(chosen_table)

            elif choice == 4:
                chosen_table = this_admin.choose_table()
                if not chosen_table:
                    continue
                this_admin.delete_row(chosen_table)

            elif choice == 5:
                log_out()

    elif role == 'student':
        while True:
            print("You can choose the following:\n"
                  "1.Check requests\n"
                  "2.Create project\n"
                  "3.Exit\n"
                  )

            choice = check_choice(3)

            this_student_info = login_table \
                .filter(lambda x: x["ID"] == person_ID)
            this_student = student.Student(person_ID, this_student_info.table,
                                           request_table.table,
                                           project_table.table)

            if choice == 1:
                accept, ID = this_student.read_request()
                if accept == 0 and ID == 0:
                    continue
                this_request_table = request_table.filter \
                    (lambda x: x['projectID'] == ID and
                               x['to_be_member'] == person_ID)
                if accept == 1:
                    for project in project_table.table:
                        if project["projectID"] == ID:
                            name = project_table.find(ID, "title")
                            """
                            start adding student the be a member
                            """
                            this_request_table.update(project["projectID"],
                                                      "response",
                                                      "1")
                            this_request_table.update(project["projectID"],
                                                      "response_date",
                                                      today)

                            if not project["member1"]:
                                project["member1"] = person_ID
                                login_table.update(person_ID, "role", "member")
                                if not check_pending(ID):
                                    project_table.update(ID, "status",
                                                         "non")
                                print(
                                    f"You have became a member of {name} "
                                    f"project.\n")
                                login_check(person_ID, "member")
                                break
                            elif not project["member2"]:
                                project["member2"] = person_ID
                                login_table.update(person_ID, "role", "member")
                                if not check_pending(ID):
                                    project_table.update(ID, "status",
                                                         "non")
                                print(
                                    f"You have became a member of {name} "
                                    f"project.\n")
                                login_check(person_ID, "member")
                                break
                            else:
                                print("The project is already full.")
                            continue
                elif accept == -1:  # Denied
                    for project in project_table.table:
                        if project["projectID"] == ID:
                            this_request_table.update(project["projectID"],
                                                      "response",
                                                      "-1")
                            this_request_table.update(project["projectID"],
                                                      "response_date",
                                                      today)
                            if not check_pending(ID):
                                project_table.update(ID, "status",
                                                     "non")
                            print("Denied the request.\n")
                            continue

            elif choice == 2:  # create project , ID is project_dict
                project_dict = this_student.create_project()
                if not project_dict:  # Check if he has pending request
                    continue
                project_dict['lead'] = person_ID
                login_table.update(person_ID, "role", "lead")
                # print(login_table.filter(lambda x: x["ID"] == person_ID))
                project_table.insert(project_dict)
                print()
                login_check(person_ID, "lead")
                break
            elif choice == 3:
                log_out()

    elif role == 'member':
        while True:
            print("You can choose the following:\n"
                  "1.See project status\n"
                  "2.View project\n"
                  "3.Check request responses\n"
                  "4.Exit\n")
            choice = check_choice(4)
            this_member_info = login_table.filter(lambda x: x["ID"] == val[0])
            this_project = \
                project_table.filter(lambda x: x["member1"] == val[0])
            if not this_project.table:
                this_project = project_table.filter \
                    (lambda x: x["member2"] == val[0])

            this_member = member.Member(val[0], this_member_info,
                                        request_table.table,
                                        this_project.table)
            if choice == 1:
                this_member.check_project_status()
            elif choice == 2:
                this_member.view_project()
            elif choice == 3:
                this_member.check_responses()
            elif choice == 4:
                log_out()

    elif role == 'lead':
        while True:
            print("You can choose the following:\n"
                  "1.See project status\n"
                  "2.Modify project\n"
                  "3.Check request responses\n"
                  "4.Invite potential members\n"
                  "5.Invite potential advisor\n"
                  "6.Send project proposal\n"
                  "7.Send project report\n"
                  "8.Request project evaluation\n"
                  "9.Exit\n")

            this_student_info = login_table.filter(lambda x: x["ID"] == val[0])
            this_project = project_table.filter(lambda x: x["lead"] == val[0])
            this_lead = lead.Lead(val[0],
                                  this_student_info.table,
                                  request_table.table,
                                  this_project.table,
                                  ad_request_table.table,
                                  pending_project_table.table,
                                  proposal_table.table,
                                  report_table.table
                                  )
            projectID = this_project.table[0]["projectID"]
            project_name = this_project.table[0]["title"]
            project_advisor = this_project.table[0]["advisor"]
            choice = check_choice(9)

            if choice == 1:
                this_lead.check_project_status()

            elif choice == 2:
                kick = this_lead.modify_project()
                if kick:
                    login_table.update(kick, "role", "student")

            elif choice == 3:
                this_lead.check_responses()

            elif choice == 4:
                student_ID = this_lead.send_request()
                if student_ID:
                    person_list = [x['ID'] for x in login_table.select("ID")]
                    if student_ID not in person_list:
                        print(f"The person with ID: {student_ID} doesn't"
                              f" exist.\n")
                        continue
                    elif login_table.find(student_ID, "role") != "student":
                        print("You can only invite students.\n")
                        continue
                    request_dict = {'projectID': projectID,
                                    'project_name': project_name,
                                    'to_be_member': student_ID,
                                    'response': None,
                                    'response_date': None}
                    request_table.insert(request_dict)
                    print(f"Successfully invited person with ID: {student_ID}"
                          f"\n")
                    project_table.update(projectID, "status", "pending member")

            elif choice == 5:
                advisor_ID = this_lead.send_request_advisor()
                if advisor_ID:
                    person_list = [x['ID'] for x in login_table.select("ID")]
                    if advisor_ID not in person_list:
                        print(f"The person with ID: {advisor_ID}"
                              f" doesn't exist.\n")
                        continue
                    elif login_table.find(advisor_ID, "role") != "faculty":
                        if login_table.find(advisor_ID, "role") != "advisor":
                            print("The person you are requesting is not"
                                  " a faculty.\n")
                            continue
                    request_dict = {'projectID': projectID,
                                    'project_name': project_name,
                                    'to_be_advisor': advisor_ID,
                                    'response': None,
                                    'response_date': None}
                    ad_request_table.insert(request_dict)
                    print(f"Successfully invited a faculty with ID:"
                          f" {advisor_ID}\n")
                    project_table.update(projectID, "status", "pending advisor"
                                         )

            elif choice == 6:
                status = this_lead.send_proposal()
                if status:
                    request_dict = {'projectID': projectID,
                                    'project_name': project_name,
                                    'advisor': project_advisor,
                                    'response': None,
                                    'response_date': None}
                    proposal_table.insert(request_dict)
                    project_table.update(projectID, "status",
                                         "pending proposal")
                    print("Sent proposal to the project advisor.\n")

            elif choice == 7:
                status = this_lead.send_report()
                if status:
                    request_dict = {'projectID': projectID,
                                    'project_name': project_name,
                                    'advisor': project_advisor,
                                    'response': None,
                                    'response_date': None}
                    report_table.insert(request_dict)
                    project_table.update(projectID, "status", "pending report")
                    print("Sent report to the project advisor.\n")

            elif choice == 8:
                evaluator_ID, evaluator_ID2 = \
                    this_lead.request_project_evaluation()
                if evaluator_ID == 0 and evaluator_ID2 == 0:
                    continue
                faculty_table = login_table.filter \
                    (lambda x: (x["role"] == "faculty" or
                                x["role"] == "advisor"))
                faculty_list = faculty_table.aggregate(lambda x: x, "ID")

                if float(evaluator_ID) not in faculty_list:
                    print("Evaluator1 is not a faculty!\n")
                    continue
                if float(evaluator_ID2) not in faculty_list:
                    print("Evaluator2 is not a faculty!\n")
                    continue

                request_dict = {'projectID': projectID,
                                'project_name': project_name,
                                'advisor': project_advisor,
                                'evaluator': evaluator_ID,
                                'evaluator2': evaluator_ID2,
                                'status': None}
                pending_project_table.insert(request_dict)
                project_table.update(projectID, "status",
                                     "requesting evaluator")
                print("Successfully requested the project evaluation.\n")

            elif choice == 9:
                log_out()

    elif role == 'faculty':
        while True:
            print("You can choose the following:\n"
                  "1.Check requests\n"
                  "2.Check evaluate requests\n"
                  "3.evaluate assigned project\n"
                  "4.exit\n"
                  )

            choice = check_choice(4)
            this_faculty_info = login_table.filter(lambda x: x["ID"] == val[0])
            this_faculty = faculty.Faculty(person_ID, this_faculty_info.table,
                                           ad_request_table.table,
                                           pending_project_table,
                                           assigned_project_table.table,
                                           project_table.table)

            if choice == 1:
                accept, ID = this_faculty.read_request()
                if accept == 0 and ID == 0:
                    continue
                if accept == 1:
                    for project in project_table.table:
                        if project["projectID"] == ID:
                            name = project_table.find(ID, "title")
                            """
                            start adding faculty the be an advisor
                            """
                            ad_request_table.update(project["projectID"],
                                                    "response",
                                                    "1")
                            ad_request_table.update(project["projectID"],
                                                    "response_date",
                                                    today)
                            if not project["advisor"]:
                                project["advisor"] = person_ID
                                login_table.update(person_ID, "role", "advisor"
                                                   )
                                if not check_pending(ID):
                                    project_table.update(ID, "status",
                                                         None)
                                project['status'] = "ready for proposal"
                                print(
                                    f"You have became an advisor of {name} "
                                    f"project.\n")
                                print()
                                login_check(person_ID, "advisor")
                                break
                            else:
                                print("The project already had an advisor.")
                            continue
                elif accept == -1:  # Denied
                    for project in project_table.table:
                        if project["projectID"] == ID:
                            ad_request_table.update(project["projectID"],
                                                    "response",
                                                    "-1")
                            ad_request_table.update(project["projectID"],
                                                    "response_date",
                                                    today)
                            print("Denied the request.\n")
                            continue

            elif choice == 2:
                accept, ID, number = this_faculty.read_evaluate_request()
                if accept == 0 and ID == 0:
                    continue
                evaluator = "evaluator1"
                if number == 2:
                    evaluator = "evaluator2"

                def assign_project():
                    pending_project_table.update(ID,
                                                 "status",
                                                 "both evaluator accepted"
                                                 )
                    project_table.update(ID, "status", "evaluating")
                    _project_name = project_table.find(ID, "title")
                    _project_advisor = project_table.find(ID, "advisor")
                    _evaluator = pending_project_table.find(ID, "evaluator")
                    _evaluator2 = pending_project_table.find(ID, "evaluator2")
                    _request_dict = {'projectID': ID,
                                     'project_name': _project_name,
                                     'advisor': _project_advisor,
                                     'evaluator': _evaluator,
                                     'evaluator2': _evaluator2,
                                     'feedback': None,
                                     'feedback2': None,
                                     'score': None,
                                     'score2': None,
                                     'status': None}
                    assigned_project_table.insert(_request_dict)

                if accept == 1:
                    if ((pending_project_table.find(ID, "status") ==
                         "evaluator1 accepted" and number == 2) or
                            (pending_project_table.find(ID, "status") ==
                             "evaluator2 accepted" and number == 1)):
                        assign_project()
                    else:
                        pending_project_table.update(ID,
                                                     "status",
                                                     f"{evaluator} accepted"
                                                     )

                    print("You accepted to evaluate this project\n")
                    continue
                elif accept == -1:
                    if not check_pending(ID):
                        project_table.update(ID, "status", None)
                    pending_project_table.update(ID,
                                                 "status",
                                                 f"{evaluator} rejected")
                    print("You denied to evaluate this project\n")
                    continue

            elif choice == 3:
                this_faculty.evaluate_project()

            elif choice == 4:
                log_out()

    elif role == 'advisor':
        while True:
            print("You can choose the following:\n"
                  "1.Check proposal requests\n"
                  "2.Check report requests\n"
                  "3.Go to faculty menu\n"
                  "4.exit\n"
                  )

            choice = check_choice(4)
            this_advisor_info = login_table.filter(lambda x: x["ID"] == val[0])
            this_advisor = faculty.Advisor(person_ID,
                                           this_advisor_info.table,
                                           ad_request_table.table,
                                           pending_project_table,
                                           assigned_project_table.table,
                                           project_table.table,
                                           proposal_table.table,
                                           report_table.table)

            if choice == 1:
                accept, ID = this_advisor.read_proposal()

                if accept == 0 and ID == 0:
                    continue
                elif accept == 1:
                    proposal_table.update(ID, "response", "1")
                    proposal_table.update(ID, "response_date", today)
                    if not check_pending(ID):
                        project_table.update(ID, "status", "ready for report")
                    print("You approved this proposal.\n")

                elif accept == -1:
                    proposal_table.update(ID, "response", "-1")
                    proposal_table.update(ID, "response_date", today)
                    if not check_pending(ID):
                        project_table.update(ID, "status", None)
                    print("You rejected this proposal.\n")

            elif choice == 2:
                accept, ID = this_advisor.read_report()

                if accept == 0 and ID == 0:
                    continue
                elif accept == 1:
                    report_table.update(ID, "response", "1")
                    report_table.update(ID, "response_date", today)
                    if not check_pending(ID):
                        project_table.update(ID, "status",
                                             "ready for evaluation")
                    print("You approved this report.\n")

                elif accept == -1:
                    report_table.update(ID, "response", "-1")
                    report_table.update(ID, "response_date", today)
                    if not check_pending(ID):
                        project_table.update(ID, "status", None)
                    print("You rejected this report.\n")

            elif choice == 3:
                login_check(person_ID, "faculty")
                # if you want to come back to advisor have to log in again
                break

            elif choice == 4:
                log_out()


if not val:
    log_out()

login_check(val[0], val[1])

