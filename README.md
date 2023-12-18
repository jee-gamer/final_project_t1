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

---
List of files description: <br />
There are 4 role files <br />
There are 6 roles <br />
most function in the class is just an action that can be done by that role.

1. Admin class - is in the project_manage
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
