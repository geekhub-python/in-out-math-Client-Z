#!/usr/bin/env python3
students = int(input("Enter count students: "))
apples = int(input("Enter count apples: "))

count_apples_result = apples // students 
count_apples = apples % students
print(count_apples_result)
print(count_apples)
