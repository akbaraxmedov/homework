# cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# my_cars = cars[2:4]
# print(my_cars)
# print(cars[2:5])
# print(cars[:4])
# print(cars[2:])
#
#
# sonlar = [1, 2, 3, 4, 5,]
# sonlar2 = sonlar[:]
# sonlar2.append(6)
# sonlar2.appen(7)
# print("Bu sonlar royxati:", sonlar)
# print("Bu sonlara2 royhati:", sonlar2)

tomonlar = (20, 30, 55.2)
print(tomonlar)

toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizart')
toys = list(toys)
#
toys.append('dragon')
toys.remove('bus')
toys[1] = 'mcquen'
toys = tuple(toys)
print(toys)


mehmonlar = ['Jonibek', 'Temurbek', 'Javlonbek', 'Otkirbek']
for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon}, siz 20-Mart kuni oshga taklif qilamiz")
    print("Hurmat bilan, Palinchiyevlar oylasi")


sonlar = list(range(1,11))
for son in sonlar:
    print(f"{son} ning kvadrati {son**2} ga teng")


sonlar = list(range(11))
sonlar_kvadrati =[]
for son in sonlar:
    sonlar_kvadrati.append(son**2)

print(sonlar)
print(sonlar_kvadrati)

dostlar = []
print("5 ta eng yaqin dostingiz kim?")
for n in range(5):
    dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting:"))
print(dostlar)

