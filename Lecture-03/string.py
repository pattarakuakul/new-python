string1=input("Enter a first string: ")
string2=input("Enter a second string: ")

if string1 == string2:
    print(f'"{string1}" and "{string2}" are equal.')
else:
    print(f'"{string1}" and "{string2}" are not equal.')

if string1 < string2:
    print(f'"{string1}" comes before "{string2}".')
elif string1 > string2:
    print(f'"{string1}" comes after "{string2}" in lexicographical order.')

if string1.lower() == string2.lower():
    print(f'"{string1}" and "{string2}" are equal when case is ignored.')
else:
    print(f'"{string1}" and "{string2}" are not equal when case is ignored.')