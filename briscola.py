import random

#funzione per mischiare il mazzo
def mischia_mazzo(mazzo: list[dict]):

    for _ in range(random.randint(5, 10)):
        random.shuffle(mazzo)

#funzione per creare il mazzo
def crea_mazzo(semi: list, valori: list) -> list[dict]:
    mazzo = []
    for seme in semi:
        for valore in valori:
            mazzo.append({"seme": seme, "valore": valore})
    return mazzo