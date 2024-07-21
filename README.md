Educational Management System Documentation
Educational Management System
GitHub Repository: https://github.com/omarEssam-11/Educational-Management-System
Table of Contents
1. Introduction
2. Installation
3. Usage Guide
 - Logging In
 - Student Functionalities
 - Doctor Functionalities
4. Code Structure
5. Classes and Methods
6. Example Usage
1. Introduction
The Educational Management System is a Python-based project designed to facilitate the
management of educational courses, assignments, and student enrollments. The system provides
functionalities for both students and doctors (professors) to manage their academic activities
efficiently.
2. Installation
To get started with the Educational Management System, clone the repository from GitHub and
navigate to the project directory:
Educational Management System Documentation
```bash
git clone https://github.com/omarEssam-11/Educational-Management-System.git
cd Educational-Management-System
```
Ensure you have Python installed on your system. The system does not require any external
libraries beyond the Python standard library.
3. Usage Guide
#### Logging In
1. **Start the system** by running the main script:
 ```bash
 python main.py
 ```
2. **Choose an option**:
 - Login
 - Sign up
 - Shutdown system
#### Student Functionalities
- **Register in Course**: View available courses and register.
- **List My Courses**: View all registered courses.
- **View Course**: View details of a specific course, including assignments.
- **Submit Solution**: Submit solutions for assignments.
- **Grades Report**: View grades for assignments.
Educational Management System Documentation
#### Doctor Functionalities
- **List Courses**: View all courses taught by the doctor.
- **Create Course**: Create a new course.
- **View Course**: View details of a specific course, including assignments.
- **Create Assignment**: Add assignments to courses.
- **View Assignment**: View, grade, and comment on student submissions.
4. Code Structure
The main classes and methods in the code are:
- **User (ABC)**
 - Attributes: `username`, `password`, `ID`, `email`, `full_name`
- **Student (User)**
 - Additional Attributes: `registered_courses`, `list_of_assignments`
 - Methods: `register_in_course()`, `list_my_courses()`, `unregister_from_course()`,
`generate_student_assignments()`, `course_report()`, `submit_solution()`, `view_course()`,
`get_all_grades()`, `grades_report()`, `create_new_student()`, `menu()`
- **Doctor (User)**
 - Additional Attributes: `courses`
 - Methods: `add_assignment_for_students()`, `list_courses()`, `create_assignment()`,
`view_assignment()`, `set_grade()`, `set_comment()`, `get_all_assignments()`, `list_assignments()`,
`get_assignment_students()`, `get_assignment_from_assignemntsList_for_student()`,
`show_grades_report()`, `show_assignment_info()`, `list_solutions()`, `view_solutions()`,
`create_course()`, `create_new_doctor()`, `menu()`
- **Course**
Educational Management System Documentation
 - Attributes: `name`, `code`, `doctor_name`, `student_ids`, `assignments`
- **Assignment**
 - Attributes: `assignment_id`, `name`, `grade`, `status`, `comments`, `maximum_grade`,
`description`
 - Methods: `push_solution()`
5. Classes and Methods
- **User (ABC)**
 - Attributes: `username`, `password`, `ID`, `email`, `full_name`
- **Student (User)**
 - Additional Attributes: `registered_courses`, `list_of_assignments`
 - Methods: `register_in_course()`, `list_my_courses()`, `unregister_from_course()`,
`generate_student_assignments()`, `course_report()`, `submit_solution()`, `view_course()`,
`get_all_grades()`, `grades_report()`, `create_new_student()`, `menu()`
- **Doctor (User)**
 - Additional Attributes: `courses`
 - Methods: `add_assignment_for_students()`, `list_courses()`, `create_assignment()`,
`view_assignment()`, `set_grade()`, `set_comment()`, `get_all_assignments()`, `list_assignments()`,
`get_assignment_students()`, `get_assignment_from_assignemntsList_for_student()`,
`show_grades_report()`, `show_assignment_info()`, `list_solutions()`, `view_solutions()`,
`create_course()`, `create_new_doctor()`, `menu()`
- **Course**
 - Attributes: `name`, `code`, `doctor_name`, `student_ids`, `assignments`
- **Assignment**
 - Attributes: `assignment_id`, `name`, `grade`, `status`, `comments`, `maximum_grade`,
Educational Management System Documentation
`description`
 - Methods: `push_solution()`
6. Example Usage
#### Creating a new student and registering in a course:
```python
Student.create_new_student('john_doe', 'password123', '123456', 'John Doe', 'john@example.com')
student = [s for s in all_students if s.username == 'john_doe'][0]
student.register_in_course()
```
#### Creating a new doctor and adding an assignment:
```python
Doctor.create_new_doctor('dr_smith', 'password123', '654321', 'Dr. Smith', 'smith@example.com')
doctor = [d for d in all_doctors if d.username == 'dr_smith'][0]
doctor.create_course()
doctor.create_assignment('CS101', 'Assignment 1', 'Description of Assignment 1', 100)
```
