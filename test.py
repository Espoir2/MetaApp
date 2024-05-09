def valeur_numerologie(lettre):
    return (ord(lettre.lower()) - 96) % 9 or 9


print(valeur_numerologie('espoir'))