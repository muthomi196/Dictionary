class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, I am {self.name}. I am {self.age} years old and I identify as {self.gender}.")

# create an instance of the Person class
person = Person("John Doe", 30, "male")

# call the introduce method to introduce the person
person.introduce()