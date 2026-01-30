class Hero:
    # Self = diri nya sendiri / internal
    # init = dipanggil pertama kali
    def __init__(self, name, level, hp, mana, role):
        # nama__ attr : private
        # hanya bisa diakses dengan getter
        self.name = name
        self.level = level
        self.__hp = hp
        self.mana = mana
        self.role = role
        print(f"Hero [{self.role}] {self.name} telah di summon!")
    
    # fungsi mengganti print object daru bentuk memori menjadi format string
    def __str__(self):
        status = "🟢 HIDUP"
        if self.__hp == 0:
            status = "☠️ MATI"
        
        return f"[{self.role}] {self.name} | HP : {self.hp} | STATUS: {status}"
        
    def damaged(self, damage):
        self.hp -= damage
        print(F"{self.name} terkena {damage} damage!\n")
        if self.hp == 0:
            print(f"☠️ Hero {self.name} telah terliminasi\n")
    
    def attack(self, enemy):
        # suatu objek bisa di lempar, kal disini yan di lempar (disini nama)
        print(f"⚔️  {self.name} menyerang {enemy.name}")

    def heal(self, target, amount):
        target.hp += amount
        print(f"💊 Hero {self.name} mendapat kan heal +{amount}")
    
    def critical(self, target):
        print(f"👿 {target.name} terkena {damage} DMG!")
    
    # getter: mengambir attribut yang privat
    def get_hp(self):
        return self.__hp

    def set_hp(self, add_hp):
        # tambahkan falidasi jangan sampai lewat max 100 hp
        self.__hp += add_hp
