with open('file_sample.txt', 'rb') as f:
    lines = [x.strip() for x in f.readlines()]

count = 0
for line in lines:
    tmp = line.strip().lower()
    words = tmp.replace(b'line',b'Line')
    print(words)
    for word in words:
        if(word == 'line'):
            count= count+1
print('Count: '+str(count))

# The count won't be correct if you are reading the file in binary mode

text_in_binary = b'Sky is blue.Roses are red'.decode('utf-8')
print(type(text_in_binary))
replaced_text = text_in_binary.replace('red','blue')
print(replaced_text)