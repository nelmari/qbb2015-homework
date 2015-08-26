#!/usr/bin/env python

## Key notes of August 25 (Day2 of QBB2015): Python

# Integer
i = 10000

# Floating point/ real number
f = 0.333 

i_as_f = float(i)
f_as_i = int(f)

# String
s = "A String"

# Boolean 
truthy = True
falsy = False

# Lists -- contains only one type (convention)
l = [1,2,3,4,5]
l.append (7)

# Tuple -- contains different types
t = (1,"foo",5.0)

# Dictionary
d1 = {"key1":"value1", "key2":"value2"} # Literal form
d2 = dict(keyA="valueA", keyB="valueB") # Dictionary function
d3 = dict([("keya","valuea"),("keyb","valueb")]) # List of tuples & dictionary function

for value in (i, f, s, truthy, falsy, l, t, d1, d2, d3):
    print value, type (value) ; # Use commas to separate data type values to print

