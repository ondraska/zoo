import random
from datetime import datetime
class animal:
    def __init__(self, species:str, name:str, birthYear:int, checkupYear:int =0, energy:int =100):
        self.species = species
        self.name = name
        self.birtYear = birthYear
        self.checkupYear = checkupYear
        self.energy = energy
        pass

    def __str__(self):
        return f"{self.species} {self.name} {self.birtYear} {self.checkupYear} -energie: {self.energy}"

    def play(self):
        usage = random.randint(5, 20)
        self.usage = usage
        if self.energy >= usage:
            self.energy -= usage
            return f"{self.species} {self.name} spotřeboval {usage}% energie a zbívá mu {self.energy}"
        else:
            return f"nemáš dostatek energie svez se na simbovi nebo pumbovi"
        
    def feed(self):
        filled = 100 -self.energy
        self.energy = 100
        return f"{self.species} {self.name} snědl {filled} jídla a je plný"
    
    def vetCheck(self):
        if self.checkupYear < datetime.now().year:



animal1 = animal("Lev", "simba", 2016, 2020, 85)
animal2 = animal("prase", "pumba", 2021, 2025, 30)
animal3 = animal("surikata", "timo", 2020, 2024, 12)
print(animal1)
print(animal1.play())
print(animal2.play())
print(animal3.play())
print(animal3.feed())
print(animal3)