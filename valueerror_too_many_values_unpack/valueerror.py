
### List

name1,name2,name3 = ['Marta','Tristan','Gordon']
print(name1)
print(name2)


### for loop
dict_example = {
    'name': 'John',
    'age':35
}
for key in dict_example:
    print(key + " : " + str(dict_example.get(key)))

## split

#list='word1.word2.word3'.split('.')
print('word1.word2.word3'.split('.'))


a,b = input("Enter two numbers:").split()
print(a)
print(b)