# class Human:
#     MAX_ENERGY = 100
#     def __init__(self):
#         self.name = "human"
#         self.age = 0
#         self.energy = Human.MAX_ENERGY
#     def display(self) :
#         print(f"I am {self.name}")
# if __name__ == "__main__":
#     Human = Human()
#     Human.display()

class robot:
    MAX_ENERGY = 100
    def __init__(self) :
        self.name = "robot"
        self.age = 0
        self.energy = robot.MAX_ENERGY
    def display(self) :
        print(f"I am {self.name}")
    def __str__(self):
        return (f"I am {self.name}, and I am {self.age} years old")
    def __repr__(self):
        return f"robot(name={self.name}, age={self.age})"

if __name__ == "__main__":
    robot = robot()

    print(robot)
    print(repr(robot))





