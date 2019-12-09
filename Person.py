class Person:
  lastIdUsed=100
  def __init__(self, name):
    name=name
    lastIdUsed+=1
    pid=lastIdUsed
