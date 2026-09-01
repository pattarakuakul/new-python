def count_duplicated_word(word: str) -> dict:
    chars = {}
    for c in word:
        chars[c] = 0
    for c in word:
        chars[c] += 1
    result = {}
    for ch in chars:
        if chars[ch] >= 2:
            result[ch] = chars[ch]
    return result

print(count_duplicated_word("mississippi"))