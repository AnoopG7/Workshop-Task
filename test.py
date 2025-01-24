class Cylinder:
  def vol(self, h, r ):
    return 3.14 * h * r ** 2
  
a = Cylinder()
volume=a.vol(10,20)
print("The volume of the cylinder is ", volume)