import obj
class person :
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print("my name is ", self.firstname, "and my father is ", self.lastname)

class student(person):
    pass

class Student2(person):
  def __init__(self, fname, lname):
    person.__init__(self, fname, lname)
    #super().__init__(fname, lname)
    # they are the same

# class inheritanc at the top

instanc2 = Student2('deda', 'fkru')
instanc2.printname()
obj.tesitng()
instanc = student('yeabtsega', 'taye')
instanc.printname()