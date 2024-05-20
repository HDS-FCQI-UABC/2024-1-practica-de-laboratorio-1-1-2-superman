from animal import Animal

class Zorro(Animal):
    def hacer_sonido(self):
        return f"{self.nombre} dice: ¡Rauu, Rauu!"