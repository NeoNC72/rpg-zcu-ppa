from character import Character
from weapon import Weapon

class RPG:
    """
    RPG representuje RPG hru
    @Author: perutek
    @Date: 27.11.2023
    """
    def input_character(self) -> Character:
        """
        Načte postavu z stdin a vrátí ji

        Returns:
            načtená postava
        """
        name = input("Zadejte jmeno: ")
        try:
            strength = int(input("Zadejte silu: "))
        except ValueError:
            print(f"Neplatná síla ({strength}) :/, nastavuji na 1")
            strength = 1
        try:
            agility = int(input("Zadejte obratnost: "))
        except ValueError:
            print(f"Neplatná obratnost ({agility}) :/, nastavuji na 1")
            agility = 1
        try:
            vitality = int(input("Zadejte vitalitu: "))
        except ValueError:
            print(f"Neplatná vitalita ({vitality}) :/, nastavuji na 1")
            vitality = 1
        return Character(name, strength, agility, vitality)
    
    def input_weapon(self) -> Weapon|None:
        """
        Načte zbraň z stdin a vrátí ji

        Returns:
            načtená zbraň
        """
        name = input("Zadejte jmeno zbrane: ")
        if name == "":
            return None
        try:
            attack = int(input("Zadejte silu zbrane: "))
        except ValueError:
            print(f"Neplatná síla ({attack}) :/, nastavuji na 1")
            attack = 1
        try:
            defense = int(input("Zadejte obranu zbrane: "))
        except ValueError:
            print(f"Neplatná obrana ({defense}) :/, nastavuji na 1")
            defense = 1
        
        return Weapon(name, attack, defense)
    
    def equip_character(self, character:Character, left:Weapon|None, right:Weapon|None) -> None:
        """
        Dá postavě zbraňě do ruky
        """
        character.take_weapon(left, Character.HAND_LEFT)
        character.take_weapon(right, Character.HAND_RIGHT)

    def fight(self, character1:Character, character2:Character) -> Character:
        """
        Souboj dvou postav dokud jedna nezemře

        Args:
            character1: první postava
            character2: druhá postava

        Returns:
            vítězná postava
        """
        
        while character1.is_alive() and character2.is_alive():
            character2.defend(character1.attack())
            if character2.is_alive():
                character1.defend(character2.attack())
        
        if character1.is_alive():
            return character1
        else:
            return character2

    def run(self) -> None:
        """
        Spustí hru a vypíše vítěze
        """
        char1:Character = self.input_character()
        ch1w1:Weapon|None = self.input_weapon()
        ch1w2:Weapon|None = self.input_weapon()

        char2:Character = self.input_character()
        ch2w1:Weapon|None = self.input_weapon()
        ch2w2:Weapon|None = self.input_weapon()

        self.equip_character(char1, ch1w1, ch1w2)
        self.equip_character(char2, ch2w1, ch2w2)

        postava:Character = self.fight(char1, char2)
        print(f"Vitez: {postava}")


if __name__ == "__main__":
    rpg = RPG()
    rpg.run()