def find_all_pair_woth_product(nums: list,target: int)->list:
    result=[]
    for i in nums:
        for j in nums:
            sum= i * j
            if sum == target and [j,i] not in result and i != j :
                    result.append([i,j])
    return result


print(find_all_pair_woth_product([1,2,3,4,6], 6))