""" Ezekiel M. Bustillo
    DATALOGO Lab04
    Feb. 12, 2020
    I have neither received nor provided any help on this (lab) activity,
    nor have I concealed any violation of the Honor Code.
"""

class Vector:

 def __init__(self, d):
  self._coords = [0] * d
 def __len__(self):
    return len(self._coords)
 def __getitem__(self, j):
    return self._coords[j]
 def __setitem__(self, j, val):
  self._coords[j] = val
 def __add__(self, other):
    if len(self) != len(other): # relies on len method
        raise ValueError( 'dimensions must agree' )
    result = Vector(len(self)) # start with vector of zeros
    for j in range(len(self)):
        result[j] = self[j] + other[j]
    return result

 def __sub__(self, other):
     if len(self) != len(other):  # relies on __len__ method
         raise ValueError('dimensions must agree')
     result = Vector(len(self))  # start with vector of zeros
     for j in range(len(self)):
         result[j] = self[j] - other[j]
     return result

 def __mul__(other1,other2):
    result = 0           # start with vector of zeros
    for j in range(len(other1)):
      result+= other1[j]*other2[j]
    return result
 def __str__(self):
     return '<' + str (self._coords)[1:-1]+ '>' # adapt list representation

if __name__=="__main__":
    v = Vector(5)  # construct five-dimensional <0, 0, 0, 0, 0>
    v[1] = 23  # <0, 23, 0, 0, 0> (based on use of __setitem__)
    v[-1] = 45  # <0, 23, 0, 0, 45> (also via __setitem__)
    print(v[4])  # print 45 (via __getitem__)
    u = v + v  # <0, 46, 0, 0, 90> (via __add__)
    print(u)  # print <0, 46, 0, 0, 90>
    w = v * u
    print(w)
    total = 0
    for entry in v:  # implicit iteration via __len__ and __getitem__
        total += entry