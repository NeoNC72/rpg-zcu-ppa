class Weapon:
    
    """
    Weapon representuje zbraň v RPG hře
    
    @Author: perutek
    @Date: 27.11.2023
    """
    
    def __init__(self, name:str, attack:int, defense:int) -> None:
        self.__name:str = name
        self.__attack:int = attack
        self.__defense:int = defense

    @property
    def attack(self) -> int:
        """
        Vrací hodnotu útoku zbraně
        """
        return self.__attack

    @property
    def defense(self) -> int:
        """
        Vrací hodnotu obrany zbraně
        """
        return self.__defense

    def __str__(self) -> str:
        return f"{self.__name} [{self.attack}/{self.defense}]"