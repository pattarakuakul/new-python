set1 = {1,2,3,4}
set2 = {3,4,5,6}

unio_set = set1|set2
print("Union:", unio_set)  # Output: {1, 2, 3, 4, 5, 6}

intersection_set = set1&set2
print("Intersection:", intersection_set)  # Output: {3, 4}

difference_set = set1-set2
print("Difference:", difference_set)  # Output: {1, 2}

sym_diff_set = set1^set2
print("Symmetric Difference:", sym_diff_set)  # Output: {1, 2, 5, 6}
