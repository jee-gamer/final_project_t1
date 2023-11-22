

class Student:
    def __init__(self, ID, request_table):
        self.ID = ID
        request = []
        print(request_table)
        for r in request_table:
            if r['to_be_member'] == ID:
                request.append([r["projectID"], r["project_name"]])
        self.requests = request
        # This will be the ID of and title of projects
        self.project = ""

    def read_request(self):
        for ID, name in self.requests:
            print(f"You were invited to this project {name}, id: {ID}.")
        go_next = input("Do you want to accept/deny the request? (y/n): ")
        if go_next == "y":
            print("You can accept/deny/ignore these requests.")
            return self.answer_request()
        print("exiting.")

    def answer_request(self):
        copy_request = self.requests.copy()
        for ID, name in copy_request:
            print(f"You invited to this project {name}, id: {ID}.")
            accept = input("Your answer (y/n/i): ")
            if accept == "i":
                continue
            elif accept == "n":  # DONT FORGET TO CHANGE DATABASE
                self.requests.remove([ID, name])
            elif accept == "y":
                self.requests.clear()
                self.project = ID
                print(f"You have became a member of {name} project.")

                return ID  # return project ID if accept
        return None

    def update_request(self):
        # probably dont even need this because the student class get update every time someone log in
        pass

    def create_project(self):
        pass
        # dictionary = {"projectID": person["ID"],
        #               "title": f'{person["first"]}.{person["last"][0]}',
        #               "lead": str(random.randrange(1000, 10000)),
        #               "member1": person["type"],
        #               "member2": person["type"],
        #               "advisor": person["type"],
        #               "status": person["type"]
        #               }