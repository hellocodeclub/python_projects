# Approach 1 - Count
count="Every next level of your life will demand a different you".count('e')
print(count)

# Count: see all parameter options
sentence = 'Hey there, How are you doing?'
print(sentence.count('Hey'))
print(sentence.count('Hey',5))
print(sentence.count('How',0,7))
print(sentence[5:])
print(sentence[0:7])


# Approach 2 - Re module
print('Using Re module')
import re
sentence = "Every next level of your life is the next challenge"
print(len(re.findall("e", sentence)))
print(len(re.findall("next", sentence)))



# Approach 3 - collections module

from collections import Counter
sentence = "Every next level of your life will demand a different you"
counter = Counter(sentence)
print(counter['a'])

# Counting word occurences

sentence="Every next level of your life will demand a different you"
next_count = sentence.count('next') # a word in the sentence
the_count = sentence.count('the') # word that is not in the sentence
print(next_count)
print(the_count)

# Counter - most_commons method

c = Counter('abcdeabcdabcaba')
print(c.most_common(5))
print(c.most_common(2))


# Count total characters in a string

total_characters = len('Every next level of your life will demand a different you')
print(total_characters)

# Count total different characters in a string
sentence = 'Every next level of your life will demand a different you'
different_characters = set()
for ch in sentence:
    different_characters.add(ch)
print(len(different_characters))

# Find last occurrence
text = 'abcdeabcdabcaba'
print(text.rfind('a'))

# Count occurrences in a list
list =['blue','red','green','blue','black','blue','red','green']
print(list.count('blue'))




