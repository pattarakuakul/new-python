def find_all_pair_woth_product(nums: list, target: int) -> list:
    result = []
    for i in range(len(nums)):
        # แก้ไขจุดที่ 1: เปลี่ยนจาก range(i+1),len(nums) เป็น range(i+1, len(nums))
        for b in range(i + 1, len(nums)):
            # แก้ไขจุดที่ 2: เปลี่ยนจาก nums(i) เป็น nums[i]
            if nums[i] * nums[b] == target:
                # แก้ไขจุดที่ 3: จัดเก็บผลลัพธ์เป็นคู่ tuple (nums[i], nums[b]) เพื่อความสวยงาม
                result.append([nums[i], nums[b]])
    return result


print(find_all_pair_woth_product([1,2,3,4,6],6))
#print(find_all_pair_woth_product([2,4,5,7],14))
#print(find_all_pair_woth_product([3,5,9,10],25))
#print(find_all_pair_woth_product([1,2,3,4,5],20))