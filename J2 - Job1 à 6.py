"""job1"""

longueur = 10
largeur = 5

class Rectangle:
    def __init__(self, longueur, largeur):
        Rectangle.__longueur = longueur
        Rectangle.__largeur = largeur

    def _changement_valeur(self):
        self.__longueur = 8
        self.__largeur = 4

    def affiche_valeur(self):
        print(f"longeur {self.__longueur} largeur {self.__largeur}")

# r = Rectangle(longueur, largeur)
# r.affiche_valeur()
# r._changement_valeur()
# r.affiche_valeur()

"""job2"""

# titre,auteur,page = "Le petit prince","Saint-Exupéry",1

# class Livre:
#     def __init__(self, titre, auteur, page):
#         Livre.__titre,Livre.__auteur,Livre.__page = titre,auteur,page

#     def mutateur(self):
#         print(f"Voici la page actuelle {self.__page}")
#         self.accesseurs()

#     def accesseurs(self):
#         self.__page = input("Choisis une page : ")

#     def info_livre(self):
#         print(f"{self.__titre}, {self.__auteur}, page : {self.__page}")

# l = Livre(titre,auteur,page)
# l.info_livre()
# l.mutateur()

"""job3"""

titre,auteur,page,disponible = "Le petit prince","Saint-Exupéry",1,True

class Livre:

    def __init__(self, titre, auteur, page):
        Livre.__titre,Livre.__auteur,Livre.__page,Livre.disponible = titre,auteur,page,disponible

    # def mutateur(self):
    #     print(f"Voici la page actuelle {self.__page}")
    #     self.accesseurs()

    # def accesseurs(self):
    #     self.__page = input("Choisis une page : ")

    def info_livre(self):
        print(f"{self.__titre}, {self.__auteur}, page : {self.__page}")

    def emprunter(self):
        if self.disponible == True:
            input(f"Vous êtes obliger de prendre le livre {self.__titre} : ")
            self.disponible = False
            print("Vous avez pris le livre")
        else:
            print("le livre est déjà pris")

    def rendre(self):
        if self.disponible == False:
            input(f"Vous êtes obliger de rendre le livre {self.__titre} : ")
            self.disponible = True
            print("Vous avez rendu le livre")
        else:
            print("le livre est déjà rendu")

l = Livre(titre,auteur,page)
# l.info_livre()
# l.mutateur()
# l.emprunter()
# l.rendre()


"""Job4"""
nom,prenom,id,crédits = "Doe","John",145,0

# class Student:
#     def __init__(self, nom, prenom, id, crédits):
#         self.__nom = nom
#         self.__prenom = prenom
#         self.__id = id
#         self.__crédits = crédits

#     def _add_credit(self):
#         try:
#             value = int(input("how much credits to send? : "))
#         except ValueError:
#             print("que des chiffres")
#             return self._add_credit()

#         if value <= 0:
#             print("no negative number")
#             return self._add_credit()

#         self.__crédits += value
#         print(f"you've send {value} credits")

#     def _info_student(self):
#         print(f"Name : {self.__nom}, Surname : {self.__prenom}, ID : {self.__id}, Crédits : {self.__crédits}")

class Student:
    def __init__(self, nom, prenom, id, credits):
        self.__nom = nom
        self.__prenom = prenom
        self.__id = id
        self.__credits = credits
        self.__level = self.__studentEval()

    # méthode privée
    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 50:
            return "Passable"
        else:
            return "Insuffisant"

    def add_credit(self):
        try:
            value = int(input("Combien de crédits ajouter ? : "))
        except ValueError:
            print("Que des chiffres")
            return self.add_credit()

        if value <= 0:
            print("Pas de nombre négatif")
            return self.add_credit()

        self.__credits += value
        self.__level = self.__studentEval()

    def studentInfo(self):
        print(
            f"Nom : {self.__nom}\n"
            f"Prénom : {self.__prenom}\n"
            f"ID : {self.__id}\n"
            f"Niveau : {self.__credits} ({self.__level})"
        )

# s = Student(nom,prenom,id,crédits)
# s.studentInfo()
# s.add_credit()
# s.add_credit()
# s.add_credit()
# s.studentInfo()

"""Job5"""
class voiture:
    __marque = "BMW"
    __modele = "RS6"
    __année = 2016
    __kilométrage = 5048
    __reservoir = 50
    __lock = False

    def en_marche(self):
        print("AVANT",self.__kilométrage, "KM", self.__reservoir, "L")
        if self.__lock == False:
            while self.__lock == False:
                self.__reservoir -= 5
                self.__kilométrage += 5
                self.verifier_plein()
        print("APRES",self.__kilométrage, "KM", self.__reservoir, "L")
        self.demarrer

    def verifier_plein(self):
        if self.__reservoir < 5:
            self.__lock = True
        else:
            self.__lock = False

    def demarrer(self):
        self.verifier_plein()
        if self.__lock == True:
            print("faite un plein d'essence")
        else:
            self.__lock = False
            self.en_marche()

# v = voiture()
# v.demarrer()

"""job6"""
class Commande:
    def __init__(self):
        self.__liste_de_plats_commandés = []
        self.__liste_de_plats_existant = [
            ('lasagna', 8.0),
            ('coca', 2.0),
            ('pizza', 10.0),
            ('salade', 5.0),
            ('pasta', 7.5)
        ]
        self.__numéro_de_commande = 0
        self.__status_de_la_commande = 0
        self.__tva = 0.2

    def ajouter_plats_commander(self):
        plat = input("Enregistrez un plat à la commande : ").strip().lower()
        if any(p[0] == plat for p in self.__liste_de_plats_existant):
            self.__liste_de_plats_commandés.append(plat)
            print(f"{plat} ajouté à la commande.")
        else:
            print(f"{plat} n'existe pas dans le menu.")

    def suprimer_plats_commander(self):
        plat = input("Supprimez un plat à la commande : ").strip().lower()
        if plat in self.__liste_de_plats_commandés:
            self.__liste_de_plats_commandés.remove(plat)
            print(f"{plat} a été supprimé de la commande.")
        else:
            print(f"{plat} n'est pas dans la commande.")


    def afficher_commande(self):
            if not self.__liste_de_plats_commandés:
                print("Aucun plat dans la commande.")
                return

            print("Plats commandés :")
            for plat_cmd in self.__liste_de_plats_commandés:
                # récupérer le prix HT depuis le tuple
                prix_HT = next(p[1] for p in self.__liste_de_plats_existant if p[0] == plat_cmd)
                prix_TTC = prix_HT * (1 + self.__tva)
                print(f"- {plat_cmd} : {prix_HT:.2f} € HT, {prix_TTC:.2f} € TTC")

c = Commande()
c.ajouter_plats_commander()
c.afficher_commande()
c.suprimer_plats_commander()
c.afficher_commande()