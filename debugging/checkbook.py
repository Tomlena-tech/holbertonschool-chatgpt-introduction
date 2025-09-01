#!/usr/bin/python3

class Checkbook:
    """
    Classe pour gérer un carnet de chèques simple.
    
    Cette classe permet de gérer un solde bancaire avec des opérations
    de base comme les dépôts, les retraits et la consultation du solde.
    """
    
    def __init__(self):
        """
        Initialise un nouveau carnet de chèques.
        
        Paramètres:
        -----------
        Aucun
        
        Retourne:
        ---------
        None
        """
        self.balance = 0.0
    
    def deposit(self, amount):
        """
        Effectue un dépôt sur le compte.
        
        Ajoute le montant spécifié au solde actuel et affiche
        le montant déposé ainsi que le nouveau solde.
        
        Paramètres:
        -----------
        amount : float
            Le montant à déposer (doit être positif)
        
        Retourne:
        ---------
        None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))
    
    def withdraw(self, amount):
        """
        Effectue un retrait du compte.
        
        Soustrait le montant spécifié du solde si les fonds sont suffisants.
        Affiche un message d'erreur si les fonds sont insuffisants.
        
        Paramètres:
        -----------
        amount : float
            Le montant à retirer (doit être positif)
        
        Retourne:
        ---------
        None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))
    
    def get_balance(self):
        """
        Affiche le solde actuel du compte.
        
        Paramètres:
        -----------
        Aucun
        
        Retourne:
        ---------
        None
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Fonction principale qui gère l'interface utilisateur.
    
    Crée une instance de Checkbook et permet à l'utilisateur
    d'effectuer des opérations via un menu interactif.
    
    Paramètres:
    -----------
    Aucun
    
    Retourne:
    ---------
    None
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            amount = float(input("Enter the amount to deposit: $"))
            cb.deposit(amount)
        elif action.lower() == 'withdraw':
            amount = float(input("Enter the amount to withdraw: $"))
            cb.withdraw(amount)
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
