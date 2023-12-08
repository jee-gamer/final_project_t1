
class Advisor:
    def __init__(self, ID, info):
        self.ID = ID

    def request_project_evaluation(self):
        while True:
            print("You can choose your project's evaluator")
            chosen_advisor = input("Enter your project's evaluator ID: ")
            if not isinstance(chosen_advisor, int):
                print("The project evaluator ID must be integers!")
                continue
            if not chosen_advisor:
                return None
        return str(chosen_advisor)

