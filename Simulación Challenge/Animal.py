class Animal:
    def __init__(self, especie, color):
        self.especie = especie
        self.color = color
        self.edad = 0

    def CumplirAnios(self):
        self.edad += 1
        return self.edad
    
