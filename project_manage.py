# import database module

import csv
import os
from datetime import date

from database import Table, Database
from roles import student, lead, faculty

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


DB = Database()


def official_exit():
    pass


def initializing():
    # create a 'persons' table
    persons_table = Table('persons', read_csv('persons.csv'))

    # add the 'persons' table into the database

    DB.insert(persons_table)

    # create a 'login' table
    login_table = Table('login', read_csv('login.csv'))
    DB.insert(login_table)
    print(login_table)

    project_table = Table('project', [])
    """
    Max member is 3
    member1 and member2 can be none
    """
    # TEST PROJECT
    project_dictionary = {"projectID": "1",  # THE ID IS VERY TEMPORARY
                          "title": f'Test',
                          "lead": "Lionel Messi",
                          "member1": None,
                          "member2": None,
                          "advisor": None,
                          "status": None,
                          "evaluator": None
                          }
    project_table.insert(project_dictionary)
    DB.insert(project_table)

    advisor_pending_request_table = Table('advisor_request', [])
    # stuff here
    DB.insert(advisor_pending_request_table)

    member_pending_request_table = Table('member_request', [])
    """
    TESTING
    """
    # request_dict = {'projectID': "1",
    #                 'project_name': 'Test',
    #                 'to_be_member': None,  # no one
    #                 'response': None,  # 1 is accepted 0 is denied
    #                 'response_date': None}
    # pending_project_dict = {'projectID': 1,
    #                         'project_name': "yeah",
    #                         'advisor': val[0],
    #                         'evaluator': "1",
    #                         'evaluator2': "2",
    #                         'feedback': None,
    #                         'feedback2': None,
    #                         'score': None,
    #                         'score2': None,
    #                         'status': None}
    # ad_request_dict = {'projectID': "1",
    #                    'project_name': 'Test',
    #                    'to_be_advisor': "1",  # Invite theGoat NOW!
    #                    'response': None,  # 1 is accepted 0 is denied
    #                    'response_date': None}
    # advisor_pending_request_table.insert(ad_request_dict)
    project_table.filter(lambda x: x["projectID"] == "1")
    project_table.update(1, "status", "pending member")
    """
    TESTING
    """
    DB.insert(member_pending_request_table)

    project_evaluation_request_table = Table('pending_project', [])
    DB.insert(project_evaluation_request_table)

    _assigned_project_table = Table('assigned_project', [])
    # This table use for accepted evaluation only
    DB.insert(_assigned_project_table)

    _proposal_table = Table('proposal', [])
    DB.insert(_proposal_table)
    _report_table = Table('report', [])
    DB.insert(_report_table)


def log_out():
    pass


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
                        print("Wrong password!")
                        continue


initializing()

request_table = DB.search('member_request')
ad_request_table = DB.search('advisor_request')
login_table = DB.search('login')
project_table = DB.search('project')
pending_project_table = DB.search('pending_project')
assigned_project_table = DB.search('assigned_project')
proposal_table = DB.search('proposal')
report_table = DB.search('report')



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
        pass

    elif role == 'student':
        while True:
            print("You can choose the following:\n"
                  "1.Check requests\n"
                  "2.Create project\n"
                  "3.exit\n"
                  )

            choice = check_choice(3)

            this_student_info = login_table \
                .filter(lambda x: x["ID"] == person_ID)
            this_student = student.Student(person_ID, this_student_info.table,
                                           request_table.table)

            if choice == 1:
                accept, ID = this_student.read_request()
                if accept == 0 and ID == 0:
                    continue
                if accept == 1:
                    for project in project_table.table:
                        if project["projectID"] == ID:
                            name = project_table.find(ID, "title")
                            """
                            start adding student the be a member
                            """
                            request_table.update(project["projectID"],
                                                 "response",
                                                 "1")
                            request_table.update(project["projectID"],
                                                 "response_date",
                                                 today)
                            if not project["member1"]:
                                project["member1"] = person_ID
                                login_table.update(person_ID, "role", "member")
                                if not check_pending(ID):
                                    project_table.update("1", "status",
                                                         None)
                                print(
                                    f"You have became a member of {name} "
                                    f"project.\n")
                            elif not project["member2"]:
                                project["member2"] = person_ID
                                login_table.update(person_ID, "role", "member")
                                if not check_pending(ID):
                                    project_table.update(ID, "status",
                                                         None)
                                print(
                                    f"You have became a member of {name} "
                                    f"project.\n")
                            else:
                                print("The project is already full.")
                            continue
                elif accept == -1:  # Denied
                    for project in project_table.table:
                        if project["projectID"] == ID:
                            request_table.update(project["projectID"],
                                                 "response",
                                                 "-1")
                            request_table.update(project["projectID"],
                                                 "response_date",
                                                 today)
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
                exit()

    elif role == 'member':
        pass
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
            choice = check_choice(7)

            if choice == 1:
                this_lead.check_project_status()

            elif choice == 2:
                this_lead.modify_project()

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

            elif choice == 8:
                evaluator_ID, evaluator_ID2 = \
                    this_lead.request_project_evaluation()
                if not evaluator_ID:  # If cancelled
                    continue
                request_dict = {'projectID': this_project["projectID"],
                                'project_name': this_project["title"],
                                'advisor': val[0],
                                'evaluator': evaluator_ID,
                                'evaluator2': evaluator_ID2,
                                'feedback': None,
                                'feedback2': None,
                                'score': None,
                                'score2': None,
                                'status': None}
                pending_project_table.insert(request_dict)
                project_table.update(projectID, "status",
                                     "requesting evaluator")

            elif choice == 9:
                exit()

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
                                           pending_project_table.table,
                                           assigned_project_table.table)

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
                accept, ID = this_faculty.read_evaluate_request()
                if accept == 0 and ID == 0:
                    continue
                this_project = project_table \
                    .filter(lambda x: x["projectID"] == ID).table
                if accept == 1:
                    pending_project_table.update(ID, "evaluator", val[0])
                    project_table.update(ID, "status", "evaluating")
                    print("You accepted to evaluate this project\n")
                    continue
                elif accept == -1:
                    if not check_pending(ID):
                        project_table.update(ID, "status", None)
                    pending_project_table.update(ID,
                                                 "status",
                                                 "faculty rejected")
                    print("You denied to evaluate this project\n")
                    continue
            elif choice == 3:
                pass
                # this_project = pending_project_table \
                #     .filter(lambda x: x["evaluator"] == val[0]).table
                # accept = this_faculty.read_accepted_request()

                # if accept > 0:
                #     pending_project_table.update(this_project['projectID'],
                #                                  "score",
                #                                  accept
                #                                  )
                #     print(f"You approved this project with score {accept} !")
                # elif accept == -1:
                #     pending_project_table.update(this_project['projectID'],
                #                                  "score",
                #                                  "denied"
                #                                  )

            elif choice == 4:
                exit()

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
                                           ad_request_table,
                                           pending_project_table.table,
                                           assigned_project_table.table,
                                           proposal_table.table,
                                           report_table.table)

            if choice == 1:
                accept, ID = this_advisor.read_proposal()

                if accept == 0 and ID == 0:
                    continue
                elif accept == 1:
                    proposal_table.update(ID, "response", "1")
                    if not check_pending(ID):
                        project_table.update(ID, "status", None)
                    print("You approved this proposal.\n")

                elif accept == -1:
                    proposal_table.update(ID, "response", "-1")
                    if not check_pending(ID):
                        project_table.update(ID, "status", None)
                    print("You approved this proposal.\n")

            elif choice == 2:
                accept, ID = this_advisor.read_report()

                if accept == 0 and ID == 0:
                    continue
                elif accept == 1:
                    report_table.update(ID, "response", "1")
                    if not check_pending(ID):
                        project_table.update(ID, "status", None)
                    print("You approved this report.\n")

                elif accept == -1:
                    report_table.update(ID, "response", "-1")
                    if not check_pending(ID):
                        project_table.update(ID, "status", None)
                    print("You approved this report.\n")

            elif choice == 3:
                login_check(person_ID, "faculty")
                # if you want to come back to advisor have to log in again
                break


login_check(val[0], val[1])

# while True:
#     login_check(val[0], val[1])  # purpose is for sudden change in role only

