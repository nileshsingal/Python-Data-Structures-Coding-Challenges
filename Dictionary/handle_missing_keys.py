"""
Handling missing keys in Python dictionaries
In Python, dictionaries are containers that map one key to its value with access time complexity to be O(1). 
But in many applications, the user doesn’t know all the keys present in the dictionaries.
In such instances, if the user tries to access a missing key, an error is popped indicating missing keys. 
"""

#1 Using in
d = { 'a' : 1 , 'b' : 2 }
if 'q' in d:
    print(d[q])
else:
    print("Key Not Found")
    

#2 Using get()
d = { 'a' : 1 , 'b' : 2 }
print(d.get('q', 'Key Not Found'))

#3 Using default
country_code = {'India' : '0091',
                'Australia' : '0025',
                'Nepal' : '00977'}

country_code.setdefault("Japan", "Not Present" )
print(country_code["India"])
print(country_code["Japan"])

#Try catch
country_code = {'India': '0091',
                'Australia': '0025',
                'Nepal': '00977'}
try:
    print(country_code['India'])
    print(country_code['USA'])
except KeyError:
    print("Key Not Found")