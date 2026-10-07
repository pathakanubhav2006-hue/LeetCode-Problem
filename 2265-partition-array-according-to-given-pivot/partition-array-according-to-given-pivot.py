class Solution(object):
    def pivotArray(self, nums, pivot):
        LS=[]
        RS=[]
        count=0
        for i in range(len(nums)):
            if nums[i]==pivot:
                count+=1
            elif nums[i]<pivot:
                LS.append(nums[i])
            else:
                RS.append(nums[i])
        
        while(count):
            LS.append(pivot)
            count-=1
        return (LS+RS)