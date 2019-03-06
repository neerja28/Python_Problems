str = "aIbohPhoBiA"
str = str.casefold()
#print (str)
# aibohphobia
#print (list(str))
# ['a', 'i', 'b', 'o', 'h', 'p', 'h', 'o', 'b', 'i', 'a']
new_str = reversed(str)
#print (new_str)
# <reversed object at 0x10542bba8>
#print (list(new_str))
# ['a', 'i', 'b', 'o', 'h', 'p', 'h', 'o', 'b', 'i', 'a']

if list(str) == list(new_str):
    print ("It's a palindrome")
else:
    print ("No its not a palindrome")
