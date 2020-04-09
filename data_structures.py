# Assigning elements to different lists

listOne = ('Apple', 'Mango', 'Orange');
listTwo = (21, 43.5, 56, 109);

print ('listOne: ',listOne)
print ('listTwo: ',listTwo, '\n')

# Accessing elements from a Tuple

tupleOne = ['Fairy tales', 'Fiction', 'Fantasy', 1234, 465]

print ('tupleOne: ',tupleOne)

print ('tupleOne[1]: ',tupleOne[1])
print ('tupleOne[4]: ', tupleOne[4], '\n')

# Deleting different dictionary elements

dictionaryOne = {1 : 'Apple', 2 : 'Ball', 3 : 'Cat'}
dictionaryTwo = {'Botany' : 'Plants', 'Zoology' : 'Animals'}

print ('dictionaryOne: ', dictionaryOne)
print ('dictionaryTwo: ', dictionaryTwo)

del dictionaryOne[2]
del dictionaryTwo['Botany']

print ('dictionaryOne: ', dictionaryOne)
print ('dictionaryTwo: ', dictionaryTwo)
