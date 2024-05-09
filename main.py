
### -------- FONCTIONS UTILITAIRES -------- ###

def letterToDigit(letter):
    return (ord(letter.lower()) - 96) % 9 or 9

def numberToDigit(number, title=""):
    print(f"\nRéduction pour {title} :")
    digitResult = sum([int(chiffre) for chiffre in str(number)])
    while digitResult > 9:
        digitResult = sum([int(digit) for digit in str(digitResult)])
        print(f"Réduction : {digitResult}")
    return digitResult

def numberToDigit_2(number, title=""):
    print(f"\nRéduction pour {title} :")
    digitResult = sum([int(chiffre) for chiffre in str(number)])
    while digitResult > 9:
        if digitResult == 11 or digitResult == 22 or digitResult == 33:
            break
        digitResult = sum([int(digit) for digit in str(digitResult)])
        print(f"Réduction : {digitResult}")
    return digitResult

def somme_letters_specifiques(nom, letters_cibles):
    return sum(letterToDigit(letter) for letter in nom if letter.lower() in letters_cibles)

def calculer_somme_consonnes(nom_complet):
    consonnes = "bcdfghjklmnpqrstvwxz"
    somme_total = sum(somme_letters_specifiques(partie, consonnes) for partie in nom_complet)
    somme_consonnes = numberToDigit(somme_total, "Moi intime")
    return somme_consonnes

def calculer_somme_voyelles(nom_complet):
    voyelles = "aeiouy"
    somme_total = sum(somme_letters_specifiques(partie, voyelles) for partie in nom_complet)
    somme_voyelles = numberToDigit(somme_total, "Élan spirituel")
    return somme_voyelles

def trouver_annees_personnelles_1(jour, mois, annee_naissance):
    annees_personnelles_1 = []
    for annee in range(annee_naissance, annee_naissance + 200):
        if calculer_annee_personnelle_2(jour, mois, annee) == 1:
            annees_personnelles_1.append(annee)
        
    print(annees_personnelles_1)
    return annees_personnelles_1

def trouver_premiere_derniere(letters, cible):
    premiere = derniere = None
    for letter in letters:
        if letter in cible:
            if premiere is None:
                premiere = letter
            derniere = letter
    return premiere, derniere

def obtenir_date_naissance():
    jour = int(input("Entrez votre jour de naissance : "))
    mois = int(input("Entrez votre mois de naissance : "))
    annee = int(input("Entrez votre année de naissance : "))
    return jour, mois, annee

def obtenir_nom_complet():
    nom_complet = []

    nom_famille = input("Entrez votre nom de famille : ")
    nom_complet.append(nom_famille)

    prenom_usuel = input("Entrez votre prénom usuel : ")
    nom_complet.append(prenom_usuel)

    while True:
        autre_prenom = input("Entrez un autre prénom si vous en avez, sinon appuyez sur Entrée : ")
        if autre_prenom == "":
            break
        nom_complet.append(autre_prenom)

    return nom_complet

def afficher_resultats(jour, mois, annee, nom_complet, chemin_de_vie):
    print(f"\nDate de naissance : {jour}/{mois}/{annee}")
    print(f"Nom complet : {' '.join(nom_complet)}")
    print(f"Chemin de vie : {chemin_de_vie}")

def separation():
    print('-'*50)

def afficher_session(title):
    print()
    print()
    print(f" ☯️ {title.upper()} ☯️ ")
    print()

def sep_session(title):
    separation()
    afficher_session(title)


### -------- CALCUL DU CHEMIN DE VIE -------- ###

def calculer_chemin_de_vie(jour, mois, annee):
    somme = jour + mois + annee
    print(f"Calcul du chemin de vie : {jour} + {mois} + {annee} = {somme}")
    while somme > 9:
        if somme == 11 or somme == 22 or somme == 33:
            break
        somme = sum([int(chiffre) for chiffre in str(somme)])
        print(f"Réduction : {somme}")
    return somme


### -------- CALCUL DE L'EXPRESSION -------- ###

def somme_nom(nom):
    somme = sum(letterToDigit(letter) for letter in nom if letter.isalpha())
    print(f"\n{nom.upper()}")
    for letter in nom.upper():
        if letter.isalpha():
            print(letter, end=" ")
    print("\n" + "| " * len(nom))
    for letter in nom.upper():
        if letter.isalpha():
            print(letterToDigit(letter), end=" ")
    print(f"\n{nom.upper()} = {somme}")
    return somme

def calculer_expression(nom_complet):
    somme_total = sum(somme_nom(partie) for partie in nom_complet)
    expression = numberToDigit(somme_total, "Expression Totale")
    return expression

def calculer_expression_specifique(nom_famille, prenom_usuel):
    somme_specifique = somme_nom(nom_famille) + somme_nom(prenom_usuel)
    expression_specifique = numberToDigit(somme_specifique, "Expression Spécifique")
    return expression_specifique


### -------- CALCUL DE L'ANNÉE PERSONNELLE -------- ###

def calculer_annee_personnelle(jour, mois):
    annee_courante = int(input("Entrez l'année courante : "))
    somme = jour + mois + annee_courante
    print(f"Calcul de l'année personnelle : {jour} + {mois} + {annee_courante} = {somme}")
    annee_personnelle = numberToDigit(somme, "Année Personnelle")
    return annee_personnelle

def calculer_annee_personnelle_2(jour, mois, annee):
    somme = jour + mois + annee
    # print(f"Calcul de l'année personnelle : {jour} + {mois} + {annee} = {somme}")
    annee_personnelle = numberToDigit(somme, "Année Personnelle")
    return annee_personnelle


### -------- CALCUL DU NOMBRE AXIAL -------- ###

def calculer_nombre_axial(chemin_de_vie, expression):
    somme = chemin_de_vie + expression
    print(f"Calcul du nombre axial : {chemin_de_vie} + {expression} = {somme}")
    nombre_axial = numberToDigit(somme, "Nombre Axial")
    return nombre_axial


### -------- CALCUL DU NOMBRE DE FORCE -------- ###

def calculer_nombre_de_force(jour, mois):
    somme = jour + mois
    print(f"Calcul du nombre de force : {jour} + {mois} = {somme}")
    nombre_de_force = numberToDigit(somme, "Nombre de Force")
    return nombre_de_force


### -------- CALCUL DES RÉALISATIONS -------- ###

def calculer_realisations_et_periodes(jour, mois, annee, chemin_de_vie):
    realisation1 = numberToDigit(mois + jour, "Réalisation 1")
    realisation2 = numberToDigit(jour + annee, "Réalisation 2")
    realisation3 = numberToDigit(realisation1 + realisation2, "Réalisation 3")
    realisation4 = numberToDigit(mois + annee, "Réalisation 4")

    periode1_fin = 36 - chemin_de_vie
    periode2_fin = periode1_fin + 9
    periode3_fin = periode2_fin + 9

    print(f"\nRéalisation 1 (De 0 à {periode1_fin} ans) : {realisation1}")
    print(f"Réalisation 2 (De {periode1_fin} à {periode2_fin} ans) : {realisation2}")
    print(f"Réalisation 3 (De {periode2_fin} à {periode3_fin} ans) : {realisation3}")
    print(f"Réalisation 4 (De {periode3_fin} ans à la mort) : {realisation4}")


### -------- CALCUL DES CYCLES DE VIES -------- ###

def trouver_cycle_proche(age_cible, annees_personnelles_1):
    return min(annees_personnelles_1, key=lambda annee: abs(annee - age_cible))

def calculer_cycles_de_vie(jour, mois, annee):
    annees_personnelles_1 = trouver_annees_personnelles_1(jour, mois, annee)
    annee_C_1_2 = trouver_cycle_proche(annee + 28, annees_personnelles_1)
    annee_C_2_3 = trouver_cycle_proche(annee + 56, annees_personnelles_1)
    print(f"{annee_C_1_2}")
    print(f"{annee_C_2_3}")

    age_fin_cycle_formatif = annee_C_1_2 - annee - 1
    age_fin_cycle_productif = annee_C_2_3 - annee - 1

    CF = numberToDigit_2(mois, "Réduction pour Cyce formatif")
    CP = numberToDigit_2(jour, "Réduction pour Cyce Productif")
    CM = numberToDigit_2(annee, "Réduction pour Cyce de la Moisson")

    print(f"Cycle Formatif | 0 ans ({jour}/{mois}/{annee}) à {age_fin_cycle_formatif} ans (31 décembre {annee_C_1_2 - 1}): {CF}")
    print(f"Cycle Productif | {age_fin_cycle_formatif + 1} ans (1er Janvier {annee_C_1_2}) à {age_fin_cycle_productif} ans (31 décembre {annee_C_2_3 - 1}): {CP}")
    print(f"Cycle de la Moisson | {age_fin_cycle_productif + 1} ans (1er janvier {annee_C_2_3}) à la mort: {CM}")


### -------- CALCUL DES DÉFIS LIÉS À LA DATE DE NAISSANCE -------- ###

def calculer_defis_numerologiques(jour, mois, annee):
    jour_reduit = numberToDigit(jour, "Jour")
    mois_reduit = numberToDigit(mois, "Mois")
    annee_reduite = numberToDigit(annee, "Année")

    defi_mineur1 = abs(mois_reduit - jour_reduit)
    defi_mineur2 = abs(jour_reduit - annee_reduite)
    defi_majeur = abs(defi_mineur1 - defi_mineur2)
    defi_aleatoire = abs(mois_reduit - annee_reduite)

    print(f"\n1er Défi Mineur (Mois - Jour) : {defi_mineur1}")
    print(f"2ème Défi Mineur (Jour - Année) : {defi_mineur2}")
    print(f"Défi Majeur (1er Défi Mineur - 2ème Défi Mineur) : {defi_majeur}")
    print(f"Défi Aléatoire (Mois - Année) : {defi_aleatoire}")


### -------- CALCUL DES DÉFIS LIÉS À LA L'APPELATION DE NAISSANCE -------- ###

def calculer_defis_appellation(prenom_usuel, nom_famille):
    mot_unique = prenom_usuel + nom_famille
    mot_unique = mot_unique.lower()

    voyelles = "aeiouy"
    consonnes = "".join(set("abcdefghijklmnopqrstuvwxz") - set(voyelles))

    premiere_voyelle, derniere_voyelle = trouver_premiere_derniere(mot_unique, voyelles)
    premiere_consonne, derniere_consonne = trouver_premiere_derniere(mot_unique, consonnes)

    des = abs(letterToDigit(premiere_voyelle) - letterToDigit(derniere_voyelle))
    dmi = abs(letterToDigit(premiere_consonne) - letterToDigit(derniere_consonne))

    defi_expression = des + dmi

    print(f"\nDéfi de l'Élan Spirituel (DES) : {des}")
    print(f"Défi du Moi Intime (DMI) : {dmi}")
    print(f"Défi de l'Expression : {defi_expression}")


### -------- CALCUL DES DÉFIS LIÉS AU JOUR DE NAISSANCE -------- ###

def calculer_defi_jour_naissance(jour):
    if jour <= 9:
        print("\nNé entre le 1er et le 9e jour du mois : Aucun défi.")
        return None

    chiffres = [int(chiffre) for chiffre in str(jour)]
    defi = abs(chiffres[0] - chiffres[1])

    print(f"\nDéfi lié au jour de naissance ({jour}) : {defi}")
    return defi


### -------- CALCUL DES DÉFIS DE L'ANNÉE -------- ###

def calculer_defis_annee(jour, mois, annee_courante, annee_personnelle):
    somme_naissance = numberToDigit(jour + mois)
    acr  = numberToDigit(annee_courante)
    apr = numberToDigit(annee_personnelle)

    ds1 = abs(acr - somme_naissance)
    ds2 = abs(apr - somme_naissance)

    defi_majeur = abs(ds1 - ds2)

    print(f"\nDéfi Secondaire 1 (Année courante - (Jour + Mois)) : {ds1}")
    print(f"Défi Secondaire 2 (Année Personnelle - (Jour + Mois)) : {ds2}")
    print(f"Défi Majeur (DS1 - DS2) : {defi_majeur}")











def main():
    jour, mois, annee = obtenir_date_naissance()
    annee_courante = int(input("Entrez l'année courante : "))
    nom_complet = obtenir_nom_complet()
    chemin_de_vie = calculer_chemin_de_vie(jour, mois, annee)
    afficher_resultats(jour, mois, annee, nom_complet, chemin_de_vie)

    sep_session("Expression Totale")
    expression = calculer_expression(nom_complet)

    sep_session("Expression Spécifique")
    expression_spec = calculer_expression_specifique(nom_complet[0], nom_complet[1])


    sep_session(" Moi Intime ")
    calculer_somme_consonnes(nom_complet)

    sep_session("Élan spirituel")
    calculer_somme_voyelles(nom_complet)

    sep_session("Année Personnelle")
    annee_personnelle = calculer_annee_personnelle_2(jour, mois, annee_courante)
    print(f"Année Personnelle : {annee_personnelle}")

    sep_session("Nombre Axial")
    nombre_axial = calculer_nombre_axial(chemin_de_vie, expression)
    print(f"Nombre Axial : {nombre_axial}")

    sep_session("Nombre Axial Spécifique")
    nombre_axial = calculer_nombre_axial(chemin_de_vie, expression_spec)
    print(f"Nombre Axial Spécifique : {nombre_axial}")

    sep_session("Nombre de Force")
    nombre_de_force = calculer_nombre_de_force(jour, mois)
    print(f"Nombre de Force : {nombre_de_force}")

    sep_session("Réalisation de Vie et Périodes")
    calculer_realisations_et_periodes(jour, mois, annee, chemin_de_vie)

    sep_session("Cycles de Vie")
    calculer_cycles_de_vie(jour, mois, annee)

    sep_session("Défis Liés à la date de naissance")
    calculer_defis_numerologiques(jour, mois, annee)


    sep_session("Défis de l'Appellation de naissance")
    calculer_defis_appellation(nom_complet[1], nom_complet[0])

    sep_session("Défi du Jour de Naissance")
    calculer_defi_jour_naissance(jour)



    sep_session("Défis de l'Année")
    calculer_defis_annee(jour, mois, annee_courante, annee_personnelle)

if __name__ == "__main__":
    main()
