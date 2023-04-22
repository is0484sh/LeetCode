class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i+1:]):
                if num1 + num2 == target:
                    answer.append(i)
                    answer.append(i+j+1)
                    return answer
