from hero import Hero # panggil class hero

class Warrior(Hero):
    def __init__(self, name, level, hp, mana):
        # super() = memanggil parent (class Hero)
        # set role secara warrior secara default
        super().__init__(name, level, hp, mana, role="Warrior")       

    def critical(self, target):
        dmg = 80
        print(f"👿 {target.name} terkena {dmg} DMG !")
        self.attack(target)
        target.damaged(dmg)