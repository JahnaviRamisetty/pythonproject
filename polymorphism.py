class Parrot:
    def fly(self):
        print("parrot can fly")
    def swim(self):
        print("parrot can't swim")

class Fish:
    def fly(self):
        print("fish can't fly")
    def swim(self):
        print("fish can swim")

def swimming_test(bird):
    bird.swim()

p=Parrot()
f=Fish()

swimming_test(f)
swimming_test(p)
