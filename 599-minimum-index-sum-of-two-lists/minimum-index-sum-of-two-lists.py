class Solution(object):
    def findRestaurant(self, list1, list2):
        d = {}

        for i in range(len(list2)):
            d[list2[i]] = i

        min1 =len(list1)+len(list2)
        Y = []

        for i in range(len(list1)):
            if list1[i] in d:
                idx = d[list1[i]]

                if i + idx < min1:
                    min1 = i + idx
                    Y = [list1[i]]
                elif i + idx == min1:
                    Y.append(list1[i])

        return Y