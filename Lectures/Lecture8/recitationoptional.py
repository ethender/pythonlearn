##
##
##
##  Recitation Optional 
##
##
##
##

class Person(object):

    def __init__(self, name, classes):
        self.name = name
        self.classes = classes

    def get_name(self):
        return self.name

    def get_classes(self):
        return self.classes




a = Person('a',[1,2,4])
b = a.classes
b.append(5)
print a.get_classes
print a.get_classes()
