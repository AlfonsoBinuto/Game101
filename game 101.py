
import random


life_hero = 50

life_vilain = 50

potions_de_hero = 3

while life_hero > 0 and life_vilain > 0:

    print(f"Il vous reste {life_hero} point de vie\n")
    
    print(f"Il reste a Vilain {life_vilain} point de vie\n")

    
    choix = input("Attack (1) ou potion (2) ?")


    if not choix.isdigit():
        continue

    if int(choix) == 1:
        print("-" * 35)
        attaque_de_hero = random.randint(5, 15) 
        print(f"Vous avez inflige {attaque_de_hero} dégats ")
        life_vilain -= attaque_de_hero

        attaque_de_vilain = random.randint(5, 15) 
        print(f"Vilain a inflige {attaque_de_vilain} dégats ")
        life_hero -= attaque_de_vilain
        print("-" * 35)

    elif int(choix) == 2 and potions_de_hero > 0:
        print("-" * 35)
        soin_de_potion = random.randint(15,50)
        print(f"la potion vous a fait recuperer {soin_de_potion} points de vie ")
        life_hero += soin_de_potion
        life_hero = min(life_hero, 50)
        potions_de_hero -= 1 
        print(f"Potions restantes : {potions_de_hero}\n")

        attaque_de_vilain = random.randint(5, 15) 
        print(f"Vilain a inflige {attaque_de_vilain} dégats ")
        life_hero -= attaque_de_vilain
        print("-" * 35)
        
         
    elif int(choix) == 2 and potions_de_hero == 0:
        print("-" * 35)
        print("Pas de potion\n" )
        attaque_de_vilain = random.randint(5, 15) 
        print(f"Vilain a inflige {attaque_de_vilain} dégats ")
        life_hero -= attaque_de_vilain
        print("-" * 35)
      

if life_hero <= 0  :
    print("Vous etes DEAD ")

elif life_vilain <= 0 :
    print("Bravo, Vilain est DEAD")






