from person import Person
# from folder_name.filename import Class

class Student( Person ):
    
    def __init__(self, first_name, last_name, age, instructor, current_stack ):
        #super() executes parent class "Person" constructor and initializes those attributes
        super().__init__(first_name, last_name, age)
        self.instructor = instructor
        self.current_stack = current_stack

alex = Student("Alex" , "Miller", 20, "Nicole", "Web Fundamentals")
alex.print_info()

