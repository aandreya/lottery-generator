
import random

print "LOTO\n\n\n"

zaloga = int(input("Med kolikimi stevili izbiramo loto stevilke? "))
zadetki = int(input("Koliko zadetih stevil je loto dobitek? "))

loto_dobitek = []

for zadetek in range(0, zadetki):
    loto_dobitek.append(random.randint(1, zaloga))

loto_dobitek.sort()

print"\n\n\nWinning numbers are: "
print loto_dobitek
