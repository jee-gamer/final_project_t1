import copy


class Lead:
    def __init__(self, ID, info, request_table, project_info,
                 ad_request_table, evaluate_table, proposal_table,
                 report_table):
        self.ID = ID
        self.request_table = request_table
        self.project_info = project_info[0]
        self.ad_request_table = ad_request_table
        self.evaluate_table = evaluate_table
        self.proposal_table = proposal_table
        self.report_table = report_table
        self.project_ID = self.project_info['projectID']
        self.project_name = self.project_info['title']

    def check_project_status(self):
        print(f"The project status is '{self.project_info['status']}'\n")

    def modify_project(self):
        while True:
            print("You can choose the following:\n"
                  "1.View project\n"
                  "2.Change project title\n"
                  "3.Kick member1\n"
                  "4.Kick member2\n"
                  "5.exit\n"
                  )
            while True:
                choice = input("Enter your choice: ")
                try:
                    choice = int(choice)
                except TypeError as e:
                    print(e, "// Choice must be integers!")
                if choice > 5 or choice < 1:
                    print("That choice doesn't exist.")
                    continue
                break
            if choice == 1:
                print(self.project_info)

            elif choice == 2:
                new_title = input("Enter your new project title: ")
                if new_title == self.project_info['title']:
                    print("The new title is the same as the old title.\n")
                    continue
                self.project_info['title'] = new_title
                print(f"Successfully changed the project title to {new_title}."
                      f"\n")

            elif choice == 3:
                if not self.project_info['member1']:
                    print("There's no member1.\n")
                    continue
                print(f"Are you sure you're going to kick member"
                      f" with ID: {self.project_info['member1']}"
                      f" from your project?")
                sure = input("(y/n): ")
                if sure == "y":
                    memberID = copy.deepcopy(self.project_info['member1'])
                    self.project_info['member1'] = None
                    print(f"Kicked student {memberID} from your project.")
                    return memberID
                else:
                    print("You decided not to kick the member.\n")
                    continue

            elif choice == 4:
                if not self.project_info['member2']:
                    print("There's no member2.\n")
                    continue
                print(f"Are you sure you're going to kick member"
                      f" with ID: {self.project_info['member1']}"
                      f" from your project?")
                sure = input("(y/n): ")
                if sure == "y":
                    memberID = copy.deepcopy(self.project_info['member2'])
                    self.project_info['member2'] = None
                    print(f"Kicked student {memberID} from your project.")
                    return memberID
                else:
                    print("You decided not to kick the member.\n")
                    continue

            elif choice == 5:
                return

    def check_responses(self):
        request_list = []
        for request in self.request_table:
            if request["projectID"] == self.project_info["projectID"]:
                print(request)
                request_list.append(request)
        if not request_list:
            print("There are no request.\n")

    def send_request(self):
        if self.project_info["member1"] and self.project_info["member2"]:
            print("Your project member is already full.\n")
            return
        acceptable_status = ["non", "pending member", None, ""]
        if self.project_info['status'] not in acceptable_status:
            print("You can't invite people anymore")
            print("Since you have either")
            print("1. Already sent advisor request")
            print("2. Already sent proposal request to advisor")
            print("3. Already made a lot of progress into the project\n")
            return

        student_id = input("Enter the id of the student you want to invite: ")
        try:
            student_id = int(student_id)
            student_id = str(student_id)
        except TypeError as e:
            print(e, "// student_id must be integers!\n")
            return
        for request in self.request_table:
            if request["projectID"] == self.project_info["projectID"]:
                if request["to_be_member"] == student_id and \
                   not request["response"]:
                    print("You have already invited this student.\n")
                    return
                elif self.project_info["member1"] == student_id:
                    print("This student is already a member of your project.\n"
                          )
                    return
                elif self.project_info["member2"] == student_id:
                    print("This student is already a member of your project.\n"
                          )
                    return
                elif request["to_be_member"] == student_id and\
                        request["response"] == "-1":
                    self.request_table.remove(request)
                elif request["to_be_member"] == student_id and\
                        request["response"] == "1":  # means kicked and invite
                    self.request_table.remove(request)

        if student_id == self.ID:
            print("You can't invite yourself!\n")
            return
        return student_id

    def send_request_advisor(self):
        print("Are you sure? You won't be able to invite more member after "
              "you request an advisor.")
        accept = input("Enter your choice (y/n): ")
        if accept == "y":
            if self.project_info["advisor"]:
                print('You already have a project advisor.\n')
                return
            for request in self.request_table:
                if (
                    request["projectID"] == self.project_info["projectID"] and
                    not request["response"]
                ):
                    print("There's still pending member requests.\n")
                    return

            faculty_id = input(
                "Enter the id of the faculty you want to invite: ")
            try:
                faculty_id = int(faculty_id)
                faculty_id = str(faculty_id)
            except TypeError as e:
                print(e, "// faculty_id must be integers!\n")
                return
            for request in self.ad_request_table:  # Check if already requested
                if (
                    request["projectID"] == self.project_info["projectID"] and
                    not request["response"]
                ):
                    print('You have already requested an advisor for'
                          ' this project.'
                          '\n')
                    return
            return faculty_id
        else:
            print()
        return

    def send_proposal(self):
        if not self.project_info['advisor']:
            print("You don't have a project advisor yet\n")
            return False
        for request in self.proposal_table:
            if request["projectID"] == self.project_info["projectID"]:
                if not request["response"]:
                    print("You have already sent a proposal approval "
                          "request to advisor.\n")
                    return False
                if request["response"] == "1":
                    print("This project proposal is already approved\n")
                    return False
        return True

    def send_report(self):
        projectID_list = []
        for request in self.proposal_table:
            projectID_list.append(request["projectID"])
            if request["projectID"] == self.project_info["projectID"]:
                if not request["response"] or request["response"] == "-1":
                    print("The project proposal hasn't been approved yet!\n")
                    return False

        for request in self.report_table:
            if request["projectID"] == self.project_info["projectID"]:
                if not request["response"]:
                    print("You have already sent a report approval "
                          "request to advisor.\n")
                    return False
                if request["response"] == "1":
                    print("This project report is already approved\n")
                    return False

        if self.project_info["status"] != "ready for report":
            print("You haven't sent the proposal yet!\n")
            return False

        return True

    def request_project_evaluation(self):
        if self.project_info['status'] == "passed":
            print("This project is already passed\n")
            return 0, 0
        for r in self.evaluate_table:
            if r['projectID'] == self.project_info['projectID']:
                if not r['status']:
                    print("You have already sent a project evaluation request."
                          "\n")
                    return 0, 0
                if r['status'] == "1":
                    print("Evaluation request is already accepted."
                          "\n")
                    return 0, 0

        if self.project_info['status'] != "ready for evaluation":
            print("This project is not ready for evaluation yet.\n")
            return 0, 0
        while True:
            print("You can choose two faculty to evaluate your project")
            chosen_ev = input("Enter your first project's evaluator ID: ")
            chosen_ev2 = input("Enter your second project's evaluator ID: ")
            try:
                chosen_ev = int(chosen_ev)
                chosen_ev2 = int(chosen_ev2)
                chosen_ev = str(chosen_ev)
                chosen_ev2 = str(chosen_ev2)
            except TypeError as e:
                print(e, "// evaluator_id must be integers!")
                continue
            if not chosen_ev or not chosen_ev2:
                print("You cancelled the request.\n")
                return None
            advisor = self.project_info['advisor']
            if chosen_ev == advisor or chosen_ev2 == advisor:
                print("You can't choose a faculty that is the advisor of your"
                      " project.\n")
                continue
            return str(chosen_ev), str(chosen_ev2)


