"""
NAME : Mburu Martin
ADM NO : BSCIT-05-0167/2024
Class Definition, Inheritance
"""

class Animal:
    def fur(self):
        return f"I have fur all over my body."

class Dog(Animal):
    def bark(self):
        return f"Dog Barking."

class Puppy(Dog):
    def play(self):
        return f"I play all the time."

#Object Creation
bosco = Puppy()
print(bosco.fur())
print(bosco.bark())
print(bosco.play())
