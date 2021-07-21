class Animal:
    def __init__ (self, multicellular, heterotrophic, canMove):
        self.multicellular = multicellular
        self.heterotrophic = heterotrophic
        self.canMove = canMove

class Mammal(Animal):
    def __init__(self, multicellular, heterotrophic, canMove, hasHair, warmBlooded, mammaryGlands):
        super().__init__(multicellular, heterotrophic, canMove) 
        self.hasHair = hasHair
        self.warmBlooded = warmBlooded
        self.mammaryGlands = mammaryGlands

class Amphibians(Animal):
    def __init__(self, multicellular, heterotrophic, canMove, smoothSkin, coldBlooded, feterlizeExternaly):
        super().__init__(multicellular, heterotrophic, canMove) 
        self.smoothSkin = smoothSkin
        self.coldBlooded = coldBlooded
        self.feterlizeExternaly = feterlizeExternaly

class Reptiles(Animal):
    def __init__(self, multicellular, heterotrophic, canMove, hasScales, coldBlooded, feterlizeExternaly):
        super().__init__(multicellular, heterotrophic, canMove) 
        self.hasScales = hasScales
        self.coldBlooded = coldBlooded
        self.feterlizeExternaly = feterlizeExternaly

class Birds(Animal):
    def __init__(self, multicellular, heterotrophic, canMove, hasFeathers, warmBlooded, layEggs):
        super().__init__(multicellular, heterotrophic, canMove) 
        self.hasFeathers = hasFeathers
        self.warmBlooded = warmBlooded
        self.layEggs = layEggs

class Insects(Animal):
    def __init__(self, multicellular, heterotrophic, canMove, hasExoskeleton, compoundEyes, pairOfAntennae):
        super().__init__(multicellular, heterotrophic, canMove) 
        self.hasExoskeleton = hasExoskeleton
        self.compoundEyes = compoundEyes
        self.pairOfAntannae = pairOfAntennae                                    