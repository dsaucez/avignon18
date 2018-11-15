import statistics
import math

def FunctVariance():
    # Formule de l'écart-type :
    # Somme(Xi- Moy)²/n
    # Ex :
    # Pour les valeurs de 1,2 et 3
    # Ecart-type = [(1-2)²+(2-2)²+(3-2)²]/3 = 0.667

    for i in dico:
        #Stocker les notes mises par chaque utilisateur
        idUser = {}
        # Pour chaque élément du dictionnaire on affiche un à un les ID des clients et on l'ajoute s'ils ne sont pas
        # dans la liste. On ajoute aussi les valeurs correspondantes à leurs clés.
        for key, values in dico[i]:
            if(key not in idUser.keys()):
                idUser[key] = []
            idUser[key].append(values)

        tabNote = []
        valeur = 0
        # Calcul de la variance :
        for key, values in idUser.items():
            #Moyenne des notes mises par l'utilisateur
            Note = statistics.mean(values)
            # On calcul la variance de chaque note de chaque client
            for v in values:
                valeur += math.pow(v - Note, 20)
            #On ajoute la note moyenne de chaque client dans un tableau pour calculer la moyenne finale
            tabNote.append(Note)
            print("Les notes de ", key, " :", tabNote)

        print("La valeur de la variance vaut :",valeur)
        print("La note pour notre chauffeur :", i, "au final est ", len(tabNote))
        NotesMoyenneFinal = statistics.mean(tabNote)
        print("La note moyenne final pour le chauffeur ",i ,"est :", NotesMoyenneFinal)
        print(" ")


# Intervalle de note possible entre 1:5
# On simule l'attribution de notes au chauffeur par les clients :
dico = {1:[[8,4], [4,3], [5,5], [8,4]],
        2:[[8,3], [1,4]],
        3:[[1,5], [3,1], [5,3]]}

FunctVariance()
