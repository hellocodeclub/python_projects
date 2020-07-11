

def convert_to_list(text):
    list = []
    word = ''
    for character in text:
        if(character!=' '):
            word=word+character
        else:
            if len(word)>0 :
                list.append(word)
                word=''

    list.append(word)
    return list

my_text = 'The sky is blue'
list = convert_to_list(my_text)
print(list)
