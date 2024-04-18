

'''8. Leiskite naudotojui įvesti 10 sveikųjų skaičių, tada spausdinkite šių įvestų skaičių sumą ir vidurkį.'''


# suma = 0
# vidurkis = 0
#
# for i in range(10):
#     skaicius = int(input(f"Įveskite {i+1}-ąjį sveikąjį skaičių: "))
#     suma += skaicius
#
# vidurkis = suma / 10
#
#
# print("Įvestų skaičių suma:", suma)
# print("Įvestų skaičių vidurkis:", vidurkis)


# destytojo variantas
result = []
for i in range(10):
    number = int(input('iveskit sk'))
    result.append(number)

print(sum(result)/ len(result))

