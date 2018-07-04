class Parent(object):

    def implicit(self):
        print("PARENT implictit()")


class Child(Parent):
    pass


dad = Parent()
son = Child()

dad.implicit()
son.implicit()
