

"""1 pratimas: Parašykite Python programą, kad surastumėte dažniausiai pasitaikančius elementus ir jų skaičių nurodytame tekste.
Originali eilutė: lkseropewdssafsdfafkpwe
Dažniausiai trys minėtos eilutės simboliai [('s', 4), ('e', 3), ('f', 3)]"""

from collections import Counter

def daugiausiai_pasitaikancios(eilute, kiekis):
    pasikartojimai = Counter(eilute)
    daugiausiai = pasikartojimai.most_common(kiekis)
    return daugiausiai

eilute = "lkseropewdssafsdfafkpwe"
daugiausiai = daugiausiai_pasitaikancios(eilute, 3)
print("Dažniausiai trys minėtos eilutės simboliai:", daugiausiai)


"""destytojo"""

def return_most_common(text, number=3):
    result = []
    for l in set(text):
        result.append((l, text.count(l)))
    result.sort(key=lambda x: x[1], reverse=True)
    return result[:3]


'''2 .pratimas: 
1) Sukurkite sąrašą, pasirinkdami nelyginius indekso elementus iš pirmojo sąrašo 
2) ir lyginius indekso elementus iš antrojo

Turėdami du sąrašus, l1 ir l2, parašykite programą, kuri sukurtų trečiąjį sąrašą l3, pasirinkdami nelyginį indekso elementą iš sąrašo l1 ir lyginius indekso elementus iš sąrašo l2.

Duota:
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
Numatoma išvestis:
Elementas nelyginėse indekso pozicijose iš pirmojo sąrašo
[6, 12, 18]
Elementas lyginio indekso pozicijose iš antrojo sąrašo
[4, 12, 20, 28]
Spausdinimas Galutinis trečiasis sąrašas
[6, 12, 18, 4, 12, 20, 28]'''


def sarasas3(l1,l2):
    return(l1[1::2]+l2[::2])

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

print(sarasas3(l1,l2))



def kuriam_sarasa(l1, l2):
    nelyginiu_el_sar_l1 = []
    lyg_el_sar_l2 = []

    for i in l1:
        if i % 2 != 0:
            nelyginiu_el_sar_l1.append(i)

    for i in l2:
        if i % 2 ==0:
            lyg_el_sar_l2.append(i)

    galutinis_sar = nelyginiu_el_sar_l1 + lyg_el_sar_l2
    return galutinis_sar

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

print(kuriam_sarasa(l1,l2))



'''3 pratimas: sukurkite Python rinkinį taip, kad elementas iš abiejų sąrašų būtų rodomas poroje.

Duota:
pirmasis_sąrašas = [2, 3, 4, 5, 6, 7, 8]
antrasis_sąrašas = [4, 9, 16, 25, 36, 49, 64]
Numatoma išvestis:
Rezultatas yra {(6, 36), (8, 64), (4, 16), (5, 25), (3, 9), (7, 49), (2, 4)'''

pirmasis_sąrašas = [2, 3, 4, 5, 6, 7, 8]
antrasis_sąrašas = [4, 9, 16, 25, 36, 49, 64]

# Sukuriame rinkinį su poromis
poros = {(x, y) for x, y in zip(pirmasis_sąrašas, antrasis_sąrašas)}

print("Rezultatas yra:", poros)


"""destytojo 1"""

def return_zipped_data(listas_1, listas_2):
    result = []
    for i in range(len(listas_1)):
        result.append((listas_1[i], listas_2[i]))
    return result

"""destytojo 2"""

def return_zipped_data(listas_1, listas_2):
    result = []
    for i, _ in enumerate(listas_1):
        result.append((listas_1[i], listas_2[i]))
    return result

"""destytojo 3"""

def return_zipped_data(listas_1, listas_2):
    result = []
    for value_1, value_2 in zip(listas_1, listas_2):
        result.append((value_1, value_2))
    return result

"""arba lengviau"""

def return_zipped_data(listas_1, listas_2):
    return set(zip(listas_1, listas_2))

'''4 pratimas: pakartokite duotą sąrašą ir patikrinkite, ar tam tikras elementas egzistuoja kaip rakto reikšmė žodyne. 
Jei ne, ištrinkite jį iš sąrašo

Duota:
ritinio_skaičius = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
Numatomas rezultatas:
Pašalinus nepageidaujamus elementus iš sąrašo [47, 69, 76, 97]'''


def removinam(ritinio_skaicius,sample_dict):
    naujas_sarasas = []

    for i in ritinio_skaicius:
        if i in sample_dict.values():
            naujas_sarasas.append(i)
    return naujas_sarasas

ritinio_skaicius = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

naujas_sarasas = removinam(ritinio_skaicius,sample_dict)
print(naujas_sarasas)


'''list comperhension by ChatGpt'''

def removinam(ritinio_skaicius, sample_dict):
    naujas_sarasas = [x for x in ritinio_skaicius if x in sample_dict.values()]
    return naujas_sarasas

ritinio_skaicius = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

naujas_sarasas = removinam(ritinio_skaicius, sample_dict)
print("Pašalinus nepageidaujamus elementus iš sąrašo:", naujas_sarasas)


'''5 pratimas: gaukite visas reikšmes iš žodyno ir įtraukite jas į sąrašą, bet nepridėkite dublikatų
Duota:
greitis = {'sausis': 47, 'vasaris': 52, 'kovas': 47, 'balandis': 44, 'gegužė': 52, 'birželis': 53, 'liepa': 54, 
'rugpjūtis': 44 , "rugsėjis": 54}
Numatomas rezultatas:
[47, 52, 44, 53, 54]'''

def value_to_list(greitis):

    rezultatas =[]

    for i in greitis.values():
        if i not in rezultatas:
            rezultatas.append(i)
    return rezultatas

greitis = {'sausis': 47, 'vasaris': 52, 'kovas': 47, 'balandis': 44, 'gegužė': 52, 'birželis': 53, 'liepa': 54,
'rugpjūtis': 44 , "rugsėjis": 54}

print(value_to_list(greitis))


