class Animal:
    def __init__(self, name, weight=0):
        self.name = name
        self.weight = weight

    def feed(self):
        self.weight += 1

    def voise(self):
        animal_voise = {Cow:'мууу',
                  Goose: 'гагага',
                  Sheep: 'беее',
                  Chicken:'ко-ко-ко',
                  Goat:'бэээ',
                  Duck:'кря-кря'
                  }
        for k,v in animal_voise.items():
            if type(self) == k:
                return v


class Bird:
    def __init__(self, name, weight=0, eggs=0):
        self.eggs = eggs
        self.name = name
        self.weight = weight

    def collect_eggs(self):
        if self.eggs != 0:
            self.eggs -= 1
        else:
            print('Нечего собирать')


class Givemilk:
    def __init__(self, name, weight=0, milk=0):
        self.milk = milk
        self.name = name
        self.weight = weight

    def collect_milk(self):
        if self.milk != 0:
            self.milk -= 1
        else:
            print('Нечего собирать')


class Goose(Animal, Bird):
    def __init__(self, name, weight=0, eggs=0):
        self.eggs = eggs
        super().__init__(name, weight)



class Cow(Animal, Givemilk):
    def __init__(self, name, weight=0, milk=0):
        self.milk = milk
        super().__init__(name, weight)



class Sheep(Animal):
    def __init__(self, name, weight=0, wool=0):
        self.wool = wool
        super().__init__(name, weight)

    def collect_wool(self):
        if self.wool != 0:
            self.wool -= 1
        else:
            print('Нечего собирать')



class Chicken(Animal, Bird):
    def __init__(self, name, weight=0, eggs=0):
        self.eggs = eggs
        super().__init__(name, weight)



class Goat(Animal, Givemilk):
    def __init__(self, name, weight=0, milk=0):
        self.milk = milk
        super().__init__(name, weight)


class Duck(Animal, Bird):
    def __init__(self, name, weight=0, eggs=0):
        self.eggs = eggs
        super().__init__(name, weight)



gray_goose = Goose('Серый', 4, 5)
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
    list_animals = [
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
    for animal in list_animals:
        weight_sum += animal.weight
        if animal.weight > weight_default:
            weight_default = animal.weight
            favorite_animal = animal.name
    return f'Общий вес: {weight_sum}. Самое тяжелое животное: {favorite_animal}'

print(weight_total_and_heaviest())

def print_all_metods_animals():
    list_animals = [
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
    for animal in list_animals:
        print(f'{animal.name} издает звук {animal.voise()}')
        print(f'Его вес до кормешки:{animal.weight}')
        animal.feed()
        print(f'Его вес после кормешки:{animal.weight}')
        print()
print_all_metods_animals()