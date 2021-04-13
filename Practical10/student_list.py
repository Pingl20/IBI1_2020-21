# make class
class Student(object):
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.programme = None

    # define the functions
    def set_first_name(self, FirstName):
        self.first_name = FirstName

    def set_last_name(self, LastName):
        self.last_name = LastName

    def set_programme(self, Programme):
        if Programme in ["BMI", "BMS"]:
            self.programme = Programme
        else:
            self.programme = "Programme can only be BMI or BMS"

    # define the form of print
    def data(self):
        print("Student's full name is " + self.first_name + " " +
              self.last_name + " and the undergraduate programme is "
              + self.programme + ".")

# example
student1 = Student()
student1.set_first_name("Hua")
student1.set_last_name("Li")
student1.set_programme("BMS")
student1.data()