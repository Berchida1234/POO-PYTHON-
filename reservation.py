from datetime import datetime

class Reservation:
    """
    Classe représentant une réservation de livre dans la bibliothèque.
    """

    def __init__(self, utilisateur, livre):
        """
        Constructeur de la classe Reservation.
        
        Paramètres :
        - utilisateur : instance de la classe Utilisateur qui fait la réservation
        - livre : instance de la classe Livre réservé
        """
        self.utilisateur = utilisateur  # L'utilisateur qui a réservé le livre
        self.livre = livre              # Le livre réservé
        self.date_reservation = datetime.now()  # Date et heure exactes de la réservation

        # Rendre le livre indisponible dès qu'il est réservé
        self.livre.disponible = False

        # Optionnel : associer cette réservation au livre pour faciliter le suivi
        self.livre.reservation = self

    def afficher_details(self):
        """
        Affiche les détails de la réservation.
        Retourne une chaîne formatée avec :
        - Nom de l'utilisateur
        - Titre du livre
        - ISBN du livre
        - Date de réservation (formatée)
        """
        return f"Réservation : Utilisateur '{self.utilisateur.nom}', " \
               f"Livre '{self.livre.titre}' (ISBN: {self.livre.isbn}), " \
               f"Date: {self.date_reservation.strftime('%Y-%m-%d %H:%M')}"
