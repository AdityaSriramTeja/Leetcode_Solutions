class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) -1
        while start < end: 
            add = numbers[start] + numbers[end] 
            if add < target: 
                start+=1 
            elif add > target: 
                end -=1 
            else: 
                return [start+1,end+1] 
        return []