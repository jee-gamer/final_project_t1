
class Faculty:
    def __init__(self, ID, info, advisor_table, evaluate_table,
                 assigned_table):
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
                request.append([r["projectID"], r["project_name"], 1])
            elif r['evaluator2'] == ID and not r['status']:
                request.append([r["projectID"], r["project_name"], 2])
        self.evaluate_requests = request

        assigned_project = []
        for r in assigned_table:
            if r['evaluator'] == ID and not r['status']:
                request.append([r["projectID"], r["project_name"], 1])
            elif r['evaluator2'] == ID and not r['status']:
                request.append([r["projectID"], r["project_name"], 2])
        self.assigned_project = assigned_project

    def read_request(self):
        for ID, name in self.requests:
            print()
            print(f"You were invited to project '{name}', id: {ID}.\n")
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
        for ID, name, _ in self.evaluate_requests:
            print()
            print(f"You were requested to evaluate project '{name}', id: {ID}."
                  f"\n"
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
        for ID, name, number in copy_request:  # number is order of evaluator
            print(f"You were requested to evaluate project '{name}', id: {ID}."
                  )

            accept = input("Your answer (y/n): ")
            if accept == "n":
                self.evaluate_requests.remove([ID, name, number])
                return -1, str(ID)
            elif accept == "y":
                return 1, str(ID)  # return project ID and 1 == accept

        return None

    def evaluate_project(self, ID, number):
        print("What do you think about this project?")
        feedback = input("Enter your feedback here: ")
        print("Please rate the project from 1-10. (Enter -1 if project fails.")
        while True:
            accept = input("Enter the score: ")
            if not isinstance(accept, int):
                print("The score can only be integers!")
                continue
            if accept < -1:
                print("Cannot give score lower than -1.")
                continue
            break

    # def read_accepted_request(self):
    #     for ID, name, _ in self.evaluate_requests:
    #         print()
    #         print(
    #             f"You were requested to evaluate project '{name}', id: {ID}."
    #             )
    #     if not self.evaluate_requests:
    #         print("There are no requests.\n")
    #         return 0, 0
    #     go_next = input("Do you want to answer the requests? (y/n): ")
    #     if go_next == "y":
    #         print("\nYou can accept/deny/ignore these requests.")
    #         return self.answer_evaluate_request()
    #     elif go_next == "n":
    #         print("You refused to answer any requests\n")
    #         return 0, 0
    #     print("exiting.")
    #
    #     return accept, str(ID), feedback, number  # return score and projectID


class Advisor(Faculty):
    def __init__(self, ID, info, advisor_table, evaluate_table,
                 assigned_table, proposal_table, report_table):
        super().__init__(ID, info, advisor_table, evaluate_table,
                         assigned_table)

        request = []
        for r in proposal_table:
            if r['advisor'] == ID and not r['response']:
                request.append([r["projectID"], r["project_name"]])
        self.proposal_request = request

        request = []
        for r in report_table:
            if r['advisor'] == ID and not r['response']:
                request.append([r["projectID"], r["project_name"]])
        self.report_request = request

    def read_proposal(self):
        for ID, name in self.proposal_request:
            print()
            print(f"You were requested to approve proposal of project"
                  f" '{name}', id: {ID}.\n")
        if not self.proposal_request:
            print("There are no requests.\n")
            return 0, 0
        go_next = input("Do you want to answer the requests? (y/n): ")
        if go_next == "y":
            print("\nYou can accept/deny/ignore these requests.")
            return self.answer_proposal()
        elif go_next == "n":
            print("You refused to answer any requests\n")
            return 0, 0
        print("exiting.")

    def answer_proposal(self):
        copy_request = self.proposal_request.copy()
        for ID, name in copy_request:
            print(f"You were requested to approve proposal of project"
                  f" '{name}', id: {ID}.")
            accept = input("Your answer (y/n/i): ")
            if accept == "i":
                continue
            elif accept == "n":
                self.proposal_request.remove([ID, name])
                return -1, str(ID)
            elif accept == "y":
                return 1, str(ID)  # return project ID and 1 == accept

        return None

    def read_report(self):
        for ID, name in self.report_request:
            print()
            print(f"You were requested to approve report of project"
                  f" '{name}', id: {ID}.\n")
        if not self.report_request:
            print("There are no requests.\n")
            return 0, 0
        go_next = input("Do you want to answer the requests? (y/n): ")
        if go_next == "y":
            print("\nYou can accept/deny/ignore these requests.")
            return self.answer_report()
        elif go_next == "n":
            print("You refused to answer any requests\n")
            return 0, 0
        print("exiting.")

    def answer_report(self):
        copy_request = self.report_request.copy()
        for ID, name in copy_request:
            print(f"You were requested to approve report of project"
                  f" '{name}', id: {ID}.")
            accept = input("Your answer (y/n/i): ")
            if accept == "i":
                continue
            elif accept == "n":
                self.report_request.remove([ID, name])
                return -1, str(ID)
            elif accept == "y":
                return 1, str(ID)  # return project ID and 1 == accept

        return None
