#!/usr/bin/env python3

"""
75f27814477994851d582bc685328a19
oopython
lab2
v2
kakl19
2020-02-07 19:23:52
v4.0.0 (2019-03-05)

Generated 2020-02-07 20:23:53 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 2 - oopython
#
# If you need to peek at examples or just want to know more, take a look at
# the [Python documentation](https://docs.python.org/3/library/index.html).
# Here you will find everything this lab will go through and much more.
#



# --------------------------------------------------------------------------
# Section 1. Class relationships
#
# Practice on creating classes and relationships between them in python.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (2 points)
#
# Create a new class named **Person**.  Give the class the instance
# attributes "name" and "ssn". Make "ssn" a private attribute. The values for
# the attributes should be sent to the constructor as arguments.
# Create a *get* method for "ssn".
#
# In the code below create a new variable called **per** and set it to a new
# instance of Person. Give it the name `Skorstten` and ssn `768244-4857`.
#
#
# Answer with per\'s get method for ssn.
#
# Write your code below and put the answer into the variable ANSWER.
#
class Person():
    """
    Person class
    """

    def __init__(self, name, ssn, address=""):
        """Initiates person object"""
        self.name = name
        self._ssn = ssn
        self.address = address

    def get_ssn(self):
        """Gets private attribute ssn"""
        return self._ssn

    def set_address(self, address):
        """Sets address"""
        self.address = address

    def to_string(self):
        """Prints an object as a string"""
        str1 = "Name: {name} SSN: {ssn} {address}".format(
            name=self.name,
            ssn=self._ssn,
            address=self.address.to_string()
        )
        return str1

per = Person('Skorstten', '768244-4857')



ANSWER = per.get_ssn()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (2 points)
#
# Create a new class named **Address**.  Give the class the instance
# attributes "city", "state" and "country". The values for the attributes
# should be sent to the constructor as arguments.
# Create a method, in Address, called **to_string**, it should return
# `"Address: <city> <state> <country>"` (replace the \<city\> with the value
# of the attribute city...).
#
# Add the instance attribute **address** to class Person. It's value should
# be sent as argument to constructor, give it a default value of and empty
# string, `""`.
# Create a set method for attribute "address".
# Create a method, in Person, called **to_string**, it should return `"Name:
# <name> SSN: <ssn> Address: <city> <state> <country>"`. Use Address'
# to_string method to get address data.
#
# In the code below Create a new instance of the class Address. Initiate it
# with the city `Imre`, the state `Sagenmark` and the country `Andor`.
# Use the set method in Person to add the newly create Address object to your
# **per** object.
#
# Answer with per's "to_string" method.
#
# Write your code below and put the answer into the variable ANSWER.
#

class Address():
    """
    Address class
    """

    def __init__(self, city, state, country):
        """
        Inits address objects
        """
        self.city = city
        self.state = state
        self.country = country

    def to_string(self):
        """Prints an object as a string"""
        return "Address: {} {} {}".format(self.city, self.state, self.country)

address1 = Address('Imre', 'Sagenmark', 'Andor')

per.set_address(address1)


ANSWER = per.to_string()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (2 points)
#
# Create a new class name **Teacher** make it inherit from class "Person". In
# the constructor add the instance attribute "courses" and initiate it to and
# empty list.
# Create the method **add_course**, it should take one argument and add it to
# the course list attribute.
# Create the method **remove_course**, it should take one argument and remove
# if from the course list attribute.
# Overload the **to_string** method from the base class. It should return the
# same as the original method and add the courses to the end of the string,
# `"Name: <name> SSN: <ssn> Address: <city> <state> <country> Courses:
# <course>, <course>, ..."`. The list of courses should be comma seperated
# without one at the end. Tip, use `super(Teacher, self)` to access base
# method.
#
#
# In the code below Create a new instance of the class Address. Initiate it
# with the city `Renere`, the state `Vansterland` and the country `Illian`.
# Create a new instance of the class Teacher. Initiate it with the name
# `Farseer` and ssn `578118-6946` and the aforementioned Address object.
# Use the add_course method to add the following courses, `htmlphp`, `webapp`
# and `linux`.
#
#
# Answer with the Teacher object's "to_string" method.
#
# Write your code below and put the answer into the variable ANSWER.
#

class Teacher(Person):
    """
    Class for teacher
    """

    def __init__(self, name, ssn, address, courses=None):
        """Inits object"""
        if courses is None:
            courses = []
        super(Teacher, self).__init__(name, ssn, address)
        self.courses = courses

    def add_course(self, course):
        """Takes one argument and adds it to the course list attribute"""
        self.courses.append(course)

    def remove_course(self, course):
        """Takes one argument and removes it to the course list attribute"""
        self.courses.remove(course)

    def to_string(self):
        """Prints an object as a string"""
        return super(Teacher, self).to_string()+ \
        " Courses: {courses}".format(courses=', '.join(self.courses))

address2 = Address('Renere', 'Vansterland', 'Illian')
teacher1 = Teacher('Farseer', '578118-6946', address2)
teacher1.add_course('htmlphp')
teacher1.add_course('webapp')
teacher1.add_course('linux')

ANSWER = teacher1.to_string()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (2 points)
#
# Create a new class name **Student** make it inherit from class "Person". In
# the constructor add the instance attribute "courses_grades" and initiate it
# to and empty list.
# Create the method **add_course_grade**, it should take two arguments, one
# course and a grade. Create a tuple with the two arguments and add to the
# attribute "courses_grades".
# Create the method **average_grade**. Calculate and return the students
# average grade. Ignore grades with "-" in the calculation.
#
# In the code below Create a new instance of the class Address. Initiate it
# with the city `Elanor`, the state `Withywoods` and the country `Ceald`.
# Create a new instance of the class Student. Initiate it with the name
# `Badgerlock` and ssn `930807-7536` and the aforementioned Address object.
# Use the add_course_grade method to add the following courses, `python` with
# grade `5`, `oophp` with grade `-` and `design` with grade `5`.
#
#
# Answer with the Student object's "average_grade" method.
#
# Write your code below and put the answer into the variable ANSWER.
#

class Student(Person):
    """
    Class for student
    """

    def __init__(self, name, ssn, address, courses_grades=None):
        """Inits object"""
        if courses_grades is None:
            courses_grades = []
        super(Student, self).__init__(name, ssn, address)
        self.courses_grades = courses_grades

    def add_course_grade(self, course, grade):
        """
        Takes two arguments and adds it to the courses_grades list as a tuple
        """
        self.courses_grades.append((course, grade))

    def average_grade(self):
        """
        Calculates and return the students average grade.
        Ignore grades with "-" in the calculation.
        """
        count = 0
        grade = 0
        for tup in self.courses_grades:
            if tup[1].isdigit():
                grade += int(tup[1])
                count += 1
        return grade/count

address3 = Address('Elanor', 'Withywoods', 'Ceald')
student = Student('Badgerlock', '930807-7536', address3)
student.add_course_grade('python', '5')
student.add_course_grade('oophp', '-')
student.add_course_grade('design', '5')


ANSWER = student.average_grade()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)


dbwebb.exit_with_summary()
