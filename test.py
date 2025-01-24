class Cylinder:
    def csa(self,h,r):
        return 2*3.14*r*h

b = Cylinder()
curve = b.csa(10,20)
print("The CSA of Cylinder is ",curve)
        