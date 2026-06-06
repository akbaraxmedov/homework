# def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
#     """Toliq ism qaytaruvchi funksiya"""
#     if otasining_ismi:
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()
#
# talaba1 = toliq_ism_yasa('olim', 'hakimov')
# talaba2 = toliq_ism_yasa('hakim', 'olimov', 'abrorovich')
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
#
# def avto_info(kompaniya, model, rang, korobka, yili, narxi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rang,
#             'korobka':korobka,
#             'yili':yili,
#             'narxi':narxi}
#     return avto
#
# avto1 = avto_info('GM', 'Malibu', 'Qora', 'Avtomat', 2018)
# avto2 = avto_info('GM', 'Gentra', 'Oq', 'Mexanika', 2016, 15000)
# avtolar = [avto1, avto2]
# print('Online bozordangi mavjud avtomashinalar: ')
# for avto in avtolar:
#     if avto['narxi']:
#         narx = avto['narxi']
#     else:
#         narx = "Nomalum"
#     print(f"{avto['rang']} {avto['model']}. narxi:{'narxi'}")


# def avto_info(kompaniya, model, rang, korobka, yili, narxi=None):
#     avto = {'kompaniya':kompaniya,
#             'rang':rang,
#             'korobka':korobka,
#             'yili':yili,
#             'narxi':narxi}
#     return avto
#
# print("Saytimizdagi avtolar ro'yxatini shakilantiramiz.")
# avtolar = []
# while True:
#     print("\nQydagi malumotlarni kiriting")
#     kompaniya = input("ishlab chiqaruvchi: ")
#     model = input("Model: ")
#     rang = input("Rang: ")
#     korobka = input("Korobka: ")
#     yili = input("Ishlab chiqarilgan yili: ")
#     narxi = input("Narxi: ")
#

 # """javob = input("yana avto qoshsizmi?"""
 # print(avtolar)
# #     avtolar.append(avto_info(kompaniya, model, rang, korobka, yili, narxi))
# car0 = {eak
#
#     'model':'lasetti',
#     'rang':'oq',
#     'yil':'2019',
#     'narxi':9000,
#     'km':89000,
#     'korobka':'avtomat'
#
# }
#
# car1 = {
#     'model': 'lasetti',
#     'rang': 'oq',
#     'yil': '2019',
#     'narxi': 9000,
#     'km': 89000,
#     'korobka': 'mexanik'
#
# }
#
# car2 = {
#     'model': 'lasetti',
#     'rang': 'oq',
#     'yil': '2019',
#     'narxi': 9000,
#     'km': 89000,
#     'korobka': 'mexanik'
#
# }
#
# malibus =[]
# for n in range(10):
#     new_car = {
#         'model':'malibus',
#         'rang':'None',
#         'yil':2020,
#         'narx':None,
#         'km':0,
#         'akrobka':'avto'
#     }
#     malibus.append(new_car)
#
# print(malibus)

