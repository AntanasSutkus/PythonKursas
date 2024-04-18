"""
ciklai
"""
import time

# i = 10
# while True:
#     print(i)
#     time.sleep(1)
#     if i==15:
#         break
# else:
#     print('gjgyj')




# i = 10
# while i> 5:
#     print(i)
#     i-=1


# for i in range(10):
#     print(i)
#     if i == 8:
#         break #arba continue(tada praleidzia


# for i in range(10):
#     print(i)
#     if i == 8:
#         continue
#
# #listai, tuplai, dictai , stringai yta ITERABLE


"""1 Sukurkite kintamuosius, kuriuose reprezentuotų vartotojo vardą ir slaptažodį. Pradėkite begalinį ciklą, leidžiantį įvesti vartotojo vardą ir slaptažodį. Jei duomenys teisingi, sustabdykite begalinį ciklą ir išspausdinkite pasisveikinimo pranešimą."""

print(".....8 pamoka....I uzduotis....")

corect_name = "Antanas"
corect_password = "123456"

while True:
    name = input("Input username:")
    password = input("input paas:")

    if corect_name == name and corect_password == password:
        print("hello", name)
        break

    else:
        print("Wrong user data, try again")





