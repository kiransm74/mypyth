#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

class StarShip ():
    def __init__ (self, maxwarp):
        self.maxwarp=maxwarp
        self.nacelles=2

class ncc1701e (StarShip):
    def __init_ (self, holodeck, separator):
        super().__init__(self, 10)
        self.holodeck=True
        self.separator=True

ncc1=ncc1701e(7)
        
print(ncc1.maxwarp)
print(ncc1.holodeck)