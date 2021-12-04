# Rectangle that is represented as a list [x1, y1, x2, y2], where (x1, y1) is the coordinates of its top-left corner, and (x2, y2) is the coordinates of its bottam-right corner. 
# Now two rectangles overlap if the area of their intersection is positive.
# Two rectangles that only touch at the corner or edges do not overlap.Check in O(1) Time complexity and O(1) Space complexity that both rectangle overlap or not 
# Asked in : GoldmanSachs, Expedia, OLA

class Point: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
# Returns true if two rectangles(S, P) and (S1, P1) overlap   
def checkOverlapRectangle(S, P, S1, P1): 
    #Practise Yourself :  Write your code Here 
  
if __name__ == "__main__": 
    S = Point(0, 10) 
    P = Point(10, 0) 
    S1 = Point(5, 5) 
    P1 = Point(20, 0) 
  
    if(checkOverlapRectangle(S, P, S1, P1)): 
        print("Rectangles Overlap") 
    else: 
        print("Rectangles Don't Overlap") 
