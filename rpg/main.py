from hero import Hero
from mage import Mage
from archer import Archer
from assasin import Assasin
from monster import Monster

# summon hero hero nya
print("=== MULAI GUILD PARTY ===")
alucard = Hero("alucard",80, 100, 100, "Warrior")
alok = Mage("Alok", 85, 100, 100)
layla = Archer("Layla", 83, 100, 100)
hayabusa = Assasin("Hayabusa", 90, 100, 100)
print("")

# summon monster
print("=== SUMMON MONSTER ===")
turtle = Monster("Turtle", 250, 300)


print("=== MULAI GUILD PARTY ===")
guild_party = [
    alucard,
    alok,
    layla,
    hayabusa
]

# print(f"Welcome to Mobile Legends")
# print("[Hayabusa] Ayo serang Turtle!")
# print(f"Hp alucard : {alucard.get_hp()}")

# hayabusa.critical(turtle)
# print(turtle)
running = True
while running:
    print(turtle)
    print("1.Attack, 2.Heal, 3. Exit")

    aksi = int(input("pilih aksi"))
    if aksi == 1:
        dmg = 10
        alucard.attack(turtle)
        hayabusa.attack(turtle)
        layla.attack(turtle)
        alok.attack(turtle)
        turtle.damaged(dmg * 4)
        if (turtle.hp <= 0):
            print("Turtle telah tereliminasi")
            running = False

    elif aksi == 2:
        alok.heal(hayabusa,10)

    elif aksi == 3:
        running = False




