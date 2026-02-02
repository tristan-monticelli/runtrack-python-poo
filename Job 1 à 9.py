import random

"""job1"""
class Operation:
    nombre1 = 1
    nombre2 = 2
    #Job3
    def addition():
        value = Operation.nombre1 + Operation.nombre2
        print(value)
    #Job3

o = Operation()
print(o)

"""job2"""
print(Operation.nombre1)
print(Operation.nombre2)

"""job3"""
#dans class job1
Operation.addition()

"""job4"""
class Personne:
    nom = "John"
    prenom = "Doe"
    def SePresenter():
        print("Je suis",Personne.nom, Personne.prenom)

Personne.SePresenter()

"""job5"""
class Point:
    x = 10
    y = 10
    
    def afficherLesPoints():
        print("x =",Point.x,"y =",Point.y)

    def afficherX():
        print("x =",Point.x)

    def afficherY():
        print("y =",Point.y)

    def ChangerX():
        try:
            x = int(input("Entre une valeur x : "))
        except(ValueError):
            print("Chiffre rond uniquement")
            
    def ChangerY():
        try:
            y = int(input("Entre une valeur y : "))
        except(ValueError):
            print("Chiffre rond uniquement")


Point.afficherLesPoints()
Point.afficherX()
Point.afficherY()
Point.ChangerX()
Point.ChangerY()
Point.afficherX()
Point.afficherY()

"""Job6"""
class Animal:
    age = 0
    prenom = "unknow"

    def vieillir():
        print("L'age de l'animal",Animal.age,"ans")
        Animal.age += 1
        print("L'age de l'animal",Animal.age,"ans")

    def nommer():
        Animal.prenom = input("Entrez le nom de l'Animal : ")
        print("L'animal se nomme : ", Animal.prenom)

Animal.vieillir()
Animal.nommer()

"""Job7"""
class Personnage:
    x = 0
    y = 0

    def deplacement():
        while (Personnage.x < 30) or (Personnage.y < 30):
            if random.randint(1,2) == 1:
                Personnage.x += random.randint(-10,10)
            else:
                Personnage.y += random.randint(-10,10)
        print ({"x = ",Personnage.x,"y = ",Personnage.y})

Personnage.deplacement()

"""Job8"""
class Cercle:
    PI = 3.141592653589793

    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon

    def circonference(self):
        return 2 * Cercle.PI * self.rayon

    def aire(self):
        return Cercle.PI * self.rayon ** 2

    def diametre(self):
        return 2 * self.rayon
    
    def afficherInfos(rayon):
        diametre = 2 * rayon
        circonference = 2 * Cercle.PI * rayon
        aire = Cercle.PI * rayon ** 2
        print("-" * 30)
        print(f"Rayon : {rayon}")
        print(f"Diamètre : {diametre}")
        print(f"Circonférence : {circonference}")
        print(f"Aire : {aire}")
        print("-" * 30)

Cercle.afficherInfos(4)
Cercle.afficherInfos(7)

class Produit:
    def CalculerPrixTTC(self, prixHT, TVA):
        prixTTC = prixHT * (1 + TVA / 100)
        return prixTTC

p = Produit()

def afficher(nom, prixHT, TVA):
    print(f"{nom} coûte {p.CalculerPrixTTC(prixHT, TVA)} en TTC")

afficher("Aspirateur", 255, 20)
afficher("TV oled", 2500, 20)
afficher("Bateau", 31000, 20)
afficher("Immeuble", 640000, 20)
afficher("Île Privée", 15450530, 20)