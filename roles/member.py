
class Member:
    def __init__(self, ID, request_table, info, project_info):
        self.ID = ID
        self.project_info = project_info
        self.request_table = request_table

    def check_project_status(self):
        print(f"The project status is {self.project_info['status']}\n")

    def modify_project(self):
        pass  # there is no real info in project table anyway?

    def view_project(self):
        print(self.project_info)

    def check_responses(self):
        request_list = []
        for request in self.request_table:
            if request["projectID"] == self.project_info["projectID"]:
                print(request)
                request_list.append(request)
        if not request_list:
            print("There are no request.\n")
