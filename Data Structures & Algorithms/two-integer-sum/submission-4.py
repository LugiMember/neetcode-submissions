class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #get every number into a map, contains key and value is indice
        #on the first number subtract it from the target and see if it exists
        map = {}
        count = 0
        for num in nums:
            map[num] = count
            count+=1
        
        count = 0
        for num in nums:
            complement = target - num
            output = map.get(complement)
            if output != None and output != count:
                return [count, map.get(complement)]
            count+=1