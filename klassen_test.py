klas_a = ["ben","bert","an"]
klas_b = ["hanne","klaasje","marthe"]


def keuzes():
    print("1: toon een klas")
    print("2: voeg leerling toe aan een klas")
    print("3: zoek leerling")
    print("4: verwijder leerling")
    print("5: verplaats leerling")


def druk_klas_af():
    klas = input("klas a of b")
    while not klas == "a" or not klas == "b":
        if klas == "a":
            for leerling in klas_a:
                print(leerling)
            break
        elif klas == "b":
            for leerling in klas_b:
                print(leerling)
            break
        else:
            print("klas is niet gekend")
            klas = input("geef je klas in")
def lees_leerling_in():
    leerling = input("geef de naam van leerling")
    return leerling
def voeg_leerling_toe():
    leerling = lees_leerling_in()
    klas = input("geef klas in a of b")
    if klas.lower() == "a":
        klas_a.append(leerling)
    elif klas.lower() == "b":
        klas_b.append(leerling)
    else:
        print("klas bestaat niet")
def zoek_leerling():
    leerling = lees_leerling_in()
    if leerling in klas_a:
        print("leerling zit in klas a")
    elif leerling in klas_b:
        print("leerling zit in klas b")
    else:
        print("leerling zit niet op school")
def r_zoek_leerling(leerling):
    if leerling in klas_a and leerling in klas_b:
        return "ab"
    elif leerling in klas_a:
        return "a"
    elif leerling in klas_b:
        return "b"
    else:
        return "geen klas"

def verwijder_leerling():
    leerling = lees_leerling_in()
    klas = r_zoek_leerling(leerling)
    if klas == "a":
        klas_a.remove(leerling)
    elif klas == "b":
        klas_b.remove(leerling)
    elif klas == "ab":
        klas_a.remove(leerling)
        klas_b.remove(leerling)
    else:
        print("leerling niet in klas a of b")

def verwijder_leerling(leerling):
    klas = r_zoek_leerling(leerling)
    if klas == "a":
        klas_a.remove(leerling)
    elif klas == "b":
        klas_b.remove(leerling)
    elif klas == "ab":
        klas_a.remove(leerling)
        klas_b.remove(leerling)
    else:
        print("leerling niet in klas a of b")

def verplaats_leerling():
    leerling = lees_leerling_in()
    klas = r_zoek_leerling(leerling)
    verwijder_leerling(leerling)
    if klas == "a":
        klas_b.append(leerling)
    elif klas == "b":
        klas_a.append(leerling)
    else:
        print("leerling kan niet verplaats worden")




################################################################"
#Hoofdprogramma
#################################################################
keuzes()
keuze = input("geef je keuze")
while not keuze == "stop":
    if keuze == "1":
        druk_klas_af()
    elif keuze == "2":
        voeg_leerling_toe()
    elif keuze == "3":
        zoek_leerling()
    elif keuze == "4":
        verwijder_leerling()
    elif keuze == "5":
        verplaats_leerling()
    else:
        print("keuze niet beschikbaar")
    keuzes()
    keuze = input("geef je keuze")

