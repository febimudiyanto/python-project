class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distance(self,other):
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5
c = Coordinate(3,4)
origin = Coordinate(0,0)

print("koordinat asal = ("+str(origin.x)+","+str(origin.y)+")")
print("koordinat c = ("+str(c.x)+","+str(c.y)+")")
print("jarak = ",c.distance(origin))
