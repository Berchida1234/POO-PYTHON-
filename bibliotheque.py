from datetime import datetime 
class Bibliotheque:
    def __init__(self, nom):
        self.nom = nom 
        self.livres = {} 
        self.utilisateurs = {}  
        self.reservations = {}  
    def ajouter_livre(self, livre):
       
        if livre.isbn not in self.livres:
            self.livres[livre.isbn] = livre
            print(f"Livre '{livre.titre}' ajouté au catalogue.")
        else:
            print(f"Le livre avec l'ISBN {livre.isbn} est déjà dans le catalogue.")

    def supprimer_livre(self, isbn):
        if isbn in self.livres:
            del self.livres[isbn]
            print(f"Livre avec ISBN {isbn} supprimé du catalogue.")
           
            if isbn in self.reservations:
                del self.reservations[isbn]
        else:
            print(f"Aucun livre trouvé avec l'ISBN {isbn}.")

    def rechercher_livres(self, mot_cle):
        resultats = []
        mot_cle = mot_cle.lower()
        for livre in self.livres.values():
            if mot_cle in livre.titre.lower() or mot_cle in livre.auteur.lower():
                resultats.append(livre)
        return resultats

    def enregistrer_utilisateur(self, utilisateur):
        if utilisateur.id not in self.utilisateurs:
            self.utilisateurs[utilisateur.id] = utilisateur
            print(f"Utilisateur {utilisateur.nom} enregistré.")
        else:
            print(f"Un utilisateur avec l'ID {utilisateur.id} existe déjà.")

    def emprunter_livre(self, utilisateur_id, isbn):
        if utilisateur_id not in self.utilisateurs:
            print("Utilisateur non trouvé.")
            return
        if isbn not in self.livres:
            print("Livre non trouvé.")
            return

        utilisateur = self.utilisateurs[utilisateur_id]
        livre = self.livres[isbn]

        utilisateur.emprunter_livre(self, isbn)

    def retourner_livre(self, utilisateur_id, isbn):
        if utilisateur_id not in self.utilisateurs:
            print("Utilisateur non trouvé.")
            return
        if isbn not in self.livres:
            print("Livre non trouvé.")
            return

        utilisateur = self.utilisateurs[utilisateur_id]
        livre = self.livres[isbn]

        utilisateur.retourner_livre(self, isbn)

    def reserver_livre(self, utilisateur_id, isbn):
        if utilisateur_id not in self.utilisateurs:
            print("Utilisateur non trouvé.")
            return
        if isbn not in self.livres:
            print("Livre non trouvé.")
            return

        if isbn not in self.reservations:
            self.reservations[isbn] = []

      
        if utilisateur_id not in self.reservations[isbn]:
            self.reservations[isbn].append(utilisateur_id)
            print(f"Utilisateur {utilisateur_id} a réservé le livre {isbn}.")
        else:
            print("Vous avez déjà réservé ce livre.")

    def afficher_catalogue(self):
        print(f"\nCatalogue de la bibliothèque '{self.nom}':")
        for livre in self.livres.values():
            statut = "Disponible" if livre.disponible else "Indisponible"
            print(f"ISBN: {livre.isbn}, Titre: {livre.titre}, Auteur: {livre.auteur}, Statut: {statut}")

    def afficher_statistiques(self):
        print("\nStatistiques de la bibliothèque :")
        total_livres = len(self.livres)
        livres_disponibles = sum(1 for livre in self.livres.values() if livre.disponible)
        livres_empruntes = total_livres - livres_disponibles
        total_emprunts_actifs = sum(len(user.livres_empruntes) for user in self.utilisateurs.values())

        print(f"Nombre total de livres : {total_livres}")
        print(f"Nombre de livres disponibles : {livres_disponibles}")
        print(f"Nombre de livres empruntés : {livres_empruntes}")
        print(f"Nombre d'emprunts actifs : {total_emprunts_actifs}")

        top_livres = sorted(self.livres.values(), key=lambda x: x.nb_emprunts, reverse=True)[:5]
        print("\nTop 5 des livres les plus empruntés :")
        for livre in top_livres:
            print(f"{livre.titre} par {livre.auteur} (Emprunts : {livre.nb_emprunts})")

        users_penalises = [u for u in self.utilisateurs.values() if u.penalise]
        print(f"\nNombre d'utilisateurs pénalisés : {len(users_penalises)}")