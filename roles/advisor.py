
class Advisor:
    def __init__(self, ID, info, evaluate_table):
        self.ID = ID
        self.evaluate_table = evaluate_table

    def request_project_evaluation(self):
        for r in self.evaluate_table:
            if r['advisor'] == self.ID and r['status'] == "passed":
                print("This project is already passed\n")
                return None
        while True:
            print("You can choose your project's evaluator")
            chosen_ev = input("Enter your project's evaluator ID: ")
            try:
                chosen_ev = int(chosen_ev)
            except ValueError as e:
                print(e, "// evaluator_id must be integers!")
                continue
            if not chosen_ev:
                return None
            return str(chosen_ev)
