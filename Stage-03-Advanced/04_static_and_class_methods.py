class Student:
    count = 0

    @staticmethod
    def school_name():
        return "ABC High School"

    @classmethod
    def increase_count(cls):
        cls.count += 1
        return cls.count


print(Student.school_name())

print(Student.increase_count())
print(Student.increase_count())
print(Student.increase_count())

print("Total Students:", Student.count)