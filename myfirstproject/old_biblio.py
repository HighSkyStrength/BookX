#Accueil au service
print("Bienvenue sur le service de Bibliothèka.")
#Inscription
username = input("Pour continuer, veuillez créer un compte, choisissez votre pseudo : ")
password = input("Veullez ensuite choisir votre mot de passe, sachant qu'il contenir au minimum 8 caractères : ")
password_lenght = len(password)
if password_lenght < 8:
    print("Mot de passe pas assez long")
    password: input("Vueillez ensuite choisir votre mot de passe, sachant qu'il contenir au minimum 8 caractères : ")
else:
    print("Mot de passe parfait")

print("Tu es donc "+ username + " et tu as choisi comme mot de passe: " + password)
answer = input("Confirmez-vous ? Réponse simple attendue, Oui ou Non, avec le respect des majuscules: ")
while answer != "Oui":
    username = input("Pour continuer, veuillez créer un compte, choisissez votre pseudo : ")
    password = input("Veullez ensuite choisir votre mot de passe, sachant qu'il contenir au minimum 8 caractères : ")
    password_lenght = len(password)
    if password_lenght < 8:
        print("Mot de passe pas assez long")
        password: input(
            "Vueillez ensuite choisir votre mot de passe, sachant qu'il contenir au minimum 8 caractères : ")
    else:
        print("Mot de passe parfait")

#Menu
    print("Tu es donc " + username + " et tu as choisi comme mot de passe: " + password)
    answer = input("Confirmez-vous ? Réponse simple attendue, Oui ou Non, avec le respect des majuscules: ")
book_list = ["Alice aux pays des merveilles   ", " Alice au pays de la mer", "  Alice à la jungle", "   Alice va voir Alice"]

print("Si vous vous avoir la liste des livres disponible, tapez 'liste', si vous voulez avoir des infos, tapez infos, si vous voulez emprunter un livre, tapez 'emprunt' : ")
choice = input(" ")
while choice != "emprunt":
    choice = input(" ")
    if choice == "liste":
        print("Nous avons de disponible  {} ".format(book_list))
    elif choice == "infos":
        print("Programme fait par Shiga")

print("Donc vous voulez empruntez un livre...")
#Menu d'emprunt
connection = input("Veuillez d'abord vous connecter, entrer votre pseudo ")

while connection != username :
    print("Pseudo erroné")
    connection = input("Veuillez vous connecter, entrer votre pseudo ")
connection = input("À présent, veuillez entrer votre mot de passe")
while connection != password:
    print("Mot de passe erroné")
    connection = input("Veuillez re-entrer votre mot de passe")

print("Connexion autorisée")
choixe = input("Tapez 'liste de livre' pour voir la liste totale des livres disponibles, vous pouvez toujours retourner au menu en écrivant 'retour' : ")
if choixe == "liste de livre":
    print("Liste : {}".format(book_list))
elif choixe == "retour":
    print("Retour au menu")
    print(
        "Si vous vous avoir la liste des livres disponible, tapez 'liste', si vous voulez avoir des infos, tapez infos, si vous voulez emprunter un livre, tapez 'emprunt' : ")
    choice = input(" ")
    while choice != "emprunt":
        choice = input(" ")
        if choice == "liste":
            print("Nous avons de disponible  {} ".format(book_list))
        elif choice == "infos":
            print("Programme fait par Shiga")

    print("Donc vous voulez empruntez un livre...")
