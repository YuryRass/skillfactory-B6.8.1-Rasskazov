class Cat:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
    def print_info(self):
        print ("Имя: ", self.name)
        print ("Пол: ", self.gender)
        print ("Возраст: ", self.age)
        print("-" * 10)
    