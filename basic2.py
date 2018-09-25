# Last file is too long, So I decided to start a new one.

# Next topic is 'Sets'
# Sets is one kind of lists, but with no duplicate items.
# It's very similar to use.
# this example arises another problem, how to split a sentence and remove puncuation
import string
sentence = 'Swallow, swallow, my little swallow.'
print(sentence)
# maketrans method is suit to translate method, to provide a  table
# method should be called by an object
# maketrans, first and second parameter should have same length.
# The third parameter would be replacing to nothing.
str = sentence.translate(sentence.maketrans('','', string.punctuation))
print(str)
list = list(str.split(" "))
set = set(str.split(" "))
print(list)
print(set)
