from hero import Hero # panggil class hero

class Mage(Hero):
    def __init__(self, name, level, hp, mana):
        # super() = memanggil parent (class Hero)
        # set role secara mage secara default
        super().__init__(name, level, hp, mana, role="mage")       

    def critical(self, target):
        dmg = 50
        print(f"👿 {target.name} terkena {dmg} DMG !")
        self.attack(target)
        target.damaged(dmg)

    def cast_spell(self):
        dmg = 10
        print(f"{self.name} menggunakan magic attack")

