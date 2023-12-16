
class Member:
    def __init__(self, ID, info, request_table, project_info):
        self.ID = ID
        self.project_info = project_info[0]
        self.request_table = request_table

    def check_project_status(self):
        print(f"The project status is {self.project_info['status']}\n")

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
