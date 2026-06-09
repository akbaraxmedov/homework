# # import avto_info as aim
# #from avto_info import avto_info as ai_info_print as ip
# from avto_info import *
#
# avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020, 40000)
# info_print(avto1)

# from math import pi, sqrt, log2, log10
#
# x =  400
# print(sqrt(x))
#
# print(pow(5,5))
#
# print(pi)
# print(log2(8))
# print(log10(100))

import random as r
son = r.randint(0, 100)
print(son)

# ismlar = ['olim', 'anvar', 'hasan', 'husan']
# ism = r.choice(ismlar)
# print(ism)
# print(r.choice(ismlar))
#
#
# x = list(range(0,51,9))
# print(x)
# print(r.choice(x))
#
# x = list(range(11))
# print(x)
# r.shuffle(x)
# print(x)

# import math
#
# uzunlik = lambda pi, r : 2*pi*r
# print(uzunlik(math.pi,10))
#
# product = lambda x, y: x**y
# print(product(3,2))
#
# def daraja(n):
#     return lambda x: x**n
#
# kvadrat = daraja(2)
# kub = daraja(3)
#
# print(f"3-ninf kvadrati")

# from math import sqrt
#
# sonlar = list(range(11))
# ildizlar = list(map(sqrt, sonlar))
# print(ildizlar)
#
#
# def daraja2(x):
#     """"Belgilangan sonning kvadrat qayataruvchi funqsiaya"""
#     return x*x
#
# print(list(map(daraja2,sonlar)))
#
#
# kvadratlar = list(map(lambda x:x*x,sonlar))
# print(kvadratlar)
#
# ismlar = ['hasan', 'husan', 'olim', 'umid']
# print(list(map(lambda matn:matn.apper(),ismlar)))
#
# import random as r
#
# sonlar = r.sample(range(100), 10)
#
# def juftmi(x):
#     """Juft bolsa True, aks holda False qaytaradigan funqsia"""
#     return x%2 ==0
#
# juft_sonlar = list(filter(juftmi,sonlar))
# print(sonlar)
# print(juft_sonlar)
#
# juft_sonlar = list(filter(lambda son: son%2 ==0, sonlar))
# print(sonlar)
# print(juft_sonlar)

