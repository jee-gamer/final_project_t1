All faculty must evaluate the project before a project is approved.

make new table
 - pending_project
    - this table has the following keys
        - projectID
        - projectname
        - advisor
        - feedback (None, by faculties)
        - status (0-numbers of approval) 
            - if the number of approval reach the number of faculty then the project is considered approved
            - every time a faculty approve a project it adds the number of approval by 1
            - if a faculty already approve a project the next time they check it wont be seen
            - everything reset if the project is denied and then send again
            - delete the old pending_project if a sending a new one.
 
faculty can deny your project and gave feedback. The project members must make
changes on their project and request for approval again.


