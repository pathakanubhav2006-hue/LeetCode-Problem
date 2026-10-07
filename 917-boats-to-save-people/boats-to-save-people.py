class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        left, right = 0, len(people) - 1
        boats = 0

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1          # lightest person shares the boat
            right -= 1             # heaviest person always boards
            boats += 1

        return boats
        