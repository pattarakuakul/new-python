phonebook={'Kit': '777-1111','gust':'777 9000','peetooo':'115-5000'}

hedict = {}
hedict['Hulk'] = '888-1111'
print(hedict.get('Halk','Key not found'))
print(hedict.get('Hulk','Key not found'))

for key,value in phonebook.items():
    print(key,value)
print(phonebook.keys())
print(phonebook.values())


print(phonebook.pop('Kitt','Element not found'))
print(phonebook.pop('Kit','Element not found'))

print(phonebook)
print(phonebook.popitem())
print(phonebook)
phonebook.clear()
print("After clear")
print(phonebook)