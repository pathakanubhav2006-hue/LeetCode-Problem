class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        distance = 0  # This will store the final total count
        
        for i in range(len(arr1)):
            temp = 0  # Counts how many elements in arr2 violate the condition for arr1[i]
            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j]) <= d:
                    temp += 1
            
            # If temp is 0, it means NO element in arr2 was within distance d
            if temp == 0:
                distance += 1

        return distance