class Cylinder:
    def _init_(self, radius, height): 
        self.radius = radius
        self.height = height
        
    def Area(self):
      return 2 * 3.14 * self.radius * (self.radius + self.height)