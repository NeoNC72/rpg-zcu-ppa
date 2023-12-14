from weapon import Weapon

class Character:
    """
    Character representuje postavu v RPG hre

    @Author: perutek
    @Date: 27.11.2023
    """
    HAND_LEFT:int = 0
    HAND_RIGHT:int = 1
    """
    Konstanty pro ruce
    """
    def __init__(self, name:str, strength:int, agility:int, vitality:int) -> None:
        self.__name :str = name
        self.__strength:int= strength
        self.__agility:int = agility
        self.__vitality:int = vitality
        self.__right_hand:Weapon|None = None
        self.__left_hand:Weapon|None = None

    def __weaponattack(self) -> int:
        if self.__left_hand is not None and self.__right_hand is not None:
            return self.__left_hand.attack + self.__right_hand.attack
        else:
            if self.__left_hand is not None:
                return self.__left_hand.attack
            elif self.__right_hand is not None:
                return self.__right_hand.attack
            else:
                return 0
    
    def __weapondefence(self) -> int:
        if self.__left_hand is not None and self.__right_hand is not None:
            return self.__left_hand.defense + self.__right_hand.defense
        else:
            if self.__left_hand is not None:
                return self.__left_hand.defense
            elif self.__right_hand is not None:
                return self.__right_hand.defense
            else:
                return 0

    def __defence(self) -> int:
        return self.__agility + self.__weapondefence()


    def attack(self) -> int:
        """
        Vrací hodnotu útoku postavy

        Returns: 
            hodnota útoku
        """
        return self.__strength + self.__weaponattack()
            
    def defend(self, attack:int) -> int:
            """
            Spočítá strátu životů po útoku

            Args:
                attack: hodnota útoku
            
            Returns:
                rozdíl mezi útokem a obranou
            """
            if attack < self.__defence():
                return 0
            change :int= attack - self.__defence()
            self.__vitality = self.__vitality - change
            return change
        
    def is_alive(self) -> bool:
        """
        Zjišťuje, jestli je postava naživu
        
        Returns:
            True, pokud je postava naživu, jinak False
        """
        return self.__vitality > 0
    
    def take_weapon(self, weapon:Weapon|None, hand:int) -> bool:
            """
            Dá postavě zbraň do ruky pokud v ní nic není

            Args:
                weapon: zbraň
                hand: ruka, do které se má zbraň dát (Character.LEFT_HAND (0) = levá, Character.RIGHT_HAND (1) = pravá)
            
            Returns:
                True, pokud se zbraň podařilo dát do ruky, jinak False
        
            """
            if hand == self.HAND_LEFT:
                if self.__left_hand == None:
                    self.__left_hand = weapon
                    return True
                else:
                    return False
            elif hand == self.HAND_RIGHT:
                if self.__right_hand == None:
                    self.__right_hand = weapon
                    return True
                else:
                    return False
            else:
                return False

    def __str__(self) -> str:
        return f"{self.__name} [{self.__vitality}] ({self.attack()}/{self.__defence()})"