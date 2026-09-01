def longest_unique_word_sequence(words: list[list[str]]) -> tuple:
    EmUnit = []
    EmUnit3 = []
    
    for unit in words:
        for unit2 in unit:
            unitStr = str(unit2)
            unitlower = unitStr.lower()
            EmUnit.append(unitlower)
    if not EmUnit:
        return (0, [])
        
    max_length = 0
    
    n = len(EmUnit)
    for i in range(n):
        for j in range(i + 1, n + 1):
            sub = EmUnit[i:j]
            if len(sub) == len(set(sub)):
                if len(sub) > max_length:
                    max_length = len(sub)
                    EmUnit3 = [sub]
                elif len(sub) == max_length:
                    EmUnit3.append(sub)

    return (max_length, EmUnit3)

words = [["apple", "banana"], ["apple"], ["cherry", "banana"]]
print(longest_unique_word_sequence(words),type(words))
# ผลลัพธ์: (3, [['banana', 'apple', 'cherry'], ['apple', 'cherry', 'banana']])
words2 = [["dog", "cat"], ["mouse", "cat"], ["bird", "dog"]]
print(longest_unique_word_sequence(words2),type(words2))
# ผลลัพธ์: (4, [['mouse', 'cat', 'bird', 'dog']])