"""Job1 / 2"""
# class Personne:
#     def __init__(self, age):
#         self._age = age

#     def AfficherAge(self):
#         print(f"age = {self._age}")

#     def Bonjour(self):
#         print("Hello")

#     def ModifierAge(self, a):
#         self._age = a

# class Eleve(Personne):
#     def __init__(self, age):
#         super().__init__(age)

#     def allerEnCours(self):
#         print("je vais en cours!")
    
# class Professeur(Personne):
#     def __init__(self, age, matiereEnseignee,):
#         super().__init__(age)
#         self.__matiereEnseignee = matiereEnseignee

#     def enseigner(self):
#         print(f"le cours de {self.__matiereEnseignee} va commencer!")

# p = Personne(14)
# e = Eleve(14)
# p = Professeur(40, "Math")

# e.AfficherAge()
# e.Bonjour()
# e.allerEnCours()
# e.ModifierAge(15)

# p.ModifierAge(40)
# p.enseigner()

"""Job3"""
# class Rectangle:
#     def __init__(self,longueur, largeur):
#         self.__longueur = longueur
#         self.__largeur = largeur
    
#     def perimetre(self):
#         return 2 * (self.__longueur + self.__largeur)

#     def surface(self):
#         return self.__longueur * self.__largeur

#     def getLongueur(self):
#         return self.__longueur

#     def getLargeur(self):
#         return self.__largeur

#     def setLongueur(self, longueur):
#         self.__longueur = longueur

#     def setLargeur(self, largeur):
#         self.__largeur = largeur

# class Parallelepipede(Rectangle):
#     def __init__(self, longueur, largeur, hauteur):
#         super().__init__(longueur, largeur)
#         self.__hauteur = hauteur

#     def volume(self):
#         return self.getLongueur() * self.getLargeur() * self.__hauteur
#         pass

#     def getHauteur(self):
#         return self.__hauteur

#     def setHauteur(self, hauteur):
#         self.__hauteur = hauteur

# print(f"{"-"*15}Rectangle{"-"*15}")
# r = Rectangle(10, 5)
# print(f"Longueur : {r.getLongueur()}")
# print(f"Largeur : {r.getLargeur()}")
# print(f"Perimetre : {r.perimetre()}")
# print(f"Surface : {r.surface()}")
# r.setLongueur(20)
# print(f"Nouvelle longueur : {r.getLongueur()}")

# print(f"{"-"*12}parallelepipede{"-"*12}")
# p = Parallelepipede(10, 5, 3)
# print(f"Volume : {p.volume()}")
# print(f"Longueur : {p.getLongueur()}")
# print(f"Largeur : {p.getLargeur()}")
# print(f"Perimetre : {p.perimetre()}")
# print(f"Surface : {p.surface()}")

"""Job4"""
# class Forme():
#     def aire(self):
#         return 0

# class Rectangle(Forme):
#     def __init__(self, largeur, hauteur):
#         super().__init__()
#         self.__largeur = largeur
#         self.__hauteur = hauteur

#     def aire(self):
#         return self.__largeur * self.__hauteur

# r = Rectangle(10, 5)
# print(f"Aire du rectangle : {r.aire()}")
"""job5"""
# class Cercle(Forme):
#     pi = 3.14159
#     def __init__(self, radius):
#         super().__init__()
#         self.__radius = radius

#     def aire(self):
#         return self.pi * self.__radius ** 2

# c = Cercle(10)
# print(f"Aire du cercle : {c.aire()}")

"""Job6"""
# class Vehicule:
#     def __init__(self, marque, modele, annee, prix):
#         self.__marque = marque
#         self.__modele = modele
#         self.__annee = annee
#         self.__prix = prix

#     def infoVehicule(self):
#         print(f"marque : {self.__marque}\nmodèle : {self.__modele}\nannée : {self.__annee}\nprix : {self.__prix}")

#     def Démarrer(self):
#         print("attention je roule")

# class Voiture(Vehicule):
#     def __init__(self, marque, modele, annee, prix, portes): 
#         super().__init__(marque, modele, annee, prix)
#         self.__portes = portes

#     def infoVehicule(self):
#         print()
#         super().infoVehicule()
#         print(f"portes : {self.__portes}")

#     def Démarrer(self):
#         print("Je roule sur 4 roue")

# class Moto(Vehicule):
#     def __init__(self, marque, modele, annee, prix, roue): 
#         super().__init__(marque, modele, annee, prix)
#         self.__roue = roue

#     def infoVehicule(self):
#         print()
#         super().infoVehicule()
#         print(f"roue : {self.__roue}")

#     def Démarrer(self):
#         print(f"Je roule sur {self.__roue} roue")


# v = Voiture("Toyota", "Yaris", 2020, 15000, 5)
# m = Moto("Yamaha", "1200 Vmax", 1987, 4500, 2)
# v.infoVehicule()
# m.infoVehicule()
# v.Démarrer()
# m.Démarrer()