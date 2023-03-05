class Solution:
    '''
    There is a marketing company that owns set of banners on a bridge. There are 3 different sizes of banners: small, medium and large. At the beginning of each year, shops start to request sizes of the banners and offer an amount of money in return. Of course, there are a lot of shops that want to rent the banners, but we have limited number of banners The marketing company wants us to compute the maximum profit they could get by renting the banners, by selecting the shops that are going to rent the banners.

    Notes
    If the shop requested a medium-size banner, we could assign medium or large banner to him. If the shop requested a small-size banner, we could assign to him any banner size.
    We must give the shop exactly the requested number of banners in order for the shop to pay the money. For example, if the shop wants 5 banners, we must give the shop 5 banners. If we can't give the shop 5 banners, then we don't assign banners to this shop and we don't get money from it.
    We can give the shop banners with different sizes. For example, if the shop requested 10 small banners, we can assign (3 small. 3 medium and 4 large to that shop.

    Write a function: int solution(int[] sizes, int[] prices, int[] requestedSize)
    That, given a zero-indexed array A consisting of 3 integers that represent the number of banners owned by the marketing company from each size (A[0] represents the number of small banners, A[1] represents the number of medium banners, and A[2] represents number of large banners), a zero-indexed array B consisting of K integers that represent the price each shop offers per banner, and a zero-indexed array C consisting of K integers represent the requested number of banners (C(i)/10) and the size of the banner requested per shop (C(i)%10, 0 means small size, 1 means medium size, 2 means large size), returns an integer that represents the maximum profit.

    Assume that:
    1. The length of array A is 3
    2. The values in A are between [0, 35]
    3. The lengths of arrays B, C are between [1, 100]
    4. The values in B are between [1, 100]
    5. The values in C are between [10, 502]

    Example Input:
    A = [1,2,3] (this means that we have 1 small banner, 2 medium banners, 3 large banners)
    B = [4,5,6] (this means that we have 3 shops that wants to rent the banners the first shop will pay 4$ per banner, the second shop will pay 5S and the third shop will pay 6$)
    C = [10,21,32] (this array will be the same size as prices, and means that the first shop wants 1 (10/10 = 1) banner of small size (10%10 = 0), the second shop wants 2 (21/10 = 2) banners of medium size (21%10 = 1) and the third company wants 3 (32/10 = 3) banners of large size (32%10 = 2))
    Shop 1 will pay 4$ per banner and wants 1 banner of small size
    Shop 2 will pay 5$ per banner and wants 2 banners of medium size
    shop 3 will pay 6$ per banner and wants 3 banners of large size

    Output: 32
    Explanation: The function must return: 32 (1*4 +2*5 + 3*6)
    '''
    @staticmethod
    def numberBanners(sizes, prices, requestedSize):
        mp = []
        for i, s in enumerate(requestedSize):
            mp.append([prices[i], s % 10, s // 10])
        ans = 0
        for price, size, qty in sorted(mp, reverse=True):
            if sizes[size] > 0:
                qty = min(sizes[size], qty)
                ans += price * qty
                sizes[size] -= qty
        return ans

print(Solution.numberBanners([1,5,3], [4,5,6], [10,41,31]))
