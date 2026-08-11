fruits_with_duplicates =["apple","banana","apple","cherry","apple","kiwi","apple","apple","apple","apple","apple","apple","apple"]
while "apple" in fruits_with_duplicates:
    fruits_with_duplicates.remove("apple")
print(f"Fruits after remove : {fruits_with_duplicates}")