class Solution(object):
    def passThePillow(self, n, time):
        pass_pillow=time%(n-1)
        x=time//(n-1)
        if x%2==0:
            pass1=1+pass_pillow
        elif x%2!=0:
            pass1=n-pass_pillow

        return pass1
            