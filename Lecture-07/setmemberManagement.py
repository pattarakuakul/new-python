fruits = {"apple", "banana", "cherry"}

fruits.add("orange")
print(fruits)  # Output: {'banana', 'cherry', 'orange', 'apple'}

fruits.remove("banana")
print(fruits)  # Output: {'cherry', 'orange', 'apple'}

fruits.discard("grape")
print(fruits)  # Output: {'cherry', 'orange', 'apple'}

removed_item = fruits.pop()
print(removed_item)  # Output: 'cherry' (or another item, since sets are unordered)

fruits.clear()
print(fruits)  # Output: set()