survey_results=[
    ["Python","JavaScript","C++"],
    ["Python","JavaScript","C#"],
    ["Python","Java"],
    ["Python","C++","JavaScript"],
    ["Python","JavaScript","C++","Java"],
]

sur_re = [set(per) for per in survey_results]
print(sur_re)
awnser1 = set.intersection(*sur_re)
print("awnser1 is :", awnser1)

# awnser2 = 
# print(awnser2)
allPro=set.union(*sur_re)
awnser3 = len(allPro)
print("awnser3 is :",awnser3)