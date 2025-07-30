#!/usr/bin/python3

group_totals = __import__('0-group_totals').group_totals

A = ["B:-1", "A:1", "B:3", "A:5" ]
B = [ "X:-1", "Y:1", "X:-4", "B:3", "X:5" ]
C = [ "Z:0", "A:-1" ]

print(group_totals(A))
print(group_totals(B))
print(group_totals(C))
