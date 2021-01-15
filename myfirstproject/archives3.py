

import statistics
import random
#génerer des phrases à partir de mots
syntaxe = input("Choisir des  mots sous la forme de: mot1/mot2/mt3/mot4/mot5...").split("/")
print(syntaxe)
random.shuffle(syntaxe)
print(syntaxe)
cb = len(syntaxe)
print(cb)
if cb < 5:
     print("Michou aime les {} et les {}".format(syntaxe[0] , syntaxe[1]))
elif cb >= 10:
    print(syntaxe[len(syntaxe) - 1], syntaxe[len(syntaxe) - 2])