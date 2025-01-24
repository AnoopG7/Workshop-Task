class Cylinder:

  def _init_(self, radius, height): 
        self.radius = radius
        self.height = height
        
  def vol(self, h, r ):
    return 3.14 * h * r ** 2
        
    def Area(self):
      return 2 * 3.14 * self.radius * (self.radius + self.height)
  
a = Cylinder()
volume=a.vol(10,20)
print("The volume of the cylinder is ", volume)
are=a.Area(5,7)
print("The area of the cylinder is ", are)
    

