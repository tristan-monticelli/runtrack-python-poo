class Part:
    def __init__(self,name,material):
        self.name = name
        self.material = material

    def change_material(self, new_material):
        self.material = new_material

    def __str__(self):
        return self.material, self.name
    
class Ship(Part):
    def __init__(self, name, material):
        super().__init__(name, material)
        self.__parts = Part
        self.history = []
    
    def Display_state(self):
        print(self.__parts)
    
    def replace_part(self, part_name, new_part):
        part_name = new_part
        self.history.append("Part replaced")

    def change_part(self, part_name, new_material):
        part_name = new_material
        self.history.append("Part changed")

    def Display_history(self):
        print(self.history)

class RacingShip(Ship):
    def __init__(self, name, material):
        super().__init__(name, material)
        self.speed = 0
        self.max_speed = 100
    
    def Display_speed(self):
        print(self.speed)

    def speedy(self):
        if speed >= 100:
            print(f"bateau déjà à {self.speed} km/h")
        else:
            speed += 33
            print(f"bateau à {self.speed} km/h")

def boucle():
    bateau = RacingShip("Bateau", "Bois")
    while True:
        choix = input("1 = change part, 2 = replace part, 3 = speed, 4 = stop, 5 = history : ")
        if choix == "1":
            part_name = input("Nom de la piece : ")
            new_material = input("Nouveau materiau : ")
            bateau.change_part(part_name, new_material)
        elif choix == "2":
            part_name = input("Nom de la piece : ")
            new_part = input("Nouvelle piece : ")
            bateau.replace_part(part_name, new_part)
        elif choix == "3":
            bateau.speedy()
        elif choix == "4":
            print("Arret")
            break
        elif choix == "5":
            bateau.Display_history()
        else:
            print("Choix invalide")

boucle()