class Member():
    def __init__(self, full_name):
        self.full_name = full_name

    def introduce(self):
        print('Hi! My name is', self.full_name)


class Student(Member):
    def __init__(self, full_name, reason):
        super().__init__(full_name)
        self.reason = reason


class Instructor(Member):
    def __init__(self, full_name, bio):
        super().__init__(full_name)
        self.bio = bio
        self.skills = []

    def add_skill(self, skill):
        self.skills.append(skill)


class Workshop():
    def __init__(self, date, subject):
        self.date = date
        self.subject = subject
        self.instructors = []
        self.students = []

    def add_participant(self, participant):
        if "Student" in str(type(participant)):
            self.students.append(participant)
        else:
            self.instructors.append(participant)

    def print_details(self):
        print(self.subject, self.date)
        print('Students:')
        for i, stud in enumerate(self.students):
            print(i+1, stud.full_name, '-', stud.reason)
        print("Instructors:")
        for i, inst in enumerate(self.instructors):
            skillstr = ""
            for skill in inst.skills:
                skillstr += skill + " "
            print(i+1, inst.full_name, '-', skillstr)
            print("     ", inst.bio)


workshop = Workshop("12/03/2014", "Shutl")

jane = Student("Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")
vicky = Instructor("Vicky Python", "I want to help people learn coding.")
vicky.add_skill("HTML")
vicky.add_skill("JavaScript")
nicole = Instructor("Nicole McMillan", "I have been programming for 5 years in Python and want to spread the love")
nicole.add_skill("Python")

workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)
workshop.add_participant(nicole)
workshop.print_details()
