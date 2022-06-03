class Solution:
    '''
    Next challenges:
    229
    '''
    def majorityElement(self, nums: List[int]) -> int:
        dct = defaultdict(int)
        for n in nums:
            dct[n] = dct[n]+1
        return sorted(dct.items(), key=lambda x: -x[1]).pop(0)[0]