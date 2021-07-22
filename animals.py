class Animal:
    def __init__ (self, name, __multicellular, __heterotrophic, __canMove):
        self.name = name
        self.multicellular = __multicellular
        self.heterotrophic = __heterotrophic
        self.canMove = __canMove

class Mammal(Animal):
    def __init__(self,name, multicellular, heterotrophic, canMove, hasHair, warmBlooded, mammaryGlands):
        super().__init__(name, multicellular, heterotrophic, canMove) 
        self.hasHair = hasHair
        self.warmBlooded = warmBlooded
        self.mammaryGlands = mammaryGlands

    def feedYoungOnes(self): 
        if self.mammaryGlands:
            self.mammaryGlands = self.feedYoungOnes
        return  self.feedYoungOnes()

class Amphibians(Animal):
    def __init__(self,name,  multicellular, heterotrophic, canMove, smoothSkin, coldBlooded, feterlizeExternaly):
        super().__init__(name,  multicellular, heterotrophic, canMove) 
        self.smoothSkin = smoothSkin
        self.coldBlooded = coldBlooded
        self.feterlizeExternaly = feterlizeExternaly

class Reptiles(Animal):
    def __init__(self,name,  multicellular, heterotrophic, canMove, hasScales, coldBlooded, feterlizeExternaly):
        super().__init__(name, multicellular, heterotrophic, canMove) 
        self.hasScales = hasScales
        self.coldBlooded = coldBlooded
        self.feterlizeExternaly = feterlizeExternaly

    def swimEfficiently(self):
        if self.hasScales:
            self.hasScales = self.swimEfficiently
        return self.swimEfficiently() 

    def getname(self):
         return self.name

class Birds(Animal):
    def __init__(self,name,  multicellular, heterotrophic, canMove, hasFeathers, warmBlooded, layEggs):
        super().__init__(name, multicellular, heterotrophic, canMove) 
        self.hasFeathers = hasFeathers
        self.warmBlooded = warmBlooded
        self.layEggs = layEggs

    def canFly (self):
        self.canFly = True
        if self.hasFeathers: 
            self.hasFeathers = self.canFly
            return self.canFly

    def getname(self):
         return self.name

    def setname(self, newBir):
        self.name = newBir     

        newBir = Birds("Hawk", "multicellular","heterotrphic","canMove","hasFeathers","warmBlooded", "laysEggs")


       

class Insects(Animal):
    def __init__(self,name,  multicellular, heterotrophic, canMove, hasExoskeleton, compoundEyes, pairOfAntennae):
        super().__init__(name, multicellular, heterotrophic, canMove) 
        self.hasExoskeleton = hasExoskeleton
        self.compoundEyes = compoundEyes
        self.pairOfAntannae = pairOfAntennae 


mam_1 = Mammal("elephant", "multicellular","heterotrphic","canMove","hasHair","warmBlooded", "mammaryGlands")
amp_1 = Amphibians("frog", "multicellular","heterotrphic","canMove","smoothSkin","coldBlooded", "feterlizeExternaly")
rep_1 = Reptiles("aligator", "multicellular","heterotrphic","canMove","hasScales","warmBlooded", "mammaryGlands")
bir_1 = Birds("eagle", "multicellular","heterotrphic","canMove","hasFeathers","warmBlooded", "laysEggs")
ins_1 = Insects("grasshoper", "multicellular","heterotrphic","canMove","hasExoskeleton","compoundEyes", "pairOfAntennae")


print(bir_1.getname())
