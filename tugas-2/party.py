class Hero:
    # Self = diri nya sendiri / internal
    # init = dipanggil pertama kali
    def __init__(self, name, role, hp, hero_type="hero"):
        self.name = name
        self.hp = hp
        self.role = role
        self.hero_type = hero_type
        self.max_hp = 280
        print(f"[{self.role}] {self.name} Memasuki land of dawn")

    # fungsi mengganti print object daru bentuk memori menjadi format string
    def __str__(self):
        status = "🟢 HIDUP"
        if self.hp <= 0:
            status = "☠️ MATI"
        
        return f"[{self.name}] | HP : {self.hp} | STATUS: {status}"

    def is_alive(self):
        return self.hp > 0


    def attack(self, enemy, damage):
        # suatu objek bisa di lempar, kal disini yan di lempar (disini nama)
        if not self.is_alive():
            print(f"{self.name} tidak bisa menyerang (sudah mati)" )
            return
        
        enemy.hp -= damage
        print(f"⚔️  {self.name} menyerang {enemy.name} sebesar {damage} damage!")
        print(f"{enemy.name} terkena damage {damage}\n")
        if enemy.hp <= 0:
            print(f"☠️  {enemy.name} Telah tereliminasi")
        
        if enemy.hero_type == "boss":
            if enemy.hp > 0 and enemy.hp <= enemy.max_hp / 2:
                print("👿 Lord telah berevolusi menjadi lebih kuat!\n")
        pass 
    
    def damaged(self, damage):
        self.hp -= damage
        print(F"{self.name} terkena {damage} damage!\n")
        if self.hp <= 0:
            print(f"☠️ Hero {self.name} telah terliminasi\n")
        pass
    
    def heal(self, amount):
        self.hp += amount
        print(f"💊 Hero {self.name} mendapat kan heal +{amount}")
    
    def critical(self, target):
        damage = 50
        target.hp -= damage
        print(f"⚔️  {self.name} menyerang {target.name} sebesar 50 critical DMG!")
        print(f"👿 {target.name} terkena {damage} DMG!\n")

        if target.hp <= 0:
            print(f"☠️  {target.name} Telah tereliminasi")
        
        if target.hero_type == "boss":
            if target.hp > 0 and target.hp <= target.max_hp / 2:
                print("👿 Lord telah berevolusi menjadi lebih kuat!\n")
        pass 

    def ulti(self, target, ultimate):
        damage = 100
        target.hp -= damage
        print(f"⚔️  {self.name} menggunakan ulti [{ultimate}]")
        print(f"{target.name} terkena {damage} damage!\n")



print("PARTY MENUJU GLORY")
print("==================")
Hayabusa = Hero(f"Hayabusa", "Jungler", 150)
Claude = Hero(f"Claude", "Marksman", 100)
Valentina = Hero(f"Valentina", "Mage", 150)
Grock = Hero(f"Grock", "Roam", 150)
print("")
print("==================")
print("Memasuki Mid game")
Turtle = Hero(f"Turtle", "Buff", 180, "normal")
Hayabusa.attack(Turtle, 80)
Valentina.attack(Turtle, 50)
Turtle.attack(Hayabusa, 20)
Hayabusa.attack(Turtle, 50)

print("")
print("=== Memasuki late game ===")
print("")
Lord = Hero(f"Lord", "Boss", 280, "boss")
print("")
print("[Hayabusa] Ayo serang Lord!")
print(f"[Hayabusa] Retri siap!\n")
print("Semuanya telah berkumpul di lord!")
Hayabusa.attack(Lord, 100)
Valentina.critical(Lord)
Lord.attack(Hayabusa, 100)
Lord.attack(Valentina, 80)
Valentina.heal(50)
print("")
print(Lord)
print("")
print(Hayabusa)
print("")
print(Valentina)
print("")
print(Claude)
print("")
Claude.ulti(Lord, "Blazing Duet")
print(Lord)
print("")
Hayabusa.attack(Lord, 80)
print("Hayabusa Telah membunuh Lord")

