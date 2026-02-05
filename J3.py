"""job1"""
# class Ville:
#     def __init__(self, nom, habitant):
#         self.__nom = nom
#         self.__habitant = habitant


# class Personne:
#     def __init__(self, nom, age, ville):
#         self.__nom = nom
#         self.__age = age
#         self.__ville = ville

#     def ajouterPopulation(self):
#         # Accéder directement à l'attribut privé de Ville via le nom mangling
#         self.__ville._Ville__habitant += 1
#         print(f"La population de {self.__ville._Ville__nom} est maintenant {self.__ville._Ville__habitant}")


# # Créons une ville
# paris = Ville("Paris", 1000000)
# marseille = Ville("Marseille", 861635)

# # Créons une personne habitant Paris
# p1 = Personne("John", 45, paris)
# p2 = Personne("Myrtille", 4, paris)
# p3 = Personne("Chloé", 18, marseille)

# # Appelons la méthode pour augmenter la population
# p1.ajouterPopulation()
# p2.ajouterPopulation()
# p3.ajouterPopulation()

"""job2"""
# class CompteBancaire:
#     def __init__(self, numéro_de_compte, nom, prenom, solde, decouvert):
#         self.__numéro_de_compte = numéro_de_compte
#         self.__nom = nom
#         self.__prenom = prenom
#         self.__solde = solde
#         self.__decouvert = decouvert

#     def afficher(self):
#         print(f"numéro du compte : {self.__numéro_de_compte} \n nom : {self.__nom}\n prenom : {self.__prenom}\n solde : {self.__solde}\n")
        
#     def afficherSolde(self):
#         print(f"solde actuel : {self.__solde}")

#     def transfer(self, receveur, montant):
#         self.__solde -= montant
#         receveur.__solde += montant
#         print(f"solde de {self.__nom} : {self.__solde} envoyer {montant} à {receveur.__solde}")

#     def versement(self, montant):
#         print(f"versement de {montant}")
#         self.__solde += montant

#     def retrait(self, montant):
#         if self.__solde > montant:
#             self.__solde -= montant
#             print(f"retrait de {montant}")
#         else:
#             value = self.agios(montant)
#             if value:
#                 self.__solde -= value
    
#     def agios(self, montant):
#         if self.__decouvert:
#             value = montant * 1.2
#             print(f"agios de 20% nouveau montant à {value} au lieu de {montant}")
#             return value
#         else:
#             value = False
#             print(f"paiment bloquer solde manquant {montant - self.__solde}")
#             return value

# c1 = CompteBancaire(1001, "John", "Doe", 100, True)
# c2 = CompteBancaire(1002, "John", "Doe2", 100, False)
# c1.afficher()
# c2.transfer(c1, 100)
# c1.versement(100)
# c1.afficherSolde()
# c1.retrait(200)
# c1.afficherSolde()



"""job3"""
# class Tache:
#     def __init__(self, titre, description, status):
#         self.titre = titre
#         self.description = description
#         self.status = status

#     def __str__(self):
#         return f"[{self.status}] {self.titre} : {self.description}"

# class ListeDeTaches():
#     def __init__(self):
#         self.__taches = []
    
#     def ajouterTache(self, tache):  
#         self.__taches.append([tache.titre, tache.description, tache.status])
#         self.afficherListe()
        
#     def supprimerTache(self):
#         max = len(self.__taches)
#         i = 0
#         value = input("Titre de la tache à suprimer : ")
#         while i < max:
#             if self.__taches[i][0] == value:
#                 self.__taches.pop(i)
#                 print("Tache Suprimer")
#                 self.afficherListe()
#                 return
#             i += 1
#             print("1")
#         print("non trouver")
    
#     def marquerCommeFinie(self):
#         max = len(self.__taches)
#         i = 0
#         value = input("Titre de la tache fini : ")
#         while i < max:
#             if self.__taches[i][0] == value:
#                 if self.__taches[i][2] == "En cours":
#                     self.__taches[i][2] = "Completer"
#                     print("Tache marquer comme completer")
#                     self.afficherListe()
#                     return
#                 else:
#                     print("tache déjà marquer comme completer")
#                     return
#             i += 1
#         print("non trouver")
    
#     def afficherListe(self):
#         max = len(self.__taches)
#         i = 0
#         compressed_list = []
#         while i < max:
#             compressed_list.append(self.__taches[i][0])
#             i += 1
#         print(compressed_list)

#     def filterListe(self):
#         max = len(self.__taches)
#         i = 0
#         value = input("1/ En cours et 2/ Completer : ")
#         filtered_list = []
#         while i < max:
#             if value == "En cours" or "1":
#                 if self.__taches[i][2] == "En cours":
#                     filtered_list.append(self.__taches[i][0])
#             elif value == "Completer" or "2":
#                 if self.__taches[i][2] == "completer":
#                     filtered_list.append(self.__taches[i][0])
#             else:
#                 print("Mal écrit / pas de status à trier")
#             i += 1
#         print(filtered_list)

# t1 = Tache("Pytorch","Apprendre pytorch en 1 semaine","En cours")
# t2 = Tache("Pytorch","Apprendre pytorch en 1 semaine","En cours")
# l = ListeDeTaches() 
# l.ajouterTache(t1)
# l.ajouterTache(t2)
# l.supprimerTache()
# l.marquerCommeFinie()
# l.filterListe()

"""job4"""
# class Joueur:
#     def __init__(self,nom,numéro,position,buts_marques,passe_decisives,carton_jaune,carton_rouge):
#         self.__nom = nom
#         self.__numéro = numéro
#         self.__position = position
#         self.__buts_marques = buts_marques
#         self.__passe_decisives = passe_decisives
#         self.__carton_jaune = carton_jaune
#         self.__carton_rouge = carton_rouge

#     def marquerUnBut(self):
#         self.__buts_marques += 1
#         pass

#     def effectuerUnePasseDecisive(self):
#         self.__passe_decisives += 1
#         pass

#     def recevoirUnCartonJaune(self):
#         self.__carton_jaune += 1
#         if self.__carton_jaune == 2:
#             self.recevoirUnCartonRouge()
#         pass

#     def recevoirUnCartonRouge(self):
#         self.__carton_jaune = 0
#         self.__carton_rouge += 1
#         pass

#     def afficherStatistiques(self):
#         print(f"nom : {self.__nom}\nnuméro : {self.__numéro}\nposition : {self.__position}\nbuts marqués : {self.__buts_marques}\npasses décisives {self.__passe_decisives}\ncarton jaune : {self.__carton_jaune}\ncarton rouge : {self.__carton_rouge}")

# class Equipe:
#     def __init__(self, nom, liste_joueurs=[]):
#         self.__nom = nom
#         if liste_joueurs is None:
#             self.__liste_joueurs = []
#         else:
#             self.__liste_joueurs = liste_joueurs
    
#     def ajouterJoueur(self, joueur):
#         self.__liste_joueurs.append(joueur)

#     def AfficherStatistiquesJoueurs(self):
#         i = 0
#         max = len(self.__liste_joueurs)
#         print(f"[{self.__nom}]")
#         while i < max:
#             print("-"*32)
#             self.__liste_joueurs[i].afficherStatistiques()
#             print("-"*32)                                                  
#             i += 1 
#         pass
    
#     def mettreAJourStatistiquesJoueur(self, nom_joueur, action):
#         for joueur in self.__liste_joueurs:
#             if joueur._Joueur__nom == nom_joueur:
#                 if action == "but":
#                     joueur.marquerUnBut()
#                 elif action == "passe":
#                     joueur.effectuerUnePasseDecisive()
#                 elif action == "carton_jaune":
#                     joueur.recevoirUnCartonJaune()
#                 elif action == "carton_rouge":
#                     joueur.recevoirUnCartonRouge()
#                 return
#         print(f"Joueur {nom_joueur} non trouvé dans l'équipe")

# j1 = Joueur("Mbappé", 10, "Attaquant", 0, 0, 0, 0)
# j2 = Joueur("Griezmann", 7, "Milieu", 0, 0, 0, 0)
# j3 = Joueur("Ramos", 4, "Défenseur", 0, 0, 0, 0)
# j4 = Joueur("Donnarumma", 1, "Gardien", 0, 0, 0, 0)

# j5 = Joueur("Haaland", 9, "Attaquant", 0, 0, 0, 0)
# j6 = Joueur("De Bruyne", 17, "Milieu", 0, 0, 0, 0)
# j7 = Joueur("Walker", 2, "Défenseur", 0, 0, 0, 0)
# j8 = Joueur("Ederson", 31, "Gardien", 0, 0, 0, 0)

# equipe1 = Equipe("PSG")
# equipe2 = Equipe("Manchester City")

# equipe1.ajouterJoueur(j1)
# equipe1.ajouterJoueur(j2)
# equipe1.ajouterJoueur(j3)
# equipe1.ajouterJoueur(j4)

# equipe2.ajouterJoueur(j5)
# equipe2.ajouterJoueur(j6)
# equipe2.ajouterJoueur(j7)
# equipe2.ajouterJoueur(j8)

# print("=== STATISTIQUES AVANT LE MATCH ===")
# equipe1.AfficherStatistiquesJoueurs()
# print()
# equipe2.AfficherStatistiquesJoueurs()



# equipe1.mettreAJourStatistiquesJoueur("Mbappé","but")
# equipe1.mettreAJourStatistiquesJoueur("Griezmann","carton_jaune")
# equipe1.mettreAJourStatistiquesJoueur("Griezmann","carton_jaune") #Il à donc un carton rouge (2 carton jaune = 1 carton rouge)

# equipe2.mettreAJourStatistiquesJoueur("Haaland","but")
# equipe2.mettreAJourStatistiquesJoueur("Haaland","but")
# equipe2.mettreAJourStatistiquesJoueur("Haaland","passe")


# print("=== STATISTIQUES APRES LE MATCH ===")
# equipe1.AfficherStatistiquesJoueurs()
# print()
# equipe2.AfficherStatistiquesJoueurs()




"""Job5"""
import random
import time
class Personnage:
    def __init__(self, nom, damage, health, chance, victory):
        self._nom = nom
        self._damage = int(damage)
        self._health = int(health)
        self._chance = int(chance)
        self._victory = int(victory)

    def attaquer(self, cible):
        value = random.randint(0, 100)
        if value < (100 - cible._chance):
            cible._health -= self._damage
            print(f"{self._nom} attaque {cible._nom} et inflige {self._damage} dégats!")
            self.__checkWin(cible)
        else:
            print(f"{self._nom} rate son attaque contre {cible._nom}!")

    def __checkWin(self, cible):
        if cible._health <= 0:
            self._victory += 1
            return
        
class Jeu:
    def __init__(self, niveau, joueur, adversaire):
        self._niveau = niveau
        self.joueur = joueur
        self.adversaire = adversaire

    def choisirNiveau(self):
        value = input(f"choisir sont niveau de difficulté : \n1/ Facile\n2/ Normal\n3/ Difficile\n")
        if value == "1":
            self._niveau = "Facile"
            print("Difficulté choisis [Facile]")
            self.adversaire = Personnage("adversaire", 25/2, 25*2, 25*0.75, 0)
        elif value == "2":
            self._niveau = "Normal"
            print("Difficulté choisis [Normal]")
            self.adversaire = Personnage("adversaire", 33/2, 33*2, 33*0.75, 0)
        elif value == "3":
            self._niveau = "Difficile"
            print("Difficulté choisis [Difficile]")
            self.adversaire = Personnage("adversaire", 40/2, 40*2, 40*0.75, 0)
        else:
            print("Choix uniquement pris en compte [1,2,3]")
            time.sleep(1)
            self.choisirNiveau()
        
    def ChoisirStat(self):
        point = int(100)
        damage = int(input(f"point à attribué en dégats (1 point = 0.5) ({point} restant) : "))
        point -= damage
        health = int(input(f"point à attribué en health (1 point = 2) ({point} restant) : "))
        point -= health
        chance = int(input(f"point à attribué en chance (1 point = 0.75) ({point} restant) : "))
        point -= chance
        if point >= 0:
            self.joueur = Personnage("joueur", damage/2, health*2, chance*0.75, 0)
            return
        else:
            print("Tu à attribué plus de point que tu en a")
            time.sleep(1)
            self.ChoisirStat()

    def commencerCombat(self):
        round = 0
        while self.joueur._health > 0 and self.adversaire._health > 0:
            print(f"\n=== C'est ton tour! ===")
            self.joueur.attaquer(self.adversaire)
            if self.adversaire._health <= 0:
                print("🎉 Victoire!!")
                LancerJeu()

            time.sleep(1)
            print(f"\n=== Tour de l'adversaire! ===")
            self.adversaire.attaquer(self.joueur)
            if self.joueur._health <= 0:
                print("💀 Défaite!")
                LancerJeu()

            time.sleep(1)
            round += 1
            print(f"\n=== Récapitulatifs Round {round} ===")
            print(f"Vie du joueur : {self.joueur._health} HP")
            print(f"Vie de l'adversaire : {self.adversaire._health} HP")

            time.sleep(2)

def LancerJeu():
    jeu = Jeu("none", "none", "none")

    jeu.ChoisirStat()
    jeu.choisirNiveau()

    print("\n=== LE COMBAT COMMENCE ===\n")
    time.sleep(2)

    jeu.commencerCombat()

LancerJeu()