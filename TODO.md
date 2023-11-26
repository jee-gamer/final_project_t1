* An admin
  - function
  - add_table(name)
  - create_table(name)
  - manage_database()

* A student
  - function
  - read_request() and answer_request()
  - create_project(name)
    - update role to lead
    - instant re-log in or instant action
  
* A lead Student
  - function
  - create_project(name)
  - send_invite(person) and send_invite(advisor)
    - update the project and request table
  - modify_project()
    - change name
    - kick members
    - else
    - update relating table
  - submit_final_report()

* A member
  - function
  - check_project_status()
  - modify_project()
    - anything a member should be able to do
    - update the project table
  - check_responses()
    - like lead student

* A faculty
  - function
  - read_request() and answer_request()
    - function the same as student
    - also receive detail of project
    - update project table and request table
    - if accept one then update (deny) other request in table
    - update role to advisor
    
* A project advisor
  - function
  - approve_project()
  - no idea about anything else

