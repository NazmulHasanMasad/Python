class Person:
    name="Anonymas"
#class method
    @classmethod
    def change_name(cls, name):
        cls.name=name


p1=Person()
p1.change_name("Rasel")
print(p1.name)

