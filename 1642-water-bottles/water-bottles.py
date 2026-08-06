class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        drink_water = numBottles

        while numBottles >= numExchange:
            new_bottles = numBottles // numExchange
            drink_water += new_bottles
            numBottles = new_bottles + (numBottles % numExchange)
        
        return drink_water

        