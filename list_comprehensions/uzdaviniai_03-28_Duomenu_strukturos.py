
"""Raskite visus skaičius nuo 1 iki 1000, kurie dalijasi iš 6."""
print(".......Pirma uzduotis.........")
def find_numbers_devide_six():
    return [number for number in range(1,1001) if number %6 ==0]
print(find_numbers_devide_six())



print(".........antras uzdavinys...........")
"""2_Sukurkite funkciją, kuri prie kiekvieno list nario prideda string galūnę."""


def pridek_galune(listas, galune):
    return [str(item) + galune for item in listas]

# Pavyzdys:
sarasas = [1, 2, 3, 4, 5]
naujas_sarasas = pridek_galune(sarasas, "_pabaiga")
print(naujas_sarasas)



print("...Trecia uzduotis........")
#Sukurkite string iš daugybės žodžių: Apskaičiuokite, kiek žodžių turi raidę e.

def skaiciuoti_raides_zodziuose(tekstas, raide):
    zodziu_skaicius = 0
    zodziu_sarasas = tekstas.split()

    for zodis in zodziu_sarasas:
        if raide in zodis:
            zodziu_skaicius += 1

    return zodziu_skaicius

tekstas = 'egle, paulius, saulius, mykolas'
raide = "e"
rezultatas = skaiciuoti_raides_zodziuose(tekstas, raide)
print(f"Tekste yra {rezultatas} žodžiai, kuriuose yra raidė '{raide}'.")


print('.......Ketvirta uzduotis.....')
# Naudodami tą patį string, kaip ir ankstesniame pratime: apskaičiuokite raidžių, kurios turi daugiau nei 5 simbolius, skaičių.

def skaiciuoti_ilgi(tekstas, min_simbol):

    zodziu_skaicius=0
    tekstas = tekstas.split()
    for zodis in tekstas:
        if len(zodis) > min_simbol:
            zodziu_skaicius += 1

    return zodziu_skaicius

tekstas = 'egle, paulius, saulius, mykolas'
min_simbol = 5

rezultatas = skaiciuoti_ilgi(tekstas, min_simbol)

print(f"Tekste yra {rezultatas} žodžių, kurie yra ilgesni nei {min_simbol} simboliai.")




print('.....Penkta uzduotis.....')
# Parašykite programą, kuri patikrintų, ar iš duoto skaičiaus istraukus šaknį ganam sveika skaičių
x = 9
if x %3 ==0:
    print(x, "dalinasi is trijų be liekanos")
else:
    print("nesidalina")


#kitas variantas..
import math

def saknis_int(sk):
    saknis = math.sqrt(sk)
    return saknis.is_integer()

def skaicius_saknis(sk):
    if saknis_int(sk):
        return f"is skaiciaus {sk} istraukus sakni gaunam sveika skaiciu ({int(math.sqrt(sk))})"
    else:
        return f"sveiko skaiciaus negaunam"

sk = 16
print(skaicius_saknis(sk))


"""Realybe tokia kad be CHAT GPT man tokiu kodu parasyt kolkas neimanoma. Net su uzuominom. Kolkas galiu tik analizuoti 
uzdaviniu sprendimą. Daug go neperprantu. Strategija, kartotis viską nuo pradziu vėl ir vel ir sprest is eiles nuo 
pradziu W3school ir kode academy uzduočiu"""

"""vientele visikai savarankiskai parasyta uzduotis cia 5-tos, pirmas variantas """
