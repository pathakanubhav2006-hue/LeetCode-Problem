class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
    
    # No overlap if one rectangle is completely to the left/right or above/below the other
        if rec1[0] >= rec2[2] or rec2[0] >= rec1[2]:
        # rec1's left edge is at/past rec2's right edge, OR
        # rec2's left edge is at/past rec1's right edge
            return False
    
        if rec1[1] >= rec2[3] or rec2[1] >= rec1[3]:
        # rec1's bottom edge is at/past rec2's top edge, OR
        # rec2's bottom edge is at/past rec1's top edge
            return False
    
        return True