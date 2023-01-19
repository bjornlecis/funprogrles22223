import queue
import random as rnd
q = queue.Queue(5)

for i in range(0,5):
    q.put(rnd.randint(1,55))

lijst = []
for opgave in range(q.maxsize):
    getal = q.get()
    print("wat is het dubbel van: ",getal)
    invoer = int(input(""))
    if invoer == getal*2:
        print("juist")
        lijst.append(getal)
    else:
        print("FOUT!")
for getal in lijst:
    print(getal)
