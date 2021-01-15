
if __name__ == '__main__':
    wallet = int(input("Veuiller insérer votre budget"))
    livre = 50
    print("Vous avez " + str(wallet) + "€")
    choice = input("Souhaitez-vous acheter un livre à 50 euros")
    true = "y"
    false = "n"
    if choice == true:
        past_wallet = wallet - livre
        print("Vous avez acheté le livre, votre nouveau budget est de " + str(past_wallet) + "€")
    else:
        print("Vous avez refusé l'achat")

