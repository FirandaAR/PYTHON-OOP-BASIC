from hero import Hero # panggil class hero

class Archer(Hero):
    def __init__(self, name, level, hp, mana):
        # super() = memanggil parent (class Hero)
        # set role secara Archer secara default
        super().__init__(name, level, hp, mana, role="Archer")       

    def critical(self, target):
        dmg = 80
        print(f"{self.name} menggunakan : PANAH MEBARAA!")
        print(f"👿 {target.name} terkena {dmg} DMG !")
        self.attack(target)
        target.damaged(dmg)