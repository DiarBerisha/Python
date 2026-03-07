class Vertebrate:
    def __init__(self, backbone=True):
        self.has_backbone = backbone

    def vertebratre_info(self):
        print("Vertebrates have a backbone")

class Aquatic:
    def __init__(self, habitat="Water"):
        self.habitat = habitat

    def aquatic_info(self):
        print("Aquatic animals live in water.")


class Fish(Vertebrate,Aquatic):
    def __init__(self, species, backbone=True,habitat="Water"):
        super().__init__(backbone=backbone)
        self.habitat=habitat
        self.species = species

    def fish_info(self):
        print(f"The {self.species} is a type of fish thats found in {self.habitat}")
    def swim(self):
        print("the fish is swimming.")

goldfish = Fish("Goldfish")
print(goldfish.has_backbone)
print(goldfish.habitat)
print(goldfish.fish_info())
print(goldfish.swim())
print(goldfish.aquatic_info())
print(goldfish.vertebratre_info())