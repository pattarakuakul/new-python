set_a = {1,2,3,4}
set_b ={2,3}
set_c ={1,2,3,4}
set_d ={1,2,3,4,5}

print("Is set_a a superset of set_b?", set_a >= set_b)  # Output: True
print("Is set_b a subset of set_a?",set_b <= set_a)  # Output: True


print("Is set_a a superset of set_c?", set_a > set_b)
print("Is set_a a subset of set_d?", set_a < set_d)  # Output: true

print("Are set_A and Set_c equal?", set_a == set_c)  # Output: True
print("Is set_b a subset of set_d and not equal?", set_b <= set_d and set_b != set_d)  # Output: True