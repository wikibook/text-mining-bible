class Dog:
    """개의 특성과 행동을 위한 클래스"""
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name + " is now sitting.")
    def roll_over(self):
        print(self.name + " rolled over!")
