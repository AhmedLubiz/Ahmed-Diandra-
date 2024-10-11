list_buah = ['Duren', 'Jambu', 'Pisang', 'Apel']
print('list_buah:', list_buah)

print(list_buah[-1])
print(list_buah[-2])
print(list_buah[-3])
print(list_buah[-4])

print(list_buah[1:3])

list_buah[0] = 'Naga'
print(list_buah)

list_buah.append('Jambu Monyet')
print(list_buah)

list_buah.insert(2, 'Bakso')
print(list_buah)

list_buah.pop()
print(list_buah)
list_buah.remove('Bakso')
print(list_buah)
del list_buah[0]
print(list_buah)

list_buah.sort()
print(list_buah)