class Animal:
    def legs(self):
        print("I have four legs")
    def fur(self):
        print("My body is covered with fur")
class Domestic:
    def home(self):
        print("I am kept at home")
class Cow(Animal,Domestic):
    def meat(self):
        print("I offer meat")
    def milk(self):
        print("I give out milk")
d=Cow()
d.meat()
d.milk()
d.home()
d.legs()
d.fur()
