#!/usr/bin/env python3
first = int(input("Enter count students in first class: "))
second = int(input("Enter count students in second class: "))
third = int(input("Enter count students in third class: "))

c = first // 2
if(first%2):
	c = c + 1
	
c1 = second // 2
if(second%2):
	c1= c1 + 1
	
c2 = third // 2
if(third%2):
	c2 = c2 + 1

print(c+c1+c2)
