age = int(input("Quel est votre âge"))
wallet = 50
print("Vous avez " + str(wallet) + "€")

if age < 18:
    wallet = wallet - 7
    print("Vous avez " + str(wallet) + "€ car vous avez payé un billet enfant d'un montant de 7€")
elif age > 18:
    wallet = wallet - 12
    print("Vous avez " + str(wallet) + "€ car vous avez payé un billet adulte d'un montant de 12")

pilou = input("Voulez-vous du pop-corn ? Le paquet est à 10€")

if pilou == "oui":
    wallet - 10
    print("Tenez !")
    print(str(wallet))

elif pilou == "non":
    print("Très bien")