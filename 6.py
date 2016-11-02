#!/usr/bin/env python3

len_rows = int(input()) 
len_tears = int(input())
quantity_tears = int(input())
free_length = int(input())

a = len_rows + len_tears
b = (quantity_tears * a) + free_length
b = b * 2

print(b)
