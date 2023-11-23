
class Lead:
    def __init__(self, ID, request_table, info, project_info):
        self.request_table = request_table
        self.project_info = project_info
        pass

    def check_project_status(self):
        print(f"The project status is {self.project_info['status']}\n")

    def modify_project(self):
        # Ehh how?
        pass

    def check_responses(self):
        for request in self.request_table:
            if request["projectID"] == self.project_info["projectID"]:
                print(request)

    def send_request(self):
        if self.project_info["member1"] and self.project_info["member2"]:
            print("Your project member is already full.")
            return
        student_id = input("Enter the id of the student you want to invite: ")
        try:
            student_id = int(student_id)
        except ValueError as e:
            print(e, "// student_id must be integers!")
        for request in self.request_table:
            if request["projectID"] == self.project_info["projectID"] and \
               int(request["to_be_member"]) == student_id and \
               not request["response"]:
                print("You have already invited this student.")

            if request["projectID"] == self.project_info["projectID"] and \
               self.project_info["member1"] == student_id:
                print("This student is already a member of your project.")

        return student_id

    def send_request_advisor(self):
        pass
