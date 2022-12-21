class one:
    def __init__(self,hr,dev):
        self.humanresource = hr
        self.developer = dev
class dept(one):
    pass
    def description(self):
        print(self.humanresource,self.developer)
a=dept("alpha","beta")
a.description()
