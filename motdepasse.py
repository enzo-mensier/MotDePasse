import getpass
import re

# Fonction de vérification des critères CNIL
def verifier_restrictions(mot_de_passe):
    restrictions = []

    # Vérification de la longueur minimale (ex. 12 caractères)
    if len(mot_de_passe) < 12:
        restrictions.append("Le mot de passe doit contenir au moins 12 caractères.")

    # Vérification d'une majuscule
    if not re.search(r'[A-Z]', mot_de_passe):
        restrictions.append("Le mot de passe doit contenir au moins une majuscule.")

    # Vérification d'un chiffre
    if not re.search(r'[0-9]', mot_de_passe):
        restrictions.append("Le mot de passe doit contenir au moins un chiffre.")

    # Vérification d'un caractère spécial
    if not re.search(r'[@$!%*?&]', mot_de_passe):
        restrictions.append("Le mot de passe doit contenir au moins un caractère spécial.")

    return restrictions

# Demande du mot de passe masqué
mot_de_passe = getpass.getpass("Veuillez entrer votre mot de passe : ")

# Vérification des restrictions
restrictions_non_respectees = verifier_restrictions(mot_de_passe)

# Affichage des restrictions non respectées
if restrictions_non_respectees:
    print("\nLe mot de passe ne respecte pas les critères suivants :")
    for restriction in restrictions_non_respectees:
        print(f"- {restriction}")
else:
    print("\nLe mot de passe respecte toutes les restrictions CNIL.")
    