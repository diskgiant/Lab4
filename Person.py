class Person:
  lastIdUsed=100
  def __init__(self, fn, ln):
    fname=fn
    lname=ln
    Person.lastIdUsed+=1
    pid=Person.lastIdUsed

p=Person("Jim", "Jones")
