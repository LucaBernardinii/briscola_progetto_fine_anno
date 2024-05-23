import random
from termcolor import colored

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
def distribuzione_iniziale(mazzo: list[dict]) -> list[dict]:
    mano = []
    for i in range(3):
        carta_estratta = random.choice(mazzo)
        mano.append(carta_estratta)
        mazzo.remove(carta_estratta)
    return mano

#funzione per la spiegazione del gioco
def tutorial():
    print("Benvenuto al gioco della Briscola romagnola!")
    scelta = input(str("Conosci già il gioco della briscola?  (s/n): "))
    while scelta not in ["s", "n"]:
        print("Errore, scelta non valida.")
        scelta = input(str("Conosci già il gioco della briscola?  (s/n): "))
    if scelta == "s":
        print("Bene! Inzia la partita!")
    elif scelta == "n":
        print("Ecco una spiegazione delle regole della briscola: ")
        print(colored("Regole generali: ", "light_red"))
        print("Briscola si gioca con un mazzo di 40 carte. Può essere giocato da 2 a 6 giocatori, divisi in coppie o squadre.")
        print("Lo scopo del gioco è totalizzare almeno 61 punti, dei 120 disponibili.")
        input("Premi invio per continuare.")
        print(colored("Punteggi delle carte: ", "light_red"))
        print("Carichi: Asso di valore 11, 3 di valore 10.")
        print("Figure: Re di valore 4, Cavallo di valore 3, Fante di valore 2.")
        print("Lisci: 7, 6, 5, 4, 2 di valore 0.")
        input("Premi invio per continuare.")
        print(colored("Inizio del gioco: ", "light_red"))
        print("Si distribuiscono tre carte ciascuno e si pone una carta al centro del tavolo, tutte le carte con con lo stesso seme di quella al centro sono briscole.")
        print("Le briscole hanno più valore rispetto alle carte normali, ad esempio un Fante di briscola prende in ogni caso un Fante non di briscola.")
        input("Premi invio per continuare.")
        print(colored("Svolgimento del gioco: ", "light_red"))
        print("Le carte di valore più alto prendono quelle di valore più basso e le carte di briscola prendono le carte non di briscola.")
        print("Se si giocano due carte dello stesso valore non di briscola, vince chi ha giocato per primo.")
        print("Il vincitore della mano ha diritto ha pescare per primo e a giocare per primo al turno successivo.")
        input("Premi invio per continuare.")
        print(colored("Fine del gioco e determinazione del vincitore: ", "light_red"))
        print("Il gioco finisce quando si sono giocate tutte le carte nel mazzo e in mano.")
        print("Si contano i punti secondo le regole sopra, chi ha totalizzato più vince.")
        input("Complimenti! Ora sai giocare a briscola, ripassa le regole se ne hai bisogno e quando sei pronto premi Invio per iniziare a giocare.")
        print("_________________________________________________________________________")

#funzione per la partita
def partita():
    tutorial()
    nuova_partita = True
    while nuova_partita == True:
        nome_giocatore = input("Inserisci il tuo nome: ")
        punteggio_giocatore = 0
        punteggio_computer = 0
        mazzo = crea_mazzo (["denari","coppe","bastoni","spade"],["Asso",2,3,4,5,6,7,"Fante","Cavallo","Re"])
        mischia_mazzo(mazzo)
        mano_giocatore = distribuzione_iniziale(mazzo)
        mano_computer = distribuzione_iniziale(mazzo)
        carta_briscola = scelta_briscola(mazzo)
        seme_briscola = carta_briscola["seme"]
        primo_giocatore = "giocatore"

        #fase di gioco
        while len(mano_giocatore) > 0:
            print(punteggio_giocatore)
            print(punteggio_computer)
            #inizia il giocatore
            if primo_giocatore == "giocatore":
                print(colored(f"La briscola è {carta_briscola['seme']}", "cyan"))
                if len(mano_giocatore) == 3:
                    print(colored(f"In mano hai 1 = {mano_giocatore[0]}, 2 = {mano_giocatore[1]}, 3 = {mano_giocatore[2]}", "yellow"))
                elif len(mano_giocatore) == 2:
                    print(colored(f"In mano hai 1 = {mano_giocatore[0]}, 2 = {mano_giocatore[1]}", "yellow"))
                elif len(mano_giocatore) == 1:
                    print(colored(f"In mano hai 1 = {mano_giocatore[0]}", "yellow"))
                carta_scelta = int(input(f"{nome_giocatore}, scegli la carta da giocare 1/2/3: "))
                while carta_scelta not in [1, 2, 3,]:
                    print("Errore, inserisci un numero valido 1/2/3:")
                    carta_scelta = int(input(f"{nome_giocatore}, scegli la carta da giocare 1/2/3: "))
                carta_scelta -= 1
                carta_giocata = mano_giocatore[carta_scelta]
                mano_giocatore.remove(carta_giocata)
                print(f"{nome_giocatore} ha giocato {carta_giocata}.")
                carta_giocata_computer = random.choice(mano_computer)
                mano_computer.remove(carta_giocata_computer)
                print(f"Il computer ha giocato {carta_giocata_computer}")
                seme_prioritario = carta_giocata["seme"]
                if len(mazzo) > 0:
                    carta_estratta_giocatore = estrai_carta(mazzo)
                    mano_giocatore.append(carta_estratta_giocatore)
                    carta_estratta_computer = estrai_carta(mazzo)
                    mano_computer.append(carta_estratta_computer)

            #inizia il computer
            elif primo_giocatore == "computer":
                print(colored(f"La briscola è {carta_briscola['seme']}", "cyan"))
                carta_giocata_computer = random.choice(mano_computer)
                mano_computer.remove(carta_giocata_computer)
                print(f"Il computer ha giocato {carta_giocata_computer}")
                if len(mano_giocatore) == 3:
                    print(colored(f"In mano hai 1 = {mano_giocatore[0]}, 2 = {mano_giocatore[1]}, 3 = {mano_giocatore[2]}", "yellow"))
                elif len(mano_giocatore) == 2:
                    print(colored(f"In mano hai 1 = {mano_giocatore[0]}, 2 = {mano_giocatore[1]}", "yellow"))
                elif len(mano_giocatore) == 1:
                    print(colored(f"In mano hai 1 = {mano_giocatore[0]}", "yellow"))
                carta_scelta = int(input(f"{nome_giocatore}, scegli la carta da giocare 1/2/3: "))
                while carta_scelta not in [1, 2, 3,]:
                    print("Errore, inserisci un numero valido 1/2/3:")
                    carta_scelta = int(input(f"{nome_giocatore}, scegli la carta da giocare 1/2/3: "))
                carta_scelta -= 1
                carta_giocata = mano_giocatore[carta_scelta]
                mano_giocatore.remove(carta_giocata)
                print(f"{nome_giocatore} ha giocato {carta_giocata}.")
                seme_prioritario = carta_giocata_computer["seme"]
                if len(mazzo) > 0:
                    carta_estratta_giocatore = estrai_carta(mazzo)
                    mano_giocatore.append(carta_estratta_giocatore)
                    carta_estratta_computer = estrai_carta(mazzo)
                    mano_computer.append(carta_estratta_computer)
                else:
                    pass

            #assegnazione valori
            valore_carta_giocatore = assegna_valori(carta_giocata)
            valore_carta_computer = assegna_valori(carta_giocata_computer)

            #determinazione vincitore
            #casi con briscola
            if carta_giocata["seme"] == seme_briscola and carta_giocata_computer["seme"] != seme_briscola:
                print(colored(f"{nome_giocatore} ha vinto questa mano.", "green"))
                punteggio_giocatore += valore_carta_giocatore + valore_carta_computer
                primo_giocatore = "giocatore"

            elif carta_giocata["seme"] != seme_briscola and carta_giocata_computer["seme"] == seme_briscola:
                print(colored("Il computer ha vinto questa mano.", "red"))
                punteggio_computer += valore_carta_giocatore + valore_carta_computer
                primo_giocatore = "computer"

            elif carta_giocata["seme"] == seme_briscola and carta_giocata_computer["seme"] == seme_briscola:
                if valore_carta_giocatore > valore_carta_computer:
                    print(colored(f"{nome_giocatore} ha vinto questa mano.", "green"))
                    punteggio_giocatore += valore_carta_giocatore + valore_carta_computer
                    primo_giocatore = "giocatore"
                elif valore_carta_giocatore < valore_carta_computer:
                    print(colored("Il computer ha vinto questa mano.", "red"))
                    punteggio_computer += valore_carta_giocatore + valore_carta_computer
                    primo_giocatore = "computer"
                else:
                    pass
            #casi con seme uguale
            else:
                if carta_giocata["seme"] == carta_giocata_computer["seme"]:
                    if valore_carta_giocatore > valore_carta_computer:
                        print(colored(f"{nome_giocatore} ha vinto questa mano.", "green"))
                        punteggio_giocatore += valore_carta_giocatore + valore_carta_computer
                        primo_giocatore = "giocatore"
                    elif valore_carta_giocatore < valore_carta_computer:
                        print(colored("Il computer ha vinto questa mano.", "red"))
                        punteggio_computer += valore_carta_giocatore + valore_carta_computer
                        primo_giocatore = "computer"
                    else:
                        if carta_giocata["seme"] > carta_giocata_computer["seme"]:
                            print(colored(f"{nome_giocatore} ha vinto questa mano.", "green"))
                            punteggio_giocatore += valore_carta_giocatore + valore_carta_computer
                            primo_giocatore = "giocatore"
                        elif carta_giocata["seme"] < carta_giocata_computer["seme"]:
                            print(colored("Il computer ha vinto questa mano.", "red"))
                            punteggio_computer += valore_carta_giocatore + valore_carta_computer
                            primo_giocatore = "computer"
                #casi con seme diverso
                else:
                    if seme_prioritario == "denari":
                        if carta_giocata["seme"] == "denari":
                            print(colored(f"{nome_giocatore} ha vinto questa mano.", "green"))
                            punteggio_giocatore += valore_carta_giocatore + valore_carta_computer
                            primo_giocatore = "giocatore"
                        else:
                            print(colored("Il computer ha vinto questa mano.", "red"))
                            punteggio_computer += valore_carta_giocatore + valore_carta_computer
                            primo_giocatore = "computer"

                    elif seme_prioritario == "coppe":
                        if carta_giocata["seme"] == "coppe":
                            print(colored(f"{nome_giocatore} ha vinto questa mano.", "green"))
                            punteggio_giocatore += valore_carta_giocatore + valore_carta_computer
                            primo_giocatore = "giocatore"
                        else:
                            print(colored("Il computer ha vinto questa mano.", "red"))
                            punteggio_computer += valore_carta_giocatore + valore_carta_computer
                            primo_giocatore = "computer"

                    elif seme_prioritario == "bastoni":
                        if carta_giocata["seme"] == "bastoni":
                            print(colored(f"{nome_giocatore} ha vinto questa mano.", "green"))
                            punteggio_giocatore += valore_carta_giocatore + valore_carta_computer
                            primo_giocatore = "giocatore"
                        else:
                            print(colored("Il computer ha vinto questa mano.", "red"))
                            punteggio_computer += valore_carta_giocatore + valore_carta_computer
                            primo_giocatore = "computer"

                    elif seme_prioritario == "spade":
                        if carta_giocata["seme"] == "spade":
                            print(colored(f"{nome_giocatore} ha vinto questa mano.", "green"))
                            punteggio_giocatore += valore_carta_giocatore + valore_carta_computer
                            primo_giocatore = "giocatore"
                        else:
                            print(colored("Il computer ha vinto questa mano.", "red"))
                            punteggio_computer += valore_carta_giocatore + valore_carta_computer
                            primo_giocatore = "computer"
                    else:
                        pass
            print("_________________________________________________________________________")
            
        #fine partita e punteggio totale
        print(f"Il punteggio è: {punteggio_giocatore} per {nome_giocatore} e {punteggio_computer} per il computer.")
        if punteggio_giocatore > punteggio_computer:
            print(f"{nome_giocatore} ha vinto la partita con {punteggio_giocatore}.")
        elif punteggio_giocatore < punteggio_computer:
            print(f"Il computer ha vinto la partita con {punteggio_computer}.")
        else:
            print(f"{nome_giocatore} e il computer hanno pareggiato totalizzando entrambi {punteggio_giocatore}.")

        #nuova partita o abbandono
        scelta_partita = input("Vuoi fare un'altra partita? (s/n) ")
        while scelta_partita not in ["s", "n"]:
            print("Errore scelta non valida.")
            scelta_partita = input("Vuoi fare un'altra partita? (s/n) ")
        if scelta_partita == "s":
            nuova_partita = True
            print(f"{nome_giocatore} vuole giocare un'altra partita.")
        elif scelta_partita == "n":
            nuova_partita = False
            print(f"{nome_giocatore} abbandona il tavolo.")
        else:
            pass

#invocazione funzione partita       
partita()