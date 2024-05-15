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
def assegna_valori(carta_estratta: dict) -> int:
    if carta_estratta["valore"] == "Asso":
        return 11
    elif carta_estratta["valore"] == "Fante":
        return 2
    elif carta_estratta["valore"] == "Cavallo":
        return 3
    elif carta_estratta["valore"] == "Re":
        return 4
    elif carta_estratta["valore"] == 3:
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
def partita_italiano() -> int:
    punteggio_giocatore = 0
    punteggio_computer = 0
    mazzo = crea_mazzo (["denari","coppe","bastoni","spade"],["Asso",2,3,4,5,6,7,"Fante","Cavallo","Re"])
    mischia_mazzo(mazzo)
    mano_giocatore = distribuzione_iniziale_giocatore(mazzo)
    mano_computer = distribuzione_iniziale_computer(mazzo)
    while len(mazzo) > 0:
        print(f"In mano hai {mano_giocatore[0]}, {mano_giocatore[1]}, {mano_giocatore[2]}")
        carta_scelta = input("Scegli la carta da giocare 0/1/2: ")
        carta_giocata = mano_giocatore[carta_scelta]
        mano_giocatore.remove(carta_giocata)
        carta_giocata_computer = random.choice(mano_computer)
        valore_carta_giocatore = assegna_valori(carta_giocata)
        valore_carta_computer = assegna_valori(carta_giocata_computer)
        