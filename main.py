import random as rnd
lijst_a = []
lijst_b = []
lijst_c = []
lijst_d = []

def druk_lijst(lijst):
    for x in lijst:
        print(x,end="\t")
    print()

def genereer_4_lijsten():
    #genereert 100 getallen tussen 20 en 200
    for getal in range(1,100):
        random_getal = rnd.randint(20,200)
        if getal%4==1:
            lijst_a.append(random_getal)
        elif getal%4==2:
            lijst_b.append(random_getal)
        elif getal%4==3:
            lijst_c.append(random_getal)
        else:
            lijst_d.append(random_getal)
    druk_lijst(lijst_a)
    druk_lijst(lijst_b)
    druk_lijst(lijst_c)
    druk_lijst(lijst_d)

genereer_4_lijsten()



