class Hero:
    # Self = diri nya sendiri / internal
    # init = dipanggil pertama kali
    def __init__(self, name, level, hp, mana, role):
        self.name = name
        self.level = level
        self.hp = hp
        self.mana = mana
        self.role = role
        print(f"Hero [{self.role}] {self.name} telah di summon!")
    
    # fungsi mengganti print object daru bentuk memori menjadi format string
    def __str__(self):
        status = "🟢 HIDUP"
        if self.hp == 0:
            status = "☠️ MATI"
        
        return f"[{self.name}] | HP : {self.hp} | STATUS: {status}"
        
    def damaged(self, damage):
        self.hp -= damage
        print(F"{self.name} terkena {damage} damage!\n")
        if self.hp == 0:
            print(f"☠️ Hero {self.name} telah terliminasi\n")
    
    def attack(self, enemy):
        # suatu objek bisa di lempar, kal disini yan di lempar (disini nama)
        print(f"⚔️  {self.name} menyerang {enemy.name}")

    def heal(self, amount):
        self.hp += amount
        print(f"💊 Hero {self.name} mendapat kan heal +{amount}")
    
    def critical(self, target):
        print(f"👿 {target.name} terkena {damage} DMG!")

# Panggil / summon hero-nya (buat objek nya)
# alucard = Hero("Alucard", 10, 100, 100, 150, "warrior")
# eudora = Hero("Eudora", 10, 80, 100, 150,)
# claude = Hero("Claude", 10, 120, 100, 150, "warrior")
# # print(alucard, eudora, claude)
# print("--- BATTLE START ---")
# alucard.attack(eudora)
# eudora.damaged(10)
# print("")
# # balas cuy
# eudora.attack(alucard)
# alucard.damaged(5)
# alucard.damaged(5)
# alucard.damaged(5)
# alucard.damaged(5)
# print(alucard)
# print(eudora)
# eudora.attack(alucard)
# alucard.damaged(80)
# alucard.heal(100)
# alucard.attack(eudora)
# eudora.damaged(90)
