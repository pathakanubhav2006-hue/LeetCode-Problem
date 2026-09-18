class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        area_A = (ax2 - ax1) * (ay2 - ay1)   
        area_B = (bx2 - bx1) * (by2 - by1)   
        
        overlap_left = max(ax1, bx1)
        overlap_right = min(ax2, bx2)
        overlap_bottom = max(ay1, by1)
        overlap_top = min(ay2, by2)
        overlap_width = max(0, overlap_right - overlap_left)
        overlap_height = max(0, overlap_top - overlap_bottom)
        overlap_area = overlap_width * overlap_height

        total_area = area_A + area_B - overlap_area
        return total_area