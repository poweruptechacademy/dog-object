

class Dog:
    color="brown"
    name="Rusty"
    favoriteToy ="frisbee"



    def __init__(self, name):
        self.name = name
        
    def bark(self):
        print("Woof! My name is " + self.name)


    def play(self):
        game = input("Will you play " + self.favoriteToy + " with me?")
        if game == "yes":
            print("Thanks, human!")


max = Dog("Max")
max.bark()

digger = Dog("Digger")
digger.favoriteToy="bone"
digger.bark()
digger.play()
