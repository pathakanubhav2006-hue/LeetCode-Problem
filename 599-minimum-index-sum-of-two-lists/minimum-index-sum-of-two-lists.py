class Solution(object):
    def findRestaurant(self, list1, list2):
        Y = []
        min1 = len(list1) + len(list2)

        for i in range(len(list1)):
            if list1[i] in list2:
                idx = list2.index(list1[i])

                if i + idx < min1:
                    min1 = i + idx
                    Y = [list1[i]]
                elif i + idx == min1:
                    Y.append(list1[i])

        return Y