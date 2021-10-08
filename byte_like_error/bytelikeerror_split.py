
text_in_binary = b'Sky is blue.Roses are red'.decode("UTF-8")

print(type(text_in_binary))
replaced_text = text_in_binary.replace('red','blue')
print(replaced_text)