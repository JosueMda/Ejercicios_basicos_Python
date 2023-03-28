class Person:
    def __init__(self,name,surname):
        self.name= name
        self.surname= surname
        
    def walk (self):
        print(f"{self.name} {self.surname} is walk")
        
myperson = Person("Josue", "Miranda")

print(myperson.name)
 