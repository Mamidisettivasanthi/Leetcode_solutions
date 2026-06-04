class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s=str(n)
        product=1
        sum=0
        for i in range(len(s)):
            product=product*int(s[i])
            sum=sum+int(s[i])
            i=i+1
        return product-sum
        