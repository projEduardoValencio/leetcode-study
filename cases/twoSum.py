from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pInicial = 0
        pFinal = len(numbers) - 1

        while pInicial < pFinal:
            sum = numbers[pInicial] + numbers[pFinal]
            if sum == target:
                return [pInicial + 1, pFinal + 1]
            elif sum < target:
                pInicial+=1
            else:
                pFinal-=1

        return [];

print(Solution().twoSum([2,7,11,15], 9)) # [1, 2]
print(Solution().twoSum([2,3,4], 6)) # [1, 3]