class Student:
    def __init__(self, name, age, marks):
        self._name = name
        self._age = age
        self._marks = marks

    def get_marks(self):
        return self._marks

    def get_age(self):
        return self._age

    def get_name(self):
        return self._name
