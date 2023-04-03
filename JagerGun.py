class Weapon:
    def __init__(self, name, damage, fire_rate, ammo_capacity):
        self.name = name
        self.damage = damage
        self.fire_rate = fire_rate
        self.ammo_capacity = ammo_capacity

class FourSixCCarbine(Weapon):
    def __init__(self):
        super().__init__("416-C Carbine", 42, 740, 30)

    def shoot(self):
        print("Bang!")

    def reload(self):
        print("Reloading...")


