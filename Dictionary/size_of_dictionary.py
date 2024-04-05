"""
Finding the Size of the Dictionary in Bytes
The size of a Dictionary means the amount of memory (in bytes) occupied by a Dictionary object. In this article, we will learn various ways to get the size of a Python Dictionary.
"""

import sys
 
 
dic1 = {"A": 1, "B": 2, "C": 3}
dic2 = {"Geek1": "Raju", "Geek2": "Nikhil", "Geek3": "Deepanshu"}
dic3 = {1: "Lion", 2: "Tiger", 3: "Fox", 4: "Wolf"}
 
print("Size of dict1: "+ str(sys.getsizeof(dic1)) + " bytes")
print("Size of dic2: " + str(sys.getsizeof(dic2)) + " bytes")
print("Size of dic3: "+ str(sys.getsizeof(dic3)) + " bytes")