class School:
    def __init__(self, name: str, nickname: str, address: str, principal: str, teachers: list, students: list, classrooms: list, library: bool):
        self.name = name
        self.nickname = nickname
        self.address = address
        self.principal = principal
        self.teachers = teachers
        self.students = students
        self.classrooms = classrooms
        self.library = library

    class Principal:
        def __init__(self, name: str, age: int, yearsExperience: int, isHere: bool, hobbies: list, strict: bool):
            self.name = name
            self.age = age
            self.yearsExperience = yearsExperience
            self.isHere = isHere
            self.hobbies = hobbies
            self.strict = strict

    class Teacher:
        def __init__(self, name: str, age: int, subject: str, classes: list, isHere: bool, hobbies: list, strict: bool):
            self.name = name
            self.age = age
            self.subject = subject
            self.classes = classes
            self.isHere = isHere
            self.hobbies = hobbies
            self.strict = strict

    class Student:
            def __init__(self, name: str, age: int, grade: str, classroom: str, classes: list, isHere: bool, extracurriculars: list, hobbies: list, smart: bool):
                self.name = name
                self.age = age
                self.grade = grade
                self.classroom = classroom
                self.classes = classes
                self.isHere = isHere
                self.extracurriculars = extracurriculars
                self.hobbies = hobbies
                self.smart = smart
    class Classroom:
            def __init__(self, roomNumber: str, subject: str, teacher: str, students: list, resources: list, isAvailable: bool):
                self.roomNumber = roomNumber
                self.subject = subject
                self.teacher = teacher
                self.students = students
                self.resources = resources
                self.isAvailable = isAvailable
    class Library:
            def __init__(self, location: str, books: list, isOpen: bool, librarian: str, resources: list):
                self.location = location
                self.books = books
                self.isOpen = isOpen
                self.librarian = librarian
                self.resources = resources

crb = School(
    name="Charles R. Beaudoin",
    nickname="CRB",
    address="4313 Clubview Dr, Burlington, ON L7M 5A1",
    principal="Mr.Donaldson",
    teachers=["Ms.Rodriguez", "Mrs.Nagy", "Mrs.Bailey"],
    students=["Arja", "Yazid", "Kiash", "Janet", "Zackery", "Arlo", "Riaan", "Joshua", "Gabriel", "Nahyan", "Kaushal", "Amelia", "Avy", "Liv", "Sohum", "Arna", "Finn", "Ava", "Evander", "Kaveer", "Sarah", "James", "Hannah", "Sophie"],
    classrooms=["SG1J", "SG2J", "SG3J", "SG1I"],
    library=True
)

Kaushal = School.Student(
    name="Kaushal Murugan",
    age=10,
    grade="5",
    classroom="SG1J",
    classes=["Math", "Literacy", "Music", "Art", "Phys. Ed.", "French", "Social Studies", "Science", "Library", "Health"],
    isHere=True,
    extracurriculars=["Coding Club", "Cubing Club", "Equity Club"],
    hobbies=["Coding", "Reading", "Cubing", "Playing Chess", "Playing Video Games", "Drawing"],
    smart=True

)

print(f"Welcome to {crb.name}, or {crb.nickname}, {Kaushal.name}!\nYou are in class {Kaushal.classroom} and you are taking {len(Kaushal.classes)} classes this year!")