from hero import Hero # panggil class hero

class Assasin(Hero):
    def __init__(self, name, level, hp, mana):
        # super() = memanggil parent (class Hero)
        # set role secara Assasin secara default
        super().__init__(name, level, hp, mana, role="Assasin")       

    def critical(self, target):
        dmg = 80
        target.hp -= dmg
        print(f"{self.name} menggunakan : Knight shadow")
        print(f"👿 {target.name} terkena {dmg} DMG !\n")