sentence = "Hello this Is an Example With cased letters"

words = sentence.split()
# ['Hello', 'world', 'how', 'are', 'you', 'I', 'am', 'good', 'apple', 'bananana', 'cat', 'birt']

words.sort()
# ['Example', 'Hello', 'Is', 'With', 'an', 'cased', 'letters', 'this']

print (" ".join(words))
# Example Hello Is With an cased letters this

for word in words:
    print (word)

"""
Example
Hello
Is
With
an
cased
letters
this
"""
