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
    print(f"La briscola è {carta_briscola['seme']}")
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

#funzione per la partita
def partita():
    nuova_partita = True
    while nuova_partita == True:
        nome_giocatore = input("Inserisci il tuo nome: ")
        punteggio_giocatore = 0
        punteggio_computer = 0
        mazzo = crea_mazzo (["denari","coppe","bastoni","spade"],["Asso",2,3,4,5,6,7,"Fante","Cavallo","Re"])
        mischia_mazzo(mazzo)
        mano_giocatore = distribuzione_iniziale_giocatore(mazzo)
        mano_computer = distribuzione_iniziale_computer(mazzo)
        carta_briscola = scelta_briscola(mazzo)
        seme_briscola = carta_briscola["seme"]
        primo_giocatore = "giocatore"

        #fase di gioco
        while len(mazzo) > 0:
            if primo_giocatore == "giocatore":
                print(f"In mano hai 1 = {mano_giocatore[0]}, 2 = {mano_giocatore[1]}, 3 = {mano_giocatore[2]}")
                carta_scelta = int(input(f"{nome_giocatore}, scegli la carta da giocare 1/2/3: "))
                carta_scelta -= 1
                carta_giocata = mano_giocatore[carta_scelta]
                mano_giocatore.remove(carta_giocata)
                print(f"{nome_giocatore} ha giocato {carta_giocata}.")
                carta_giocata_computer = random.choice(mano_computer)
                mano_computer.remove(carta_giocata_computer)
                print(f"Il computer ha giocato {carta_giocata_computer}")
                seme_prioritario = carta_giocata["seme"]
                carta_estratta_giocatore = estrai_carta(mazzo)
                mano_giocatore.append(carta_estratta_giocatore)
                carta_estratta_computer = estrai_carta(mazzo)
                mano_computer.append(carta_estratta_computer)
            elif primo_giocatore == "computer":
                carta_giocata_computer = random.choice(mano_computer)
                mano_computer.remove(carta_giocata_computer)
                print(f"Il computer ha giocato {carta_giocata_computer}")
                print(f"In mano hai 1 = {mano_giocatore[0]}, 2 = {mano_giocatore[1]}, 3 = {mano_giocatore[2]}")
                carta_scelta = int(input(f"{nome_giocatore}, scegli la carta da giocare 1/2/3: "))
                carta_scelta -= 1
                carta_giocata = mano_giocatore[carta_scelta]
                mano_giocatore.remove(carta_giocata)
                print(f"{nome_giocatore} ha giocato {carta_giocata}.")
                seme_prioritario = carta_giocata_computer["seme"]
                carta_estratta_giocatore = estrai_carta(mazzo)
                mano_giocatore.append(carta_estratta_giocatore)
                carta_estratta_computer = estrai_carta(mazzo)
                mano_computer.append(carta_estratta_computer)

            valore_carta_giocatore = assegna_valori(carta_giocata)
            valore_carta_computer = assegna_valori(carta_giocata_computer)

            #determinazione vincitore
            #casi con briscola
            if carta_giocata["seme"] == seme_briscola and carta_giocata_computer["seme"] != seme_briscola:
                print(f"{nome_giocatore} ha vinto questa mano.")
                punteggio_giocatore += valore_carta_giocatore + valore_carta_computer
                primo_giocatore = "giocatore"
            elif carta_giocata["seme"] != seme_briscola and carta_giocata_computer["seme"] == seme_briscola:
                print("Il computer ha vinto questa mano.")
                punteggio_computer += valore_carta_giocatore + valore_carta_computer
                primo_giocatore = "computer"
            elif carta_giocata["seme"] == seme_briscola and carta_giocata_computer["seme"] == seme_briscola:
                if valore_carta_giocatore > valore_carta_computer:
                    print(f"{nome_giocatore} ha vinto questa mano.")
                    punteggio_giocatore += valore_carta_giocatore + valore_carta_computer
                    primo_giocatore = "giocatore"
                elif valore_carta_giocatore < valore_carta_computer:
                    print("Il computer ha vinto questa mano.")
                    punteggio_computer += valore_carta_giocatore + valore_carta_computer
                    primo_giocatore = "computer"
                else:
                    pass
            #casi con seme uguale
            else:
                if carta_giocata["seme"] == carta_giocata_computer["seme"]:
                    if valore_carta_giocatore > valore_carta_computer:
                        print(f"{nome_giocatore} ha vinto questa mano.")
                        punteggio_giocatore += valore_carta_giocatore + valore_carta_computer
                        primo_giocatore = "giocatore"
                    elif valore_carta_giocatore < valore_carta_computer:
                        print("Il computer ha vinto questa mano.")
                        punteggio_computer += valore_carta_giocatore + valore_carta_computer
                        primo_giocatore = "computer"
                    else:
                        pass
                #casi con seme diverso
                else:
                    if seme_prioritario == "denari":
                        if carta_giocata["seme"] == "denari":
                            print(f"{nome_giocatore} ha vinto questa mano.")
                            punteggio_giocatore += valore_carta_giocatore + valore_carta_computer
                            primo_giocatore = "giocatore"
                        else:
                            print("Il computer ha vinto questa mano.")
                            punteggio_computer += valore_carta_giocatore + valore_carta_computer
                            primo_giocatore = "computer"
                    elif seme_prioritario == "coppe":
                        if carta_giocata["seme"] == "coppe":
                            print(f"{nome_giocatore} ha vinto questa mano.")
                            punteggio_giocatore += valore_carta_giocatore + valore_carta_computer
                            primo_giocatore = "giocatore"
                        else:
                            print("Il computer ha vinto questa mano.")
                            punteggio_computer += valore_carta_giocatore + valore_carta_computer
                            primo_giocatore = "computer"
                    elif seme_prioritario == "bastoni":
                        if carta_giocata["seme"] == "bastoni":
                            print(f"{nome_giocatore} ha vinto questa mano.")
                            primo_giocatore = "giocatore"
                        else:
                            print("Il computer ha vinto questa mano.")
                            punteggio_computer += valore_carta_giocatore + valore_carta_computer
                            primo_giocatore = "computer"
                    elif seme_prioritario == "spade":
                        if carta_giocata["seme"] == "spade":
                            print(f"{nome_giocatore} ha vinto questa mano.")
                            primo_giocatore = "giocatore"
                        else:
                            print("Il computer ha vinto questa mano.")
                            punteggio_computer += valore_carta_giocatore + valore_carta_computer
                            primo_giocatore = "computer"
                    else:
                        pass
            print("_________________________________________________________________________")
            
    print(f"Il punteggio è: {punteggio_giocatore} per {nome_giocatore} e {punteggio_computer} per il computer.")
    if punteggio_giocatore > punteggio_computer:
        print(f"{nome_giocatore} ha vinto la partita con {punteggio_giocatore}.")
    elif punteggio_giocatore < punteggio_computer:
        print(f"Il computer ha vinto la partita con {punteggio_computer}.")
    else:
        print(f"{nome_giocatore} e il computer hanno pareggiato totalizzando entrambi {punteggio_giocatore}.")
    
    scelta_partita = input("Vuoi fare un'altra partita? (s/n) ")
    if scelta_partita == "s":
        nuova_partita == True
    elif scelta_partita == "n":
        nuova_partita == False
    else:
        pass

#invocazione funzione partita       
partita()