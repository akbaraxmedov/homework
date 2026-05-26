#append() — Roʻyxatning eng oxiriga yangi bitta element qoʻshadi
# 1.1
ismlar = ['Ali', 'Vali']
ismlar.append("Sali")
print(ismlar)

# 1.2
soat = ["12:00", "12:10", "12:20"]
soat.append("12:30")
print(soat)


#extend() — Boshqa roʻyxatni toʻliq qismlarga boʻlib qoʻshadi
# 2.1
katalog = ["futbolka", "Shapka"]
yangi_tavarlar = ["shim","kurtka"]
katalog.extend(yangi_tavarlar)
print(katalog)

# 2.2
x_kordinatlar = [10, 20]
y_kordinatlar = [30, 40]
x_kordinatlar.extend(y_kordinatlar)
print(x_kordinatlar)


#insert() — Elementni aniq koʻrsatilgan indeksga joylashtiradi
# 3.1
moshinalar = ["bmw 1", "malibu 2", "byd 3"]
moshinalar.insert(1,"VIP bmw")
print(moshinalar)

# 3.2
text = ["Salom", "dunyo"]
text.insert(1,"gozal")
print(text)


# pop() — Indeksdagi elementni oʻchiradi va uni sugʻurib oladi
# 4.1
footbolchilar = ["Shaxrux", "Akbar", "Ali"]
zaxira = footbolchilar.pop()
print(zaxira)
print(footbolchilar)

# 4.2
qurollar = ["Pichoq", "Avtomat", "Granata"]
ochirilgan = qurollar.pop(1)
print(ochirilgan)
print(qurollar)


# remove() — Koʻrsatilgan qiymatni nomi boʻyicha oʻchiradi
# 5.1
ismlar = ["Akbar", "Shaxrux", "Farangiz"]
ismlar.remove("Farangiz")
print(ismlar)

# 5.2
inventar = ["Arava", "Dori", "Qilich"]
inventar.remove("Dori")
print(inventar)


# clear() — Roʻyxatni butunlay boʻshatadi
# 6.1
achkolar = [150, 300, 100]
achkolar.clear()
print(achkolar)

# 6.2
javoblar = ["A", "B", "C", "D"]
javoblar.clear()
print(javoblar)


# count() — Element necha marta qatnashganini sanaydi
# 7.1
kunlar = ["yomgir", "quyosh", "yomgir", "quyosh","bulut"]
print(kunlar.count("ymgir",))

# 7.2
tavarlar = [101, 202, 101, 303, 101]
print(tavarlar.count(101))


# index() — Element turgan birinchi indeksni (joyni) qaytaradi
# 8.1
tags = ["html", "body", "div", "p"]
print(tags.index("p"))

# 8.2
ovqatlar = ["manti", "somsa", "shashlik"]
print(ovqatlar.index("manti"))


# sort() — Elementlarni oʻsish yoki alifbo tartibida saralaydi
# 9.1
sonlar = [12, 13 , 1, 4, 0, 99]
sonlar.sort()
print(sonlar)

# 9.2
shaharlar = ["Samarqand", "Andijon", "Xiva", "Xorazm"]
shaharlar.sort()
print(shaharlar)


# reverse() — Tartibni shunchaki teskari qiladi
# 10.1
sonlar = [12, 13 , 1, 4, 0, 99]
sonlar.reverse()
print(sonlar)

# 10.2
shaharlar = ["Samarqand", "Andijon", "Xiva", "Xorazm"]
shaharlar.reverse()
print(shaharlar)

# copy() — Roʻyxatning mustaqil nusxasini yaratadi
# 11.1
natija = [85, 90, 75]
nusxa = natija.copy()
nusxa[0] = 100
print(natija)
print(nusxa)

# 11.2
shape_1 = [0, 0, 100, 100]
shape_2 = shape_1.copy()
print(shape_2)
