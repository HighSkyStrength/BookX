# Accueil au service
def accueil():
     print("Bienvenue sur le service de Bibliothèka.")
     inscription()

def inscription():
    global username
    global password
    username = input("Pour continuer, veuillez créer un compte, choisissez votre pseudo : ")
    password = input("Veullez ensuite choisir votre mot de passe, sachant qu'il contenir au minimum 8 caractères : ")
    password_lenght = len(password)
    if password_lenght < 8:
        print("Mot de passe pas assez long")
        password = input("Veuillez ensuite choisir votre mot de passe, sachant qu'il contenir au minimum 8 caractères :")
    else:
        print("Mot de passe parfait")
        confirmation()
def confirmation():
     print("Tu es donc " + username + " et tu as choisi comme mot de passe: " + password)
     answer = input("Confirmez-vous ? Réponse simple attendue, Oui ou Non, avec le respect des majuscules: ")
     if answer.upper() == "OUI":
           connexion()
     elif answer.upper() == "NON":
        inscription()
     else:
        print("Erreur")
        confirmation()

def connexion():
    print("Afin d'accéder à la suite....")
    connection = input("Veuillez d'abord vous connecter, entrer votre pseudo ")
    while connection != username:
        print("Pseudo erroné")
        connection = input("Veuillez vous connecter, entrer votre pseudo ")
    connection = input("À présent, veuillez entrer votre mot de passe")
    while connection != password:
        print("Mot de passe erroné")
        connection = input("Veuillez re-entrer votre mot de passe")

    print("Connexion autorisée")
    menu()

def menu():

    print("Si vous voulez avoir des infos, tapez 'infos', si vous voulez voir avec quel compte vous êtes connecté, tapez 'compte',  si vous voulez emprunter un livre et passer au menu d'emprunt tapez 'emprunt': ")
    choice = input("->")
    while choice != "emprunt":
        if choice == "infos":
            print("Programme fait par Shiga")
            choice = input("->")
        elif choice == "compte":
            print("Vous êtes connecté en étant "+ username+ " et avec comme mot de passe : ", password)
            choice = input("->")
        elif choice != "infos" and "compte" != choice:
            print("Erreur, veuillez vérifier l'orthographe de votre demande : ")
            choice = input("->")
    print("Donc vous voulez emprunter un livre...")
    emprunt()
global fantaisie_list
global aventure
global SF
global BD
global manga
global documentaire
global kids_books

def emprunt():
    print("Quel type de livre voulez-vous ? Choix possibles: Fantaisie, Aventure, SF, BD, Manga, Documaentaire, livre pour enfants.")
    rep_1 = "FANTAISIE"
    rep_2 = "AVENTURE"
    rep_3 = "SF"
    rep_4 = "BD"
    rep_5 = "MANGA"
    rep_6 = "DOCUMENTAIRE"
    rep_7 = "LIVRE POUR ENFANTS"
    fantaisie_list = ["Begin Fantasy I" , "Water Emblem" , "PhiBos" , "El Doredore"]
    aventure = ["Pékomon" , "Les Aventures de,Mi-loup et Thym-Thym"]
    SF = ["20 milles endroits sur la terre" , "Voyage à la ferme pas loin d'ici"]
    BD = ["Les Aventures de Mi-loup et Thym-Thym" , "Les Légendaire pas trop non plus"]
    manga = ["Shingeki no Hero Academia" , "Boku no Kyojin" , "One Slayer" , "Demon Piece"]
    documentaire = ["Les loups" , "les chiens" , "Le capitalisme"]
    kids_books = ["Martine à la mer !!" , "Franklin joue à Mario Kart" , "Martine fait une tartine"]
    answer = input("Votre choix : ")
    if answer.upper() not in [rep_1, rep_2, rep_3, rep_4, rep_5, rep_6, rep_7]:
        print("Suite Impossible")
        emprunt()
    if answer.upper() == rep_1:
        answer = input("Vous voulez donc des livres de style fantaisie ? [y/n]")
        if answer.upper() == "Y":
            fantaisie()
        elif answer.upper() == "N":
            emprunt()
    if answer.upper() == rep_2:
        answer = input("Vous voulez donc des livres de style aventure ? [y/n]")
        if answer.upper() == "Y":
            print(aventure)
        elif answer.upper() == "N":
            emprunt()
    if answer.upper() == rep_3:
        answer = input("Vous voulez donc des livres de style Sciences fiction ? [y/n]")
        if answer.upper() == "Y":
            print(SF)
        elif answer.upper() == "N":
            emprunt()
    if answer.upper() == rep_4:
        answer = input("Vous voulez donc des livres de style Bandes dessinées ? [y/n]")
        if answer.upper() == "Y":
            print(BD)
        elif answer.upper() == "N":
            emprunt()
    if answer.upper() == rep_5:
        answer = input("Vous voulez donc des livres de style Manga ? [y/n]")
        if answer.upper() == "Y":
            print(manga)
        elif answer.upper() == "N":
            emprunt()
    if answer.upper() == rep_6:
            answer = input("Vous voulez donc des livres de style documentaire ? [y/n]")
            if answer.upper() == "Y":
                print(documentaire)
            elif answer.upper() == "N":
                emprunt()
    if answer.upper() == rep_7:
            answer = input("Vous voulez donc des livres de style Kids Books ? [y/n]")
            if answer.upper() == "Y":
                print(kids_books)
            elif answer.upper() == "N":
                emprunt()
def fantaisie() : 
    global panier
    print(fantaisie_list)
    choix = input("Vous êtes sur la catégorie 'FANTAISIE', si vous voulez retourner au menu des types, tapez 'menu', si vous voulez continuer votre emprunt, tapez 'emprunt' ")
    if choix.upper == "MENU" :
        emprunt()
    elif choix.upper == "EMPRUNT" :
        choix_book_fantaisie = input("Quel livre voulez-vous choisir ?")
        if choix_book_fantaisie.upper() == "BEGIN FANTASY I" : 
            choice = input("Prendre 'Begin Fantasy I' comme emprunt ? ")
            if choix.upper() == "Y" :
                panier1 = "Begin Fantasy I" 
                retour = input("Continuer vos achats ?")
                if retour.upper == "Y":
                    fantaisie()
                elif retour.upper == "N" :
                    panier()
            elif choix.upper() == "N" :
                fantaisie()
def panier():
    print("Panier à choux")

fantaisie()
