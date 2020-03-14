# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 21:00:15 2020

@author: grezende
"""

class Student(object):
    id = 0
    
    def __init__(self):
        self.sid = Student.id
        Student.id += 1
        

s1 = Student()
s2 = Student()
s3 = Student()
s4 = Student()
s5 = Student()        

print(s1.sid)
print(s2.sid)
print(s3.sid)
print(s4.sid)
print(s5.sid)