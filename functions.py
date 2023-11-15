def exponentiation_rapide_modulo(base, exposant, m):
    if exposant == 0:
        return 1
    elif exposant % 2 == 0:
        moitie = exponentiation_rapide_modulo(base, exposant // 2, m)
        return (moitie * moitie) % m
    else:
        moitie = exponentiation_rapide_modulo(base, (exposant - 1) // 2, m)
        return (base * moitie * moitie) % m

# Exemple d'utilisation
base = 9
exposant = 337
modulo = 21  # Exemple de valeur de m
resultat = exponentiation_rapide_modulo(base, exposant, modulo)
print(f"{base}^{exposant} % {modulo} = {resultat}")
