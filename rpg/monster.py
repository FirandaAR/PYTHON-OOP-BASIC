class Monster:
    # Self = diri nya sendiri / internal
    # init = dipanggil pertama kali
    def __init__(self, name, hp, mana):
        self.name = name
        self.hp = hp
        self.mana = mana
        print(f"Monster {self.name} telah di summon!")
    
    # fungsi mengganti print object daru bentuk memori menjadi format string
    def __str__(self):
        status = "🟢 HIDUP"
        if self.hp == 0:
            status = "☠️ MATI"
        
        return f"[Monster] {self.name} | HP : {self.hp} | STATUS: {status}"
        
    def damaged(self, damage):
        self.hp -= damage
        print(F"{self.name} terkena {damage} damage!\n")
        if self.hp == 0:
            print(f"☠️ Hero {self.name} telah terliminasi\n")
    