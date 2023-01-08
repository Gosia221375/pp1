class Student():
    id = 100000

    def __init__(self, name, surname, field_of_study):
        self.name = name
        self.surname = surname
        self.field_of_study = field_of_study
        self.id = Student.id
        Student.id +=1

    def __str__(self):
        return f"{self.name} {self.surname} ({Student.id}), {self.field_of_study}, UEK Kraków"

student1 = Student("Anna", "MAJ", "Applied Informatics")
print(student1)