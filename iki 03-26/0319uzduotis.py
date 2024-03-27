
#1Parašykite python programą, kuri paprašytų vartotojo įvesti vardą, pavardę, amžių. Įrašykite šias reikšmes į dict duomenų struktūrą ir ją išspausdinkite.

print('...........1uzduotis...............')

# vartotojas = {
# 	"name": str(input('Iveskite varda :')),
# 	"pavardė": str(input('Iveskite pavarde :')),
# 	"amzius": int(input('iveskite amziu:'))
# }
# print(dict(vartotojas))


# zodynas={}
# vardas=str(input("irasykite varda:"))
# pavarde=str(input('irasykite pavarde:'))
# amzius=int(input('irasykite amziu'))
#
# print(zodynas(vardas))
# print((zodynas(pavarde))

print('...............antra Uzduotis...........')

#2Pabandykite sukurti dict struktūrą, kurioje turite panaudoti visas jums žinomas duomenų struktūras ir tipus.

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(thisdict)

print('.............trecia............')


# -----------------------------------------------
# P.4.3
# -----------------------------------------------
# Sukurkite programą, kuri iš sakinių, kuriuos jus įvedėt, sukurtų dict,
# kuriame keys reikštų raides, o values šių raidžių dažnumą tuose sakiniuose.
# Programa turi reikalauti, kad vartotojas įvestų ne mažiau kaip 3 sakinius.
# -----------------------------------------------

sentences = ""

for i in range(1, 3+1):
    sentence = input(f"Enter a sentence ({i}/3) > ")
    sentences = sentences + sentence

letter_frequencies = {}

for char in sentences:
    if char.isalpha():
        if char not in letter_frequencies.keys():
            letter_frequencies[char] = 1
        else:
            letter_frequencies[char] += 1

print(letter_frequencies)

# dict_raides = {}
# sakinukai = ""
#
# for i in range(3):
#   sakinys = input('iveskite sakini:')
#   sakinukai += sakinys
# for i in sakinukai:
#   if i.sakinukai():
#     dict_raides[i]=sakinukai.count(i)
#
# print(sakinukai)
# print(dict_raides)


print('........ketvirta..........')

studentai_pazymiai = {"Tomas": 100, "Jonas": 70, "Monika": 70}
print(studentai_pazymiai)

geri_studentai = set()

for studentas, pazymys in studentai_pazymiai.items():
    if pazymys >= 80:
        geri_studentai.add(studentas)

print(geri_studentai)
# ---------------

studento_vardas = "Jonas"

if studento_vardas in studentai_pazymiai.keys():
    print(studento_vardas, "yra tarp studentu.")
else:
    print(studento_vardas, "nera tarp studentu.")

# if <SALYGA-1>:
#     print("hello")
#     ...
#     ...
# elif <SALYGA-2>:
#     ...
#     ...
# elif <SALYGA-3>:
#     ...
#     ...
# else:
#     ...