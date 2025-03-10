from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for index in range(len(nums)):
            if target - nums[index] in indices:
                return [indices[target - nums[index]],index]
            indices[nums[index]] = index 
        return []     
               

solution = Solution()
print(solution.twoSum([2,7,11,15],9))

print(solution.twoSum([3,2,3],6))



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted((num,index) for index,num in enumerate(nums))
        left,right = 0,len(nums)-1
        while left < right:
            if sorted_nums[left][0] + sorted_nums[right][0] == target:
                return [sorted_nums[left][1] ,sorted_nums[right][1]]
            elif sorted_nums[left][0] + sorted_nums[right][0] < target:
                left += 1
            else:
                right -= 1
        return []

solution = Solution()
print(solution.twoSum([2,7,11,15],9))

print(solution.twoSum([3,2,3],6))

