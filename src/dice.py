from random import randrange

class Dice:
    """Кубики Котокафе"""
    #Nota bene: value_char потребуется для занесения в объект House.
    #Это позволит выводить дом (ASCII-art)
    #с меньшим количеством преобразований.
    VALUES = ['HOUSE', 'BALL', 'BUTTERFLY', 'BOWL', 'PILLOW', 'MOUSE']
    VALUES_SHORT = ['H', 'A', 'U', 'O', 'P', 'M']

    def __init__(self, value = 1):
        if value not in range(1,7):
            raise ValueError
        self.value = value
        self.value_char = Dice.VALUES_SHORT[self.value-1]
        
    def __repr__(self):
        return f'{self.value}'

    def __eq__(self, other):
        return self.value == other.value and self.value_char == other.value_char

    def save(self):
        return repr(self)

    @staticmethod
    def load(text: str):
        return Dice(value = int(text[0]))

    def roll(self):
        self.value = randrange(1, 7)
        self.value_char = Dice.VALUES_SHORT[self.value-1]
