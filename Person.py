class Person:
  lastIdUsed=100
  def __init__(self, fn, ln):
    self.fname=fn
    self.lname=ln
    Person.lastIdUsed+=1
    self.pid=Person.lastIdUsed
  def __str__(self):
    return("["+str(self.pid)+"]"+self.fname+" "+self.lname)

p=Person("Jim", "Jones")
print(p)
