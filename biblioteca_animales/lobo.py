from animal import Animal

class Lobo(Animal):
    def hacer_sonido(self):
        return f"{self.nombre} dice: ¡Auuu!"