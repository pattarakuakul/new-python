def longest_unique_word_sequence(words: list[list[str]]) -> tuple:
    EmUnit=[]
    EmUnit3=[]
    for unit in words:
            for unit2 in unit:
                unitStr=str(unit2)
                unitlower=unitStr.lower()
                EmUnit.append(unitlower)
    max_length = 0
    for i in range(len(EmUnit)):
        EmUnit2 = []
        for j in range(i, len(EmUnit)):
            word = EmUnit[j]
            if word in EmUnit2:
                break
            else:
                EmUnit2.append(word)
        seg_len = len(EmUnit2)
        
        if seg_len > max_length:
            max_length = seg_len
            EmUnit3 = [EmUnit2.copy()]
        elif seg_len == max_length and seg_len > 0:
            if EmUnit2 not in EmUnit3:
                EmUnit3.append(EmUnit2.copy())

    return (max_length,EmUnit3)


words = [["apple", "Banana"], ["apple"], ["cherry", "banana"]]
print(longest_unique_word_sequence(words))
# ผลลัพธ์: (3, [['banana', 'apple', 'cherry'], ['apple', 'cherry', 'banana']])
words2 = [["dog", "cat"], ["mouse", "cat"], ["bird", "dog"]]
print(longest_unique_word_sequence(words2))
# ผลลัพธ์: (4, [['mouse', 'cat', 'bird', 'dog']])