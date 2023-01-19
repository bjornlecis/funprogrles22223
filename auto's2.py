wagens = ["bmw","audi","ford","fiat"]
def druk_lijst():
    for wagen in wagens:
        print(wagen)
def keuze_menu():
    print("1: druk lijst wagens")
    print("2: voeg een wagen toe aan wagens")
    print("3: zoek wagen")
    print("4: verwijder wagen")
    print("5: verander waarde wagen")

def voeg_wagen_toe():
    meerdere = input("1 of meer wagens")
    if meerdere == "1":
        wagen = input("geef je wagen in")
        if not wagen in wagens:
                ok = input("ben je zeker dat je deze wagen wilt toevoegen  y/n")
                if ok == "y":
                    wagens.append(wagen)
        else:
            print("wagen is reeds in lijst")
    else:
        wagen = input("geef je wagen in")
        while(not wagen == "einde"):
            if not wagen in wagens:
                    ok = input("ben je zeker dat je deze wagen wilt toevoegen  y/n")
                    if ok == "y":
                        wagens.append(wagen)
            else:
                print("wagen is reeds in lijst")
            wagen = input("geef je wagen in")

def verander_naam_wagen():
    druk_lijst()
    oude_wagen = input("geef de wagen die je wenst te veranderen")
    if oude_wagen in wagens:
        index = wagens.index(oude_wagen)
        nieuwe_wagen = input("geef de nieuwe waarde in")
        vraag = f"ben je zeker dat je {oude_wagen} wilt veranderen in {nieuwe_wagen} ?"
        ok = input(vraag)
        if ok == "y":
            wagens[index] = nieuwe_wagen

def zoek_wagen():
    wagen = input("geef je wagen in")
    if wagen in wagens:
        print("wagen in de lijst")
    else:
        print("wagen is niet in de lijst")


def verwijder_wagen():
    druk_lijst()
    wagen = input("geef de wagen in die je wenst te verwijderen")
    if wagen in wagens:
        wagens.remove(wagen)
        print(wagen," is verwijderd")
    else:
        print("{} staat niet in de lijst".format(wagen))

##############################################
#Hoofdprogramma                              #
##############################################

keuze_menu()
keuze = input("geef je keuze in")

while not keuze == "stop":
    if keuze == "1":
        druk_lijst()
    elif keuze == "2":
        voeg_wagen_toe()
    elif keuze == "3":
        zoek_wagen()
    elif keuze == "4":
        verwijder_wagen()
    elif keuze == "5":
        verander_naam_wagen()
    else:
        print("foutieve invoer")
    keuze = input("geef je keuze in")

