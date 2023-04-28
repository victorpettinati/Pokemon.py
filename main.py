import json
import os
import random
from combat import Combat


def main_menu():
    print("Menu principal :")
    print("1. Lancer une partie")
    print("2. Ajouter un Pokémon")
    print("3. Accéder au Pokédex")
    print("4. Quitter")

    choice = int(input("Entrez le numéro de votre choix : "))
    return choice

def start_game():
    if not os.path.exists("pokemon.json"):
        print("Aucun Pokémon enregistré. Veuillez ajouter des Pokémon avant de lancer un combat.")
        return

    with open("pokemon.json", "r") as f:
        pokemons = json.load(f)

    print("Choisissez votre Pokémon :")
    for i, pokemon in enumerate(pokemons):
        print(f"{i + 1}. {pokemon['name']}")

    while True:
        try:
            choice = int(input("Entrez le numéro de votre choix : ")) - 1
            if 0 <= choice < len(pokemons):
                break
            else:
                print("Le numéro entré n'est pas dans la liste. Veuillez réessayer.")
        except ValueError:
            print("Veuillez entrer un nombre correspondant au numéro du Pokémon dans la liste.")

    chosen_pokemon = pokemons[choice]

    opponent_pokemon = random.choice(pokemons)
    while opponent_pokemon == chosen_pokemon:
        opponent_pokemon = random.choice(pokemons)

    battle = Combat(chosen_pokemon, opponent_pokemon)
    battle.fight()

def add_pokemon():
    name = input("Entrez le nom du Pokémon : ")
    lvl = int(input("Entre le niveau de votre Pokemon : "))
    hp = int(input("Entrez les points de vie du Pokémon : "))
    attack = int(input("Entrez l'attaque du Pokémon : "))
    defense = int(input("Entrez la défense du Pokémon : "))
    type = input("Entrez le type du Pokémon : ")

    new_pokemon = {
        "name": name,
        "lvl": lvl,
        "hp": hp,
        "attack": attack,
        "defense": defense,
        "type": type,
        
    }

    if not os.path.exists("pokemon.json"):
        with open("pokemon.json", "w") as f:
            json.dump([new_pokemon], f)
    else:
        with open("pokemon.json", "r") as f:
            pokemons = json.load(f)
        pokemons.append(new_pokemon)
        with open("pokemon.json", "w") as f:
            json.dump(pokemons, f)

    print(f"{name} a été ajouté au Pokédex.")

def view_pokedex():
    if not os.path.exists("pokemon.json"):
        print("Aucun Pokémon enregistré.")
    else:
        with open("pokemon.json", "r") as f:
            pokemons = json.load(f)

        print("Pokédex :")
        for pokemon in pokemons:
            print(f"{pokemon['name']} - Niveau:{pokemon['lvl']}, Type: {pokemon['type']}, HP: {pokemon['hp']}, Attaque: {pokemon['attack']}, Défense: {pokemon['defense']}")

if __name__ == "__main__":
    while True:
        choice = main_menu()
        if choice == 1:
            start_game()
        elif choice == 2:
            add_pokemon()
        elif choice == 3:
            view_pokedex()
        elif choice == 4:
            break
        else:
            print("Choix invalide, veuillez réessayer.")
