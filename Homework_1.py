
# Общие параметры (кличка, голос, вес)

class Goose:
    def __init__(self, name, weight=0, eggs=0):
        self.name = name
        self.vote = 'га-га-га'
        self.weight = weight
        self.eggs = eggs
    def feed(self):
        self.weight += 1
    def collect_eggs(self):
        if self.eggs != 0:
            self.eggs -= 1
        else:
            print('Нечего собирать')

class Cow:
    def __init__(self, name, weight=0, milk=0):
        self.name = name
        self.vote = 'муууу'
        self.weight = weight
        self.milk = milk
    def feed(self):
        self.weight += 1
    def collect_milk(self):
        if self.milk != 0:
            self.milk -= 1
        else:
            print('Нечего собирать')


class Sheep:
    def __init__(self, name, weight=0, wool=0):
        self.name = name
        self.vote = 'беее'
        self.weight = weight
        self.wool = wool
    def feed(self):
        self.weight += 1
    def collect_wool(self):
        if self.wool != 0:
            self.wool -= 1
        else:
            print('Нечего собирать')



class Chicken:
    def __init__(self, name, weight=0, eggs=0):
        self.name = name
        self.vote = 'ко-ко-ко'
        self.weight = weight
        self.eggs = eggs
    def feed(self):
        self.weight += 1
    def collect_eggs(self):
        if self.eggs != 0:
            self.eggs -= 1
        else:
            print('Нечего собирать')




class Goat:
    def __init__(self, name, weight=0, milk=0):
        self.name = name
        self.vote = 'мееее'
        self.weight = weight
        self.milk = milk
    def feed(self):
        self.weight += 1
    def collect_milk(self):
        if self.milk != 0:
            self.milk -= 1
        else:
            print('Нечего собирать')




class Duck:
    def __init__(self, name, weight=0, eggs=0):
        self.name = name
        self.vote = 'кря кря'
        self.weight = weight
        self.eggs = eggs
    def feed(self):
        self.weight += 1
    def collect_eggs(self):
        if self.eggs != 0:
            self.eggs -= 1
        else:
            print('Нечего собирать')



gray_goose = Goose('Серый', 4, 6)
white_goose = Goose('Белый', 3, 4)
mania_cow = Cow('Манька', 200, 15)
barashek_sheep = Sheep('Барашек', 50, 4)
kudri_sheep = Sheep('Кудрявый', 45, 6)
ko_ko_cheecken = Chicken('Ко-Ко', 2, 3)
kuka_cheecken = Chicken('Кукареку', 1.5, 4)
roga_goat = Goat('Рога', 15, 2)
kopita_goat = Goat('Копыта', 17, 3)
kria_duck = Duck('Кряква', 4, 1)

def weight_total_and_heaviest():
    list_weight = [
        gray_goose,
        white_goose,
        mania_cow,
        barashek_sheep,
        kudri_sheep,
        ko_ko_cheecken,
        kuka_cheecken,
        roga_goat,
        kopita_goat,
        kria_duck,
    ]
    weight_default = 0
    weight_sum = 0
    for animal in list_weight:
        weight_sum += animal.weight
    for animal in list_weight:
        if animal.weight > weight_default:
            weight_default = animal.weight
            favorite_animal = animal.name
    return f'Общий вес: {weight_sum}. Самое тяжелое животное: {favorite_animal}'

print(weight_total_and_heaviest())



