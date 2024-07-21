from abc import ABC
class User(ABC):
    def __init__(self, username: str, password: str, ID, email: str, full_name: str):
        self.username = username
        self.password = password
        self.ID = ID
        self.email = email
        self.full_name = full_name

class Student(User):
    def __init__(self, username, password, ID, full_name, email, registered_courses=None):
        super().__init__(username, password, ID, email, full_name)
        self.registered_courses = registered_courses
        self.list_of_assignments = {}

    def register_in_course(self):
        print("Below are the courses available for you to register\nPlease enter course number you wish to register:")
        # available_courses = [all_courses not in self.registered_courses]
        if self.registered_courses is None:
            self.registered_courses = []
        available_courses = [course for course in all_courses.keys() if course not in self.registered_courses]
        for index, c in enumerate(available_courses):
            print(f"{index + 1}) {c}")

        course_to_register = int(input("Enter course number: ")) - 1
        self.registered_courses.append(available_courses[course_to_register])
        all_courses[available_courses[course_to_register]].student_ids.append(self.ID)
        answer = input("You have successfully registered\nDo you want to Back to main menu? (y / n)")
        if answer == "y":
            self.menu()

    def list_my_courses(self):
        if self.registered_courses == None:
            print("No courses to view")
            self.menu()
        print("Here are the courses you are currently registered : ")
        for index, course in enumerate(self.registered_courses):
            print(f"{index + 1}) {all_courses[course].name} : {all_courses[course].code}")

        answer = input("Do you want to Back to main menu ? (y / n): ")
        if answer == "y":
            self.menu()

    def unregister_from_course(self, course):
        self.registered_courses.remove(course.code)
        all_courses[course.code].student_ids.remove(self.ID)
        print("You have successfully unregistered from the course")
        answer = input("Do you want to go to main menu ? enter (y): ")
        if answer == "y":
            self.menu()

    def generate_student_assignments(self):
        for course in self.registered_courses:
            if course in course_assignments:
                self.list_of_assignments[course] = [Assignment(assignment.assignment_id, assignment.name) for assignment
                                                    in course_assignments[course]]

    def course_report(self, course):
        if self.registered_courses == None:
            print("No courses")
            self.menu()
        self.generate_student_assignments()
        print(
            f"course {course.name}, code {course.code}, taught by {course.doctor_name}\ncourse has {len(course.assignments)} assignments")
        for idx, assignment in enumerate(self.list_of_assignments[course.code]):
            print(f"{idx + 1}) {assignment.name}  {assignment.status}  {assignment.grade}")


    def submit_solution(self, assignment, solution):
        assignment.solution = solution
        assignment.push_solution(self, solution)
        assignment.status = "Submitted"
        answer = input("You have successfully Submitted your solution\nDo you want to Back to main menu? (y / n)")
        if answer == "y":
            self.menu()

    def view_course(self):
        print("Here are the courses you are currently registered on : ")
        for index, course in enumerate(self.registered_courses):
            print(f"{index + 1}) {all_courses[course].name}  {course}")

        course_index = int(input("Enter course number: ")) - 1
        course_to_view = all_courses[self.registered_courses[course_index]]
        self.course_report(course_to_view)
        print("please make a choice: \n1) unregister from course\n2) submit solution\n3) Back\n4) back to main menu")
        answer = int(input(""))
        if answer == 1:
            self.unregister_from_course(course_to_view)
        elif answer == 2:
            assignment_index = int(input("which assignment to submit solution for ?\nEnter your choice: ")) - 1
            assignment_to_be_submitted = self.list_of_assignments[course_to_view.code][assignment_index]
            content_of_submission = input("Please Enter the solution:\n").strip()
            self.submit_solution(assignment_to_be_submitted, content_of_submission)
        elif answer == 3:
            self.view_course()

        elif answer == 4:
            self.menu()

    def get_all_grades(self, course_code):
        all_grades = 0
        maximum_grades = 0
        if self.registered_courses is None:
            print("No courses")
            self.menu()
        self.generate_student_assignments()

        for assignment in self.list_of_assignments[course_code]:
            maximum_grades += assignment.maximum_grade

        for assignment in self.list_of_assignments[course_code]:
            if assignment.grade != '':
                all_grades += int(assignment.grade)

        return f"{all_grades} / {maximum_grades}"

    def grades_report(self):
        self.generate_student_assignments()
        if self.list_of_assignments is None:
            print("No assignments")
            self.menu()
        for course_code, assignments_list in self.list_of_assignments.items():
            total_submissions = len([assignment for assignment in assignments_list if assignment.status == 'Submitted'])
            course_grade_report = self.get_all_grades(course_code)
            print(
                f"Course code {course_code} - total submissions: {total_submissions} assignments - grade: {course_grade_report} (till now)")

        answer = input("Do you want to go back to the main menu? (y / n): ")
        if answer.lower() == "y":
            self.menu()

    @staticmethod
    def create_new_student(usr_name, usr_password, id, full_name, email):
        new_student = Student(usr_name, usr_password, id, full_name, email)
        print("sign up for student has been done successfully")
        all_students.append(new_student)
        new_student.menu()

    def menu(self):
        print(f"Welcome {self.full_name}. You are logged in")
        print(
            "\nPlease make a Choice : \n(1) Register in course\n(2) List my courses\n(3) View course\n(4) Grades Report\n(5) Log out")
        choice = int(input("\nEnter your Choice : "))

        if choice == 1:
            self.register_in_course()
        elif choice == 2:
            self.list_my_courses()
        elif choice == 3:
            self.view_course()
        elif choice == 4:
            self.grades_report()
        elif choice == 5:
            main()

class Course:
    def __init__(self, name, code, doctor_name, student_ids=None):
        self.name = name
        self.code = code
        self.doctor_name = doctor_name
        self.student_ids = student_ids
        self.assignments = course_assignments[self.code]


class Assignment:
    def __init__(self, assignment_id, name, grade='', status="Not Submitted", comments='', maximum_grade=0, description=''):
        self.assignment_id = assignment_id
        self.name = name
        self.grade = grade
        self.status = status
        self.solution = ""
        self.comments = comments
        self.maximum_grade = maximum_grade
        self.description = description

    def push_solution(self, student, solution):
        all_students_solutions[self.assignment_id][student.ID] = solution


class Doctor(User):

    def __init__(self, username, password, doctor_id, full_name, email, courses=[]):
        super().__init__(username, password, doctor_id, email, full_name)
        self.courses = courses

    def add_assignment_for_students(self, course_code, assignment):
        students = [student for student in all_students if course_code in student.registered_courses]

        for student in students:
            if course_code not in student.list_of_assignments:
                student.list_of_assignments[course_code] = []

            student.list_of_assignments[course_code].append(assignment)

    def list_courses(self):
        dr_courses = []
        for c in self.courses:
            if c in all_courses:
                dr_courses.append(all_courses[c])

        for idx, dr_course in enumerate(dr_courses):
            print(f"{idx+1}) course name :{dr_course.name} and course code:{dr_course.code}")

    def create_assignment(self, course_code, assignment_title, assignment_description, assignment_maximum_grade):
        new_assignment_id = course_code + "-" + assignment_title
        new_assignment = Assignment(assignment_id=new_assignment_id, name=assignment_title, maximum_grade=assignment_maximum_grade, description=assignment_description)
        course_assignments[course_code].append(new_assignment)
        self.add_assignment_for_students(course_code, new_assignment)


    def view_assignment(self, assignment, course_code=''):
        print("1)Show Info\n2)Show Grades Report\n3)List Solutions\n4)View Solution\n5)Back")
        choice = int(input(""))
        if choice == 1:
            self.show_assignment_info(assignment)
        elif choice == 2:
            self.show_grades_report(course_code, assignment)
        elif choice == 3:
            self.list_solutions(assignment)
        elif choice == 4:
            self.view_solutions(assignment)
        elif choice == 5:
            self.menu()

    def set_grade(self, assignment, grade):
        assignment.grade = grade


    def set_comment(self, assignment, comment):
        assignment.comments = comment


    def get_all_assignments(self, course_code):
        return course_assignments[course_code]

    def list_assignments(self, course_code):
        all_assignments = self.get_all_assignments(course_code)
        for idx, assignment in enumerate(all_assignments):
            print(f"{idx+1}) assignment title:{assignment.name} and assignment id:{assignment.assignment_id}")


    def get_assignment_students(self, assignment):
        students_ids = [all_students_solutions[assignment.assignment_id].keys()]  ##check this
        students = []
        for stu in all_students:
            if stu.ID in students_ids:
                students.append(stu)

        return students

    def get_assignment_from_assignemntsList_for_student(self, student, course_code, assignment):
        for a in student.list_of_assignments[course_code]:
            if a.assignment_id == assignment.assignment_id:
                return a

    def show_grades_report(self, course_code, assignment):
        students = self.get_assignment_students(assignment)
        for student in students:
            print(f"{student.full_name} grade = {(self.get_assignment_from_assignemntsList_for_student(student, course_code, assignment).grade)}")

    def show_assignment_info(self, assignment):
        print(f"Assignment title is {assignment.name} and assignment id is {assignment.assignment_id}\n Assignment description is {assignment.description}")


    def list_solutions(self, assignment):
        for idx, (k, v) in enumerate(all_students_solutions[assignment.assignment_id].items()):
            print(f"{idx + 1}) {k} : {v}")

    def view_solutions(self, assignment):
        self.list_solutions(assignment)
        sols_keys = list(all_students_solutions[assignment.assignment_id].keys())
        sol_index = int(input("please Enter The solution number you want to view: ")) -1
        solution_to_view = all_students_solutions[assignment.assignment_id][sols_keys[sol_index]]
        print("1)Show Info\n2)Set Grade\n3)Set a Comment\n4)Back")
        choice = int(input("please Enter The Choice : "))
        if choice == 1:
            print(solution_to_view)
        elif choice == 2:
            grade_to_set = int(input("please Enter The Grade : "))
            self.set_grade(assignment, grade_to_set)
        elif choice == 3:
            comment = input("please Enter The Comment : ")
            self.set_comment(assignment, comment)

        elif choice == 4:
            self.view_assignment(assignment)


    def create_course(self):
        course_name = input("please enter the name of the course : ").strip()
        course_code = input("please enter the course code : ").strip()

        # Initialize the course_assignments dictionary entry for the new course
        if course_code not in course_assignments:
            course_assignments[course_code] = []

        course = Course(name=course_name, code=course_code, doctor_name=self.full_name)
        all_courses[course_code] = course
        self.courses.append(course_code)

    @staticmethod
    def create_new_doctor(usr_name, usr_password, doctor_id, full_name, email):
        new_doctor = Doctor(usr_name, usr_password, doctor_id, full_name, email)
        all_doctors.append(new_doctor)
        print("sign up successful")
        new_doctor.menu()



    def menu(self):

        print(f"Welcome Dr {self.full_name}. You are logged in")
        print("\nPlease make a Choice : \n(1) List Courses\n(2) Create course\n(3) View course\n(4) Log out")
        choice = int(input("\nEnter your Choice : "))

        if choice == 1:
            self.list_courses()
            print("would you like to back to main menu enter y to go back to main menu")
            return_to_main_menu = input("").strip()
            if return_to_main_menu == "y":
                self.menu()

        elif choice == 2:
            self.create_course()

        elif choice == 3:
            for idx, course in enumerate(self.courses):
                print(f"{idx+1}) {course}")
            course_to_view_index = int(input("which course would you like to view: ")) -1
            course_to_view_code = self.courses[course_to_view_index]

            print("1) List Assignments\n2) Create Assignment\n3) View Assignment\n4) Back")

            view_course_choice = int(input("\nEnter your Choice : "))

            if view_course_choice == 1:
                self.list_assignments(course_to_view_code)

            elif view_course_choice == 2:
                print("please enter the following info to create the assignment :")
                new_assignment_course_code = input("\nEnter the course code of the new assignment: ").strip()
                new_assignment_title = input("\nEnter the title of the new assignment: ").strip()
                new_assignment_description = input("\nEnter the description of the new assignment: ").strip()
                new_assignment_maximum_grade = input("\nEnter the maximum grade of the new assignment: ").strip()
                self.create_assignment(new_assignment_course_code, new_assignment_title, new_assignment_description, new_assignment_maximum_grade)
                print("Assignment has been successfully created\nwould you like to back to main menu enter y to go back to main menu")
                return_to_main_menu = input("").strip()
                if return_to_main_menu == "y":
                    self.menu()

            elif view_course_choice == 3:
                print("here are all the assignments for this course:")
                self.list_assignments(course_to_view_code)
                assignment_to_view_index = int(input("\nchoose which assignment you would like to view: ")) -1
                assignment_to_view = self.get_all_assignments(course_to_view_code)[assignment_to_view_index]
                self.view_assignment(assignment=assignment_to_view, course_code=course_to_view_code)

            elif choice == 4:
                self.menu()

        elif choice == 4:
            main()

        print("would you like to back to main menu enter y to go back to main menu")
        return_to_main_menu = input("").strip()
        if return_to_main_menu == "y":
            self.menu()


all_doctors = [
    Doctor(full_name='Samy', email='Samy11@yahoo.com', username='dr_samy',password='123', doctor_id='100', courses=['CS111']),
    Doctor(full_name='Ashraf', email='Ashraf11@yahoo.com', username='dr_ashraf',password='123', doctor_id='200', courses=['CS113']),
    Doctor(full_name='Hani', email='Hani@yahoo.com', username='dr_hani',password='123', doctor_id='300', courses=['CS333']),
    Doctor(full_name='Hussien', email='Hussien@yahoo.com', username='dr_hussien',password='123', doctor_id='400', courses=['CS240']),
]


course_assignments = {
    'CS111': [Assignment('CS111-Assignment-1', 'Assignment-1', maximum_grade=10), Assignment('CS111-Assignment-2', 'Assignment-2', maximum_grade=10),
              Assignment('CS111-Assignment-3', 'Assignment-3', maximum_grade=20)],
    'CS333': [Assignment('CS333-Assignment-1', 'Assignment-1', maximum_grade=15)],
    'CS240': [Assignment('CS240-Assignment-1', 'Assignment-1', maximum_grade=25), Assignment('CS240-Assignment-2', 'Assignment-2', maximum_grade=5),
              Assignment('CS240-Assignment-3', 'Assignment-3', maximum_grade=20)],
    'CS113': []
}


all_students_solutions = {
    'CS111-Assignment-1': {
        "00102345": "10 * 15 = 150",
        "00204690": "bla bla bla",
    },
    'CS111-Assignment-2': {},
    'CS111-Assignment-3': {
        "00409380": "10 * 15 = 150",
        "00102345": "bla bla bla",
        "00204690": "bla bla bla"
    },
    'CS333-Assignment-2': {},
    'CS240-Assignment-1': {},
    'CS240-Assignment-2': {},
    'CS240-Assignment-3': {},
}


all_courses = {
    'CS111': Course("Prog 1", "CS111", "Dr. Samy",
                    ["00102345", "00204690", "00409380"]),
    'CS113': Course("Math 1", "CS113", "Dr. Ashraf",
                    ["00102345", "00204690"]),
    'CS333': Course("Math 2", "CS333", "Dr. Hani",
                    ["00102345", "00409380"]),
    'CS240': Course("Stat 1", "CS240", "Dr. Hussien",
                    ["00409380"]),

}


all_students = [
    Student(full_name='Hussien Samy', ID='00102345',
            registered_courses=['CS111', 'CS113', 'CS333'], email='hussien@gmail.com',
            username='s001', password='11111'),
    Student(full_name='Ashraf Sayed', ID='00204690',
            registered_courses=['CS111', 'CS113'],
            email='hussien@gmail.com', username='s002', password='22222'),
    Student(full_name='Ali Mohamed', ID='00409380',
            registered_courses=['CS111', 'CS333', 'CS240'], email='hussien@gmail.com',
            username='s004', password='44444'),

]


def main():

    # global user_type, user
    print("Please make a Choice : \n(1) login\n(2) sign up\n(3) shutdown system")
    operation_type = int(input("\nEnter your Choice : "))

    if operation_type == 1:
        print("Please make a Choice : \n(1) Student\n(2) Doctor")
        user_type = int(input("\nEnter your Choice : "))
        print("Enter your username and password")
        usr_name = input("user name : ")
        usr_password = input("password : ")
        user = None
        if user_type == 1:
            for stu in all_students:
                if usr_name == stu.username and usr_password == stu.password:
                    user = stu
                    break
            if user is None:
                print("Invalid")
                main()
            user.menu()
        elif user_type == 2:
            for dr in all_doctors:
                if dr.username == usr_name and dr.password == usr_password:
                    user = dr
            if user is None:
                print("Invalid")
                main()
            user.menu()

    elif operation_type == 2:
        print("Please make a Choice : \n(1) Student\n(2) Doctor")
        user_type = int(input("\nEnter your Choice : "))
        usr_name = input("user name : ").strip()
        usr_password = input("password : ").strip()
        full_name = input("full name : ").strip()
        usr_id = input("id : ").strip()
        email = input("email : ").strip()
        if user_type == 1:
            Student.create_new_student(usr_name, usr_password, usr_id, full_name, email)
        elif user_type == 2:
            Doctor.create_new_doctor(usr_name, usr_password, usr_id, full_name, email)

    elif operation_type == 3:
        return 0

main()