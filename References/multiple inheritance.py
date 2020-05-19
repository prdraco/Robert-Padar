class Fruit():
    def __init__(self, season, color, name):
        self.season = season
        self.color = color
        self.name = name

class CitrusFruits(Fruit):
    def __init__(self, season, color, name):
        super().__init__(self, season, name)
        super().__init__(self, color, name)

    def __repr__(self):
        return f'CitrusFruits({self.season, self.name, self.color})'

fruit1 = CitrusFruits('winter', 'yellow', 'lemon')
print(fruit1.color)