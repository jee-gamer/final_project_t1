
class Faculty:
    def __init__(self, ID, info, advisor_table, evaluate_table):
        self.ID = ID
        request = []
        for r in advisor_table:
            if r['to_be_advisor'] == ID and not r['response']:
                # print(f"Project id = {r['projectID']}")
                request.append([r["projectID"], r["project_name"]])
        self.requests = request
        request = []
        for r in evaluate_table:
            if r['evaluator'] == ID and not r['status']:
                request.append([r["projectID"], r["project_name"]])
        self.evaluate_requests = request

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

    def read_evaluate_request(self):
        for ID, name in self.evaluate_requests:
            print()
            print(f"You were requested to evaluate project '{name}', id: {ID}."
                  )
        if not self.evaluate_requests:
            print("There are no requests.\n")
            return 0, 0
        go_next = input("Do you want to answer the requests? (y/n): ")
        if go_next == "y":
            print("\nYou can accept/deny/ignore these requests.")
            return self.answer_evaluate_request()
        elif go_next == "n":
            print("You refused to answer any requests\n")
            return 0, 0
        print("exiting.")

    def answer_evaluate_request(self):
        copy_request = self.evaluate_requests.copy()
        for ID, name in copy_request:
            print(f"You were requested to evaluate project '{name}', id: {ID}."
                  )
            accept = input("Your answer (y/n): ")
            if accept == "n":
                self.evaluate_requests.remove([ID, name])
                return -1, str(ID)
            elif accept == "y":
                return 1, str(ID)  # return project ID and 1 == accept

        print('returning none')
        return None

    def evaluate_project(self, ID, name):
        print("What do you think about this project?")
        feedback = input("Enter your feedback here: ")
        print("Do you approve this project?")
        accept = input("Your answer (y/n/): ")
        if accept == "n":
            self.evaluate_requests.remove([ID, name])
            return -1, str(ID)
        elif accept == "y":
            return 1, str(ID)  # return project ID and 1 == accept

