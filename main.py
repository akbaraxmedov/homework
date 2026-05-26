# 1 capitalize()	Converts the first character to upper case
# 1.1 ismni birinchi harifi togirlaydi (1-katta kiladi)
ism = "shoxrux"
print(ism.capitalize())

# 1.2 agar text caps lockda yozilgan bolsa togirlaydi
text = "BU MATN KECHASI YOZILMOQDA"
print(text.capitalize())


# 2 casefold()	Converts string into lower case
# 2.1
print("fuбball".casefold() == "fussball")

# 2.2 kichik hariga otkazadi
print("MOBILE".casefold())


# 3 center()	Returns a centered string
# 3.1 Barcha hariflarni kichik qikadi
email = "ALLAnazaroVshoxrux@gMAil.COM"
print(email.lower())

# 3.2 Foydalanuvchi javobini registrni hisobga olmay tekshirish
user = "ChIQiSh"
print(user.lower() == "chiqish")


# 4 upper()	Converts a string into upper case
# 4 Barcha hariflarni katta kiladi
# 4.1 Tizim xatolarini log faylda ajratib qorsatadi
status = "men_bilaman"
print(status.upper())

# 4.2 Promo codlarni avtomatik katta harif kilsh
promo = "im500fic"
print(promo.upper())


# 5 swapcase()	Swaps cases, lower case becomes upper case and , versa
# Katta xariflarni kichik , kichik harifni katta qiladi
# 5.1 Tasodifan caps lock blan yozilgan matn
text = "sALOM DUNYO !"
print(text.swapcase())

# 5.2 Hariflarni teskari qilish
code = "PyThOn5"
print(code.swapcase())


# 6 title()	Converts the first character of each word to upper case
# title() — matndagi har bir soʻzning birinchi harfini katta qiladi
# 6.1
ism_fo = "karimov sardor aliyevech"
print(ism_fo.title())

# 6.2 Maqola sarlavhasini tayorlash
text = "pthon dasturlash tili"
print(text.title())


# 7 isalnum()	Returns True if all characters in the string are alphanumeric
# Matn faqat harf va raqamlardan iboratligini tekshradi
# 7.1 logim tekshirish
parol = "Shaxrux707"
print(parol.isalnum())

# 7.2 logim tekshirish
parol = "Shaxrux @ 707"
print(parol.isalnum())


# 8 isalpha()	Returns True if all characters in the string are in the alphabet
# isalpha() — matn FAQAT harflardan iboratligini tekshiradi
# 8.1 kiritilgan ismni tekshirish
ism = "Shaxrux"
print(ism.isalpha())

# 8.2 Ichida raqam bolsa folse beradi
ism1 = "Shaxruh123"
print(ism1.isalpha())


# 9 isascii()	Returns True if all characters in the string are ascii characters
# isascii() — matn faqat ASCII (inglizcha) belgilardan iboratligini tekshiradi
# 9.1 parol faqat ingiliz hariflardan tuzilganini tekshiradi
parol = "parol123"
print(parol.isascii())

# 9.2 kiritilgan hariflar o'zbekcha (rus) bolsa folse
parol = "parol ффsalom"
print(parol.isascii())


# 10 isdigit()	Returns True if all characters in the string are digits
# isdigit() — matn raqamlardan iboratligini tekshiradi (daraja belgilarini ham taniydi)
# 10.1 yosh kiritilgan maydonni tekshiradi
yosh = "26"
print(yosh.isdigit())

# 10.2 Daraja belgisini ham raqam deb hisoblaydi
yosh = "²"
print(yosh.isdigit())