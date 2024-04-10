




"""10.1 Patys sukurkite bent 5 skirtingas funkcijas ir jas išbandykite"""

def sveikinimas(vardas):
    print("sveiki ponas", vardas)

sveikinimas("Petrai")

def dauginam(a, b, c=8):
    result = a*b*c
    print(result)

dauginam(2,4)


def keliam_kubu(a):
    rez = a ** 3
    print(rez)
keliam_kubu(5)


"""10.2 Sukurkite funkciją, kuri prie kiekvieno list nario prideda string galūnę."""

def pridedam_galune(sarasas, galune):
    for i in range(len(sarasas)):
        sarasas[i] += galune

    return sarasas

sarasas = ["saul", "melyn", "aviet"]
galune = "e"

print(pridedam_galune(sarasas, galune))


def add_string(values, end_string = "stringeris") :
    return [f'{d}_{end_string}' for d in data]

data = [1,3, "namas", "Kepure"]
end_string = 'stringeris'
print(add_string(values=data, end_string=end_string))

"""10.3 Sukurkite mini python programą, kuri kaip įvestį paimtų du skaičius ir grąžintų jų sumą, 
atimtį, dalybą, daugybą"""

# def veiksmai(a,b):
#     suma = a + b
#     skirtumas = a - b
#     sandauga = a * b
#     if b !=0:
#         dalyba = a / b
#     else:
#         dalyba = "dalyba is 0 negalima"
#     return suma, skirtumas, sandauga, dalyba
#
# a = float(input("Enter first numb:"))
# b = float(input("Enter second numb:"))
#
# suma, skirtumas, sandauga, dalyba = veiksmai(a, b)
# print(f"Suma: {suma}")
# print(f"Skirtumas: {skirtumas}")
# print(f"Sandauga: {sandauga}")
# print(f"Dalyba: {dalyba}")



a = float(input("Įveskite pirmą skaičių: "))
b = float(input("Įveskite antrą skaičių: "))

rezultatai = [(a + b), (a - b), (a * b), (a / b if b != 0 else "Dalyba iš nulio negalima")]

print("Rezultatai:", rezultatai)


"""10.4 Sukurkite funkciją, kuri grąžintų tik unikalius simbolius turinčias string reikšmes."""

def unikaliu_simboliu_stringai(sarasas):
    unikalios_reiksmes = []
    for i in sarasas:
        if len(set(i)) == len(i):
            unikalios_reiksmes.append(i)
    return unikalios_reiksmes

sarasas = ["abc", "def", "aba", "xy", "hello", "world","miegas","zole","abrikosas"]
unikalus_sarasas = unikaliu_simboliu_stringai(sarasas)
print(unikalus_sarasas)


"""10.4 Parašykite programą, apibrėžiančią funkciją extract_email_addresses(), kuri priima tekstą kaip įvestį ir iš teksto ištraukia visus el. pašto adresus."""

def extract_email_addresses(text):

    words = text.split()
    emails = []
    for word in words:

        if '@' in word:

            if word.count('@') == 1:
                emails.append(word)
    return emails

tekstas = "Mano el. pašto adresas yra jonas@example.com, o dar vienas adresas yra info@company.com."
print("Ištraukti el. pašto adresai:")
print(extract_email_addresses(tekstas))







