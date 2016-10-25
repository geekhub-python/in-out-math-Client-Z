#!/usr/bin/env python3
minutes = int(input("Enter count minutes: "))

while((minutes // 60) > 23):
	minutes = minutes - 60*24

h = minutes // 60
m = minutes % 60

print(h,m)
