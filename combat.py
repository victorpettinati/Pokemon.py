import random
import time

class Combat:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def calculate_type_multiplier(self, attacker_type, defender_type):
        type_effectiveness = {
            'Feu': {'Feu': 0.5, 'Eau': 0.5, 'Plante': 2, 'Normal': 1, 'Electrik': 1, 'Glace': 2, 'sol': 0.5, 'Roche': 1, 'Combat': 1, 'Psy': 1, 'Insecte': 2, 'Dragon': 0.5, 'Spectre': 1, 'Poison': 1},
            'Eau': {'Feu': 2, 'Eau': 0.5, 'Plante': 0.5, 'Normal': 1, 'Electrik': 1, 'Glace': 0.5, 'sol': 2, 'Roche': 2, 'Combat': 1, 'Psy': 1, 'Insecte': 1, 'Dragon': 0.5, 'Spectre': 1, 'Poison': 1},
            'Plante': {'Feu': 0.5, 'Eau': 2, 'Plante': 0.5, 'Normal': 1, 'Electrik': 1, 'Glace': 0.5, 'sol': 2, 'Roche': 2, 'Combat': 1, 'Psy': 1, 'Insecte': 0.5, 'Dragon': 0.5, 'Spectre': 1, 'Poison': 0.5},
            'Normal': {'Feu': 1, 'Eau': 1, 'Plante': 1, 'Normal': 1, 'Electrik': 1, 'Glace': 1, 'sol': 1, 'Roche': 0.25, 'Combat': 1, 'Psy': 1, 'Insecte': 1, 'Dragon': 1, 'Spectre': 0, 'Poison': 1},
            'Electrik': {'Feu': 1, 'Eau': 2, 'Plante': 1, 'Normal': 1, 'Electrik': 0.5, 'Glace': 1, 'sol': 0, 'Roche': 0, 'Combat': 1, 'Psy': 1,'Insecte': 1, 'Dragon': 1, 'Spectre': 1, 'Poison': 1},
            'Glace': {'Feu': 0.5, 'Eau': 0.5, 'Plante': 2, 'Normal': 1, 'Electrik': 1, 'Glace': 0.5, 'sol': 1, 'Roche': 2, 'Combat': 2, 'Psy': 1,'Insecte': 2, 'Dragon': 2, 'Spectre': 1, 'Poison': 1},
            'Sol': {'Feu': 2, 'Eau': 1, 'Plante': 0.5, 'Normal': 1, 'Electrik': 2, 'Glace': 1, 'sol': 1, 'Roche': 2, 'Combat': 1, 'Psy': 1,'Insecte': 1, 'Dragon': 1, 'Spectre': 1, 'Poison': 1},
            'Roche': {'Feu': 2, 'Eau': 1, 'Plante': 0.5, 'Normal': 1, 'Electrik': 2, 'Glace': 2, 'sol': 1, 'Roche': 0.5, 'Combat': 1, 'Psy': 1,'Insecte': 2, 'Dragon': 1, 'Spectre': 1, 'Poison': 1},
            'Combat': {'Feu': 1, 'Eau': 1, 'Plante': 1, 'Normal': 2, 'Electrik': 1, 'Glace': 2, 'sol': 1, 'Roche': 2, 'Combat': 1, 'Psy': 0.5,'Insecte': 1, 'Dragon': 1, 'Spectre': 0, 'Poison': 1},
            'Psy': {'Feu': 1, 'Eau': 1, 'Plante': 1, 'Normal': 1, 'Electrik': 1, 'Glace': 1, 'sol': 1, 'Roche': 1, 'Combat': 2, 'Psy': 0.5,'Insecte': 0.5, 'Dragon': 1, 'Spectre': 1, 'Poison': 2},
            'Insecte': {'Feu': 0.5, 'Eau': 1, 'Plante': 0.5, 'Normal': 1, 'Electrik': 1, 'Glace': 1, 'sol': 1, 'Roche': 0.5, 'Combat': 1, 'Psy': 2,'Insecte': 0.5, 'Dragon': 1, 'Spectre': 1, 'Poison': 1},
            'Dragon': {'Feu': 1, 'Eau': 1, 'Plante': 1, 'Normal': 1, 'Electrik': 1, 'Glace': 1, 'sol': 1, 'Roche': 1, 'Combat': 1, 'Psy': 1,'Insecte': 1, 'Dragon': 2, 'Spectre': 1, 'Poison': 1},
            'Spectre': {'Feu': 1, 'Eau': 1, 'Plante': 1, 'Normal': 1, 'Electrik': 1, 'Glace': 1, 'sol': 1, 'Roche': 1, 'Combat': 1, 'Psy': 1,'Insecte': 1, 'Dragon': 1, 'Spectre': 1, 'Poison': 1},
            'Poison': {'Feu': 1, 'Eau': 1, 'Plante': 2, 'Normal': 1, 'Electrik': 1, 'Glace': 1, 'sol': 1, 'Roche': 1, 'Combat': 1, 'Psy': 1,'Insecte': 0.5, 'Dragon': 1, 'Spectre': 1, 'Poison': 0.5},
        }

        return type_effectiveness[attacker_type][defender_type]

    def calculate_damage(self, attacker, defender):
        type_multiplier = self.calculate_type_multiplier(attacker['type'], defender['type'])
        damage = (attacker['attack'] - defender['defense'] // 2) * type_multiplier
        if damage < 0:
            damage = 0
        return damage

    def fight(self):
        print(f"{self.pokemon1['name']} VS {self.pokemon2['name']}\n")
        time.sleep(2)

        while self.pokemon1['hp'] > 0 and self.pokemon2['hp'] > 0:
            damage_dealt = self.calculate_damage(self.pokemon1, self.pokemon2)
            self.pokemon2['hp'] -= damage_dealt
            print(f"{self.pokemon1['name']} inflige {damage_dealt} points de dégâts à {self.pokemon2['name']}!")
            time.sleep(1)

            if self.pokemon2['hp'] <= 0:
                print(f"{self.pokemon2['name']} est K.O.!")
                print(f"{self.pokemon1['name']} gagne le combat!")
                break

            damage_dealt = self.calculate_damage(self.pokemon2, self.pokemon1)
            self.pokemon1['hp'] -= damage_dealt
            print(f"{self.pokemon2['name']} inflige {damage_dealt} points de dégâts à {self.pokemon1['name']}!")
            time.sleep(1)

            if self.pokemon1['hp'] <= 0:
                print(f"{self.pokemon1['name']} est K.O.!")
                print(f"{self.pokemon2['name']} gagne le combat!")
                break
