from collections import Counter

class Solution(object):
    def score(self, cards, x):
        pairs = {"left_x": Counter(), "right_x": Counter(), "all_xx": 0}

        for i in range(len(cards)):
            if cards[i][0] == x and cards[i][1] != x:
                pairs["left_x"][cards[i][1]] += 1
            elif cards[i][1] == x and cards[i][0] != x:
                pairs["right_x"][cards[i][0]] += 1
            elif cards[i][0] == x and cards[i][1] == x:
                pairs["all_xx"] += 1

        def max_matching(counter, extra):
            # counter: multiset of letters; extra: number of wildcard "xx" cards
            # available to this side. Any two DIFFERENT letters can pair; a
            # wildcard can pair with anything (including another wildcard's
            # partner, but not with another wildcard itself).
            n = sum(counter.values()) + extra
            mx = max([extra] + list(counter.values())) if counter or extra else 0
            return min(n // 2, n - mx)

        xx = pairs["all_xx"]
        best = 0
        # try every way of splitting the xx cards between left and right
        for z1 in range(xx + 1):
            z2 = xx - z1
            total = max_matching(pairs["left_x"], z1) + max_matching(pairs["right_x"], z2)
            best = max(best, total)

        return best