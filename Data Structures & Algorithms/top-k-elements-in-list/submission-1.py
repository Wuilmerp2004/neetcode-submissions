class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        items = []
        for num, cnt in count.items():
            items.append([cnt, num])
        items.sort()
        res = []
        while len(res) < k:
            res.append(items.pop()[1])
        return res 



        
        


        