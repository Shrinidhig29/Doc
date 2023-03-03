"""nums = [1, 2, 34, 56, 1]
target = 2 
if target is 2 then sum index of nums[] is equal to taget"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
       seen = {}
       for i, value in enumerate(nums): #1
           remaining = target - nums[i] #2
           
           if remaining in seen: #3
               return [i, seen[remaining]]  #4
           else:
               seen[value] = i  #5
[2,7,11,15]
9
