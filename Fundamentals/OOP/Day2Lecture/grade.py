
class Grade:
    def __init__(self, topic, mark, student_name):
        self.topic = topic
        self.mark = mark
        self.student_name = student_name
    
    def print_info (self):
        print("Topic", self.topic)
        print("Grade", self.mark)
        print("Student", self.student_name) 
        return self

    def extra_points(self, percentage):
        current_grade = self.mark
        final_grade = current_grade + (current_grade * (percentage / 100)) 
        self.mark = final_grade
        return self

alex_grade = Grade("Web Fundamentals", 82.0, "Alex")
alex_grade.print_info()
alex_grade.extra_points(2)
alex_grade.print_info()

#to chain methods we need to return self reference, cannot chain methods if a method is already returning something
alex_grade.print_info().extra_points(2).print_info()