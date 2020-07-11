# Calculating the average number of words per sentence in a paragraph.

input = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras suscipit nisl quam, eu auctor elit fermentum eu. Fusce faucibus ipsum erat, a semper ante pretium non. Proin blandit at diam eget tincidunt. Nunc efficitur nunc at nisi auctor malesuada. Phasellus a turpis non libero luctus semper. 
Donec vitae scelerisque tortor. Praesent vel nibh faucibus, aliquam 
nulla sit amet, aliquam augue. Vivamus vitae justo sodales, luctus erat ut, 
faucibus elit.Nulla at volutpat orci. Nullam sed odio nulla. 
Sed gravida accumsan ex, nec posuere lacus sodales id. Nulla vulputate vel 
risus et bibendum. Mauris ultrices dolor sed nulla finibus, nec consequat 
arcu mollis. Morbi non tempus nulla, id pharetra libero. Phasellus non turpis 
non orci pulvinar convallis sit amet nec purus. Nunc egestas interdum sem. 
Mauris rutrum nunc risus, at posuere lacus euismod ac."""

list_of_lists =[]
sentences = input.split('.')

list_of_lists = [ sentence.split() for sentence in sentences ]

all_words_sum = sum([ len(list) for list in list_of_lists])

word_sentence_average = all_words_sum / len(list_of_lists)

print(word_sentence_average)
