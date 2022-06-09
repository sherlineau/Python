
class Grade:
    def __init__(self, topic, mark, student_name):
        self.topic = topic
        self.mark = mark
        self.student_name = student_name
    
    def print_info (self):
        print("Topic", self.topic)
        print("Grade", self.mark)
        return self

    def extra_points(self, percentage):
        current_grade = self.mark
        final_grade = current_grade + (current_grade * (percentage / 100)) 
        self.mark = final_grade
        return self


class Student:
    #class attributes
    bootcamp = "Coding Dojo"
    list_students = []

    # Constructor - constructing objects
    def __init__(self, first_name, last_name, instructor, current_stack, mark):
        # attributes - accessible in the entire class
        self.first_name = first_name
        self.last_name = last_name
        self.instructor = instructor
        self.current_stack = current_stack
        self.grade = Grade( current_stack, mark, first_name )
        # this line adds the instances that is created to the list of students list_students
        Student.list_students.append( self )
    
    #Methods
    def print_student_info ( self ):
        print("First name", self.first_name)
        print("Last name", self.last_name)
        print("Instructor", self.instructor)
        print("Current stack", self.current_stack)
        self.grade.print_info()

    def full_name ( self ):
        return self.first_name + " " + self.last_name


    # class methods reference to class itself 
    @classmethod            #v use cls to reference all instances of class
    def print_all_students( cls ):
        for student in cls.list_students: 
            # student represents an object
            print(student.full_name(), student.current_stack)

    @classmethod
    def change_stack_name(cls, new_stack):
        for student in cls.list_students:
            student.current_stack = new_stack


    # static method will not have a reference to instances or class itself
    # used when accessing class or instance is not required
    # requires developers to provide parameters
    # basically has no access to any of the class attributes or instance attributes
    @staticmethod
    def add_two_numbers ( num1, num2):
        return num1 + num2;

alexander = Student( "Alexander" , "Miller" , "Alfredo", "Python/Flask", 8.2)
martha = Student( "Martha", "Smith", "Amanda", "Web Fundamentals", 9.1)
roger = Student( "Roger", "Smith", "Tyler", "Java", 7.9)
anna = Student( "Anna", "Smith", "Nicole", "Web Fundamentals", 8.5)

print(Student.list_students)
# Student.print_all_students()
# Student.change_stack_name("MERN")
# Student.print_all_students()

# alexander.print_student_info()

# alexander = Student( "Alexander" , "Miller" , "Alfredo", "Python/Flask")
# #alexander.print_student_info()
# print(f"{alexander.first_name}'s instructor is {alexander.instructor}")

# martha = Student( "Martha", "Smith", "Amanda", "Web Fundamentals")
# #martha.print_student_info()

# name = alexander.full_name()
# print( name )