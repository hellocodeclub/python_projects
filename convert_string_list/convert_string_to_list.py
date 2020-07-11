####################################################

my_text = 'The sky is blue'
my_text_with_extra_spaces = '   The    sky    is   blue  '
list_of_strings = my_text.split()
list_of_strings_extra_spaces = my_text_with_extra_spaces.split()
print(list_of_strings)
print(list_of_strings_extra_spaces)

####################################################

my_text = 'Sky is blue. Roses are red'
my_text_with_extra_spaces = '   Sky is blue.    Roses are red   '

list_of_sentences = my_text.split('.')
list_of_sentences_with_extra_spaces = my_text_with_extra_spaces.split('.')

print(list_of_sentences)
print(list_of_sentences_with_extra_spaces)

####################################################

import re
my_text = 'The weather is great in this area, I know. Do you agree?.I don\’t. The weather is horrible here'
list = re.split('\\.|\s|\\,', my_text)

print(list)

####################################################
# Convert String to List of List
my_text = 'Sky is blue. Roses are red'
sentence_list = my_text.split('.')
list_of_lists = [ sentence.split() for sentence in sentence_list ]

print(list_of_lists)
print(type(list_of_lists))


####################################################
# Split string by characters

my_text = 'Sky is blue'
characters = [character for character in my_text]

print(characters)
print(type(characters))

####################################################
# Convert String to List of int

# Method 1

import ast
my_text = '1,2,4,5,67'
list_of_integers = ast.literal_eval('['+my_text+']')
print(list_of_integers)
print(type(list_of_integers))

# Method 2
import json
my_text = '1,2,4,5,67'
list_of_integers_with_json = json.loads('['+my_text+']')
print(list_of_integers_with_json)
print(type(list_of_integers_with_json))

####################################################
# Convert String to List of Dictionaries

# Method #1
import ast
my_text = '{"id":1,"name":"Bob","age":20},{"id":2,"name":"Alice","age":22}'
list_of_dictionaries = ast.literal_eval('['+my_text+']')
print(list_of_dictionaries)
print(type(list_of_dictionaries))
print(type(list_of_dictionaries[0]))

# Method #2
import json
my_text = '{"id":1,"name":"Bob","age":20},{"id":2,"name":"Alice","age":22}'
list_of_dictionaries = json.loads('['+my_text+']')
print(list_of_dictionaries)
print(type(list_of_dictionaries))
print(type(list_of_dictionaries[0]))

####################################################
# Convert list to string

list = ['Sky','is','really','blue']
list_string=str(list)
print(list_string)
print(type(list_string))
