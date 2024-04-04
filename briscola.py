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

#funzione per estrarre la carta
def estrai_carta (mazzo: list [dict]) -> dict:
    carta = random.choice (mazzo)
    mazzo.remove (carta)
    return carta

#funzione per scelta della briscola
def scelta_briscola(mazzo: list [dict]) -> dict:
    carta_briscola = random.choice (mazzo)
    mazzo.remove (carta_briscola)
    mazzo.append (carta_briscola)






#svolgimento partita
print("Italiano->I")
print("Romagnolo->R")
scelta_lingua = input("Scegli la lingua con cui giocare: ")
if scelta_lingua == "I":
    print("La partita si svolgerà in italiano.")
elif scelta_lingua == "R":
    print("Us zuga in rumagnol.")
else:
    print("Scelta non valida, invurnid.")



mazzo = crea_mazzo (["denari","coppe","bastoni","spade"],["Asso",2,3,4,5,6,7,"Fante","Cavallo","Re"])