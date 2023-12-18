# Final project for 2023's 219114/115 Programming I

How to use: <br />
1.Log in by running the file project_manage.py <br />
2.Enter the username and password. <br />
3.Choose action from various choice <br />
4.Log out and save the changes by choosing the "Exit" choice.
(warning. If you don't choose the "Exit" choice, the changes won't be saved.)

Advisor is a subclass of Faculty
and is in the same file

Being a Faculty means you don't advise any project. <br />
so normally every faculty should be an advisor. <br />
an Advisor can advise multiple project at once. <br />
an Advisor and a Faculty can evaluate multiple project at once. <br />

There are 2 faculty/advisor needed for evaluation.

A faculty/advisor can read multiple request at once but can only accept one at a time. <br />
Also can only evaluate one project at a time (as in one per action)

for project to pass. It needs atleast 1 score out of 10 for both evaluator <br />
(yes it's really bad score, but atleast you pass right?) <br />
evaluator can only give score of 1-10 or <br /> 
-1 if reject the project

---
List of files description: <br />
There are 4 role files <br />
There are 6 roles <br />
most function in the class is just an action that can be done by that role.

1. Admin class - is in the project_manage
   (since admin needs direct Database modification, it is located in project_manage for easier use.)
- can update table, clear table, insert row, remove row
2. Student class - is in roles folder
- can read and accept project request and become member of project
- can create a project after rejecting all his request
3. Lead class - is in roles folder
- can view project, modify project, kick members
- can check project status
- can send proposal, report, evaluation requests
- can check invitation responses
- can invite student and advisor to the project

4. Member class - is in roles folder
- can check project status, view project
- can check invitation responses

5. Faculty class - is in roles folder, faculty.py
- can read/answer project request
- can read/answer evaluation requests
- can evaluate project

6. Advisor class - is in roles folder, faculty.py, is a subclass of Faculty
- can read/answer project proposal
- can read/answer project report
- in the program, can choose to go to faculty menu.

Most bugs is taken care of. <br />
I tested most scenarios but not all. <br />
so any bugs that is found is a new bug I haven't discovered before. <br />
There is no missing feature. <br />
Keep in mind that when the lead send project proposal, report, evaluation, it checks for the project status such as "ready for report" when trying to send report.

The table of each role and action:
(be mindful that not every action is done by just one function in the table, most has to return value back to the project_manage.py and let it access and modify the database.)

|  Role   |                    Action                     |           Method           |      Class      | Completion percentage |
|:-------:|:---------------------------------------------:|:--------------------------:|:---------------:|:---------------------:|
|  Admin  |    Update table (choose row choose column)    | choose_table, update_table |      Table      |         100%          |
|  Admin  |                  Clear table                  | choose_table, clear_table  |      Table      |         100%          |
|  Admin  |               Insert data (row)               |  choose_table, insert_row  |      Table      |         100%          |
|  Admin  |                  Delete row                   |  choose_table, delete_row  |      Table      |         100%          |
| Student |                Check requests                 |        read_request        |     Student     |         100%          |
| Student |                Create project                 |       create_project       |     Student     |         100%          |
| Member  |             Check project status              |    check_project_status    |     Member      |         100%          |
| Member  |              View project (info)              |        view_project        |     Member      |         100%          |
| Member  |            Check request responses            |      check_responses       |     Member      |         100%          |
|  Lead   |             Check project status              |    check_project_status    |      Lead       |         100%          |
|  Lead   |  Modify project (change name, kick members)   |       modify_project       |      Lead       |         100%          |
|  Lead   |            Check request responses            |      check_responses       |      Lead       |         100%          |
|  Lead   |               Request a member                |        send_request        |     Student     |         100%          |
|  Lead   |              Request an advisor               |    send_request_advisor    | Faculty/Advisor |         100%          |
|  Lead   |             Send project proposal             |       send_proposal        |     Advisor     |         100%          |
|  Lead   |              Send project report              |        send_report         |     Advisor     |         100%          |
|  Lead   |        Request for project evaluation         | request_project_evaluation | Faculty/Advisor |         100%          |
| Faculty |        Check requests (to be advisor)         |        read_request        |      Lead       |         100%          |
| Faculty |            Check evaluate requests            |   read_evaluate_request    |      Lead       |         100%          |
| Faculty |          Evaluated assigned projects          |      evaluate_project      |      Lead       |         100%          |
| Advisor |            Check proposal requests            |       read_proposal        |      Lead       |         100%          |
| Advisor |             Check report requests             |        read_report         |      Lead       |         100%          |
| Advisor | Go to faculty menu (log in as faculty 1 time) |            None            |     Faculty     |         100%          |









