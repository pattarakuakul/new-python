attendance_week =[
    ["Alice","Bob","Charlie","David"],
    ["Alice","Charlie","David"],
    ["Alice","Bob","David"],
    ["Alice","David","Eve"],
    ["Bob","Charlie","David"]
]

#convert to set
attendance_sets = [set(day) for day in attendance_week]
print(attendance_sets)

#find the set who come every day
present_every_day = set.intersection(*attendance_sets)
print("Present every day :", present_every_day)

#How many student
all_students=set.union(*attendance_sets)
adsent_at_least_one_day = all_students - present_every_day
print("Adsent at least one day :", adsent_at_least_one_day)

first_day_present = attendance_sets[0]
last_day_present= attendance_sets[-1]
first_day_but_not_last = list(first_day_present - last_day_present)
print("Present on first day but absent on last day:" ,first_day_but_not_last)

unique_student_count = len(all_students)
print("Total unique students:",unique_student_count)
