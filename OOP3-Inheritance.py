# class A:
#     def sayhello(self):
#         print("Hello")
#
#
# class B(A):
#     def saygoodbye(self):
#         print("Goodbye")
#
#
# class C(B):
#     pass
#
#
# parent = A()
# child = B()
# grandchild = C()
# child.sayhello()
# grandchild.saygoodbye()

# ----------------------------------------------------------------------------------------------------------------------

# class Parent:
#     def __init__(self, name, city, job):
#         self.name = name
#         self.city = city
#         self.job = job
#
#     def sayhello(self):
#         print("Hello")
#
#
# class Child(Parent):
#     def __init__(self, name, university, field, job=None, city=None):
#         super().__init__(name, city, job)
#         self.uni = university
#         self.field = field
#
#     def saygoodbye(self):
#         print("Goodbye")
#
#
# # valed = Parent("asghar", "yazd", "teacher")
# farzand = Child(university="sharif", name="farid", field="computer")
# print(farzand.city)


# ----------------------------------------------------------------------------------------------------------------------

# Without Inheritance

# class Pedar:
#     def __init__(self, fname):
#         self.familyname = fname
#
#     def greeting(self):
#         print("hello")
#
#
# class Farzand:
#     def __init__(self):
#         self.pedar = Pedar(input("Familyname : "))
#
#     def say_goodbye(self):
#         print("goodbye")
#
#
# pesar = Farzand()
# print(pesar.pedar.familyname)
