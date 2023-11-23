
class Student:
    def __init__(self, ID, request_table, info):
        # print(info)
        self.ID = ID
        request = []
        for r in request_table:
            if r['to_be_member'] == ID and not r['response']:
                # print(f"Project id = {r['projectID']}")
                request.append([r["projectID"], r["project_name"]])
        self.requests = request
        self.role = info[0]["role"]

    def read_request(self):
        for ID, name in self.requests:
            print()
            print(f"You were invited to project '{name}', id: {ID}.")
        if not self.requests:
            print("There are no requests.\n")
            return 0, 0
        go_next = input("Do you want to answer the requests? (y/n): ")
        if go_next == "y":
            print("\nYou can accept/deny/ignore these requests.")
            return self.answer_request()
        elif go_next == "n":
            print("You refused to answer any requests\n")
            return 0, 0
        print("exiting.")

    def answer_request(self):
        copy_request = self.requests.copy()
        for ID, name in copy_request:
            print(f"You were invited to project '{name}', id: {ID}.")
            accept = input("Your answer (y/n/i): ")
            if accept == "i":
                continue
            elif accept == "n":
                self.requests.remove([ID, name])
                return -1, str(ID)
            elif accept == "y":
                return 1, str(ID)  # return project ID and 1 == accept

        print('returning none')
        return None

    def create_project(self):
        if self.requests:
            print("You must deny all the request first to create a project.\n")
            return None
        if self.role != "student":
            print("You are not a student.\n")
            return None
        project_name = input("Enter your project title: ")
        project_dictionary = {"projectID": "2",  # need to random this
                              "title": project_name,
                              "lead": None,
                              "member1": None,
                              "member2": None,
                              "advisor": None,
                              "status": None
                              }
        return project_dictionary