# __main__.py
from gato import Gato
from perro import Perro
from lobo import Lobo

# Crear una instancia de Gato
mi_gato = Gato("Felix")

# Llamar al método hacer_sonido
print(mi_gato.hacer_sonido())

# Crear una instancia de Gato
mi_perro = Perro("Bon")

# Llamar al método hacer_sonido
print(mi_perro.hacer_sonido())

# Crear una instancia de Lobo
mi_lobo = Lobo("Jordan Belfort")

# Llamar al método hacer_sonido
print(mi_lobo.hacer_sonido())
