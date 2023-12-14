
class Lead:
    def __init__(self, ID, info, request_table, project_info,
                 ad_request_table, evaluate_table):
        self.ID = ID
        self.request_table = request_table
        self.project_info = project_info[0]
        self.ad_request_table = ad_request_table
        self.evaluate_table = evaluate_table

    def check_project_status(self):
        print(f"The project status is {self.project_info['status']}\n")

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
                except ValueError as e:
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
                    self.project_info['member1'] = None
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
                    self.project_info['member2'] = None
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
        student_id = input("Enter the id of the student you want to invite: ")
        try:
            student_id = int(student_id)
            student_id = str(student_id)
        except ValueError as e:
            print(e, "// student_id must be integers!\n")
            return
        for request in self.request_table:
            if request["projectID"] == self.project_info["projectID"]:
                if int(request["to_be_member"]) == student_id and \
                   not request["response"]:
                    print("You have already invited this student.\n")
                    return
                elif self.project_info["member1"] == student_id:
                    print("This student is already a member of your project.\n"
                          )
                    return
        if student_id == self.ID:
            print("You can't invite yourself!\n")
            return
        return student_id

    def send_request_advisor(self):
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

        faculty_id = input("Enter the id of the faculty you want to invite: ")
        try:
            faculty_id = int(faculty_id)
            faculty_id = str(faculty_id)
        except ValueError as e:
            print(e, "// faculty_id must be integers!\n")
            return
        for request in self.ad_request_table:  # Check if already requested
            if (
                request["projectID"] == self.project_info["projectID"] and
                not request["response"]
            ):
                print('You have already requested an advisor for this project.'
                      '\n')
                return
        return faculty_id

    def request_project_evaluation(self):
        if self.project_info['status'] == "passed":
            print("This project is already passed\n")
            return None
        while True:
            print("You can choose two faculty to evaluate your project")
            chosen_ev = input("Enter your first project's evaluator ID: ")
            chosen_ev2 = input("Enter your second project's evaluator ID: ")
            try:
                chosen_ev = int(chosen_ev)
                chosen_ev2 = int(chosen_ev2)
            except ValueError as e:
                print(e, "// evaluator_id must be integers!")
                continue
            if not chosen_ev or not chosen_ev2:
                print("You cancelled the request.\n")
                return None
            return str(chosen_ev), str(chosen_ev2)


