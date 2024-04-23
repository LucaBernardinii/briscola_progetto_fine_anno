import random

#funzione per mischiare il mazzo
def mischia_mazzo(mazzo: list[dict]):
    for i in range(random.randint(5, 10)):
        random.shuffle(mazzo)

#funzione per creare il mazzo
def crea_mazzo(semi: list, valori: list) -> list[dict]:
    mazzo = []
    for seme in semi:
        for valore in valori:
            mazzo.append({"seme": seme, "valore": valore, "briscola": False})
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
    seme_briscola = carta_briscola["seme"]
    lista_briscole = []
    for carta in mazzo:
        seme = carta["seme"]
        if seme_briscola == seme:
            lista_briscole.append(carta)
    for carta in lista_briscole:
        carta["briscola"] = True
    return carta_briscola

#funzione per assegnazione dei valori delle carte
def assegna_valori(carta: dict) -> int:
    if carta["valore"] == "Asso" or carta["valore"] == "Ass":
        return 11
    elif carta["valore"] == "Fante" or carta["valore"] == "Fent":
        return 2
    elif carta["valore"] == "Cavallo" or carta["valore"] == "Caval":
        return 3
    elif carta["valore"] == "Re":
        return 4
    elif carta["valore"] == 3:
        return 10
    else:
        return 0
    
#funzione per la distribuzione iniziale delle carte del giocatore
def distribuzione_iniziale_giocatore(mazzo: list[dict]) -> list[dict]:
    mano_giocatore = []
    for i in range(3):
        carta_estratta = random.choice(mazzo)
        mano_giocatore.append(carta_estratta)
        mazzo.remove(carta_estratta)
    return mano_giocatore

#funzione per la distribuzione iniziale delle carte del computer
def distribuzione_iniziale_computer(mazzo: list[dict]) -> list[dict]:
    mano_computer = []
    for i in range(3):
        carta_estratta = random.choice(mazzo)
        mano_computer.append(carta_estratta)
        mazzo.remove(carta_estratta)
    return mano_computer

#funzione per la partita in italiano
def partita_italiano(mazzo: list [dict]) -> int:
    punteggio_giocatore = 0
    punteggio_computer = 0
    mazzo = crea_mazzo (["denari","coppe","bastoni","spade"],["Asso",2,3,4,5,6,7,"Fante","Cavallo","Re"])
    mischia_mazzo(mazzo)
    mano_giocatore = distribuzione_iniziale_giocatore(mazzo)
    mano_computer = distribuzione_iniziale_computer(mazzo)
    while len(mazzo) > 0:
        for i in range(3):
            print(f"In mano hai" carta[""])
        

#funzione per la partita in romagnolo
def partita_romagnolo(mazzo: list [dict]) -> int:
    punteggio_giocatore = 0
    punteggio_computer = 0
    mazzo = crea_mazzo (["danèri","copp","bastun","spede"],["Ass",2,3,4,5,6,7,"Fent","Caval","Re"])
    mischia_mazzo(mazzo)
    while len(mazzo) > 0:
    









#svolgimento partita
print("Italiano->I")
print("Romagnolo->R")
scelta_lingua = input("Scegli la lingua con cui giocare: ")
if scelta_lingua == "I" or scelta_lingua == "i":
    print("La partita si svolgerà in italiano.")
    nome_giocatore = input("Inserisci il tuo nome?: ")
    
elif scelta_lingua == "R" or scelta_lingua == "r":
    print("Us zuga in rumagnol.")
    nome_giocatore = input("Cum ut cem?: ")
    
else:
    print("Scelta non valida, invurnid.")



