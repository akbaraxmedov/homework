def sonlar_kopaytmasi(*sonlar):

    if not sonlar:
        return 0

    kopaytma = 1
    for son in sonlar:
        kopaytma *= son
    return kopaytma


# Funksiyani tekshiramiz
print(sonlar_kopaytmasi(100, 300, 400))


def talaba_malumoti(ismi, familiyasi, **ixtiyoriy_malumotlar):

    talaba = {
        'ism': ismi,
        'familiya': familiyasi
    }
    talaba.update(ixtiyoriy_malumotlar)

    return talaba

talaba1 = talaba_malumoti("Ali", "Valiyev")
print(talaba1)

talaba2 = talaba_malumoti("Zilola", "Karimova", yoshi=20, kursi=3, stipendiya=True, fakultet="IT")
print(talaba2)


#Talabalar baholarining o'rtachasini hisoblash
def talabaning_ortacha_bahosi(ism, *baholar):
    if not baholar:
        return f"{ism}ning baholari kiritilmagan."

    ortacha = sum(baholar) / len(baholar)

    return f"{ism}ning o'rtacha bahosi: {ortacha:.1f}"


natija = talabaning_ortacha_bahosi("Anvar", 5, 4, 3, 5, 2, 5)
print(natija)


#Mahsulot haqida ma'lumot yaratish
def mahsulotlar(nomi, **qoshimcha_malumotlar):

    mahsulot = {
        "nomi": nomi,

    }

    # **kwargs orqali kelgan barcha qo'shimcha ma'lumotlarni lug'atga qo'shamiz
    mahsulot.update(qoshimcha_malumotlar)

    return mahsulot


# Funksiyani turli xil mahsulotlar uchun sinab ko'ramiz:

# 1-misol: Telefon uchun
meva = mahsulotlar("olma", narxi="12000", kg="10", olivb_kelingan="olmazor",)
print(meva)

# 2-misol: Oyoq kiyim uchun
kiym_kechak = mahsulotlar("futbolka", brend="Nike", olchami=52, rangi="Qora")
print(kiym_kechak)