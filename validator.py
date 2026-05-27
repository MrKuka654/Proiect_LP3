def valideaza_date(plecare, destinatie, toate_statiile):
    if plecare not in toate_statiile:
        return "Eroare: statia de plecare nu exista!"

    if destinatie not in toate_statiile:
        return "Eroare: statia destinatie nu exista!"

    if plecare == destinatie:
        return "Eroare: plecarea si destinatia sunt identice!"

    return None