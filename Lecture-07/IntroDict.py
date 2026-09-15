
phonebook={'Kit': '777-1111','gust':'777 9000','peetooo':'115-5000'}

print(phonebook)
print(phonebook['gust'])
print(phonebook.get('peetooo'))

key = 'Pluto'
if key in phonebook:
    print(phonebook['Pluto'])
else:
    print(key + '  not in Phonebook')

phonebook['Simpson'] = '777-6666'
phonebook['Pluto'] = '777-9999'
phonebook['gust'] = '999-6666'
print(phonebook)

print()
del phonebook['Simpson']
print(phonebook)