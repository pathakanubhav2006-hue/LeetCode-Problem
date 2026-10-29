class Solution(object):
    def mirrorDistance(self, n):
        reverse_n=0
        copy_n=n
        while(n):
            digit=n%10
            reverse_n=reverse_n*10+digit
            n/=10
        return(abs(copy_n-reverse_n))
        