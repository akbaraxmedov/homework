#3-masala:
sozlar = ["akbar", "etibor", "images", "qoptok", "shaftoli", "olim"]
sozlar2 = ("a", "e", "i", "o", "u", "oʻ")

natija = list(filter(lambda x: x.startswith(sozlar2), sozlar))
print(natija)


#4-masala:
sonlar = [43, 45, 234, 200, 34, 6454, 100, 42, 100, 101]

filtr = list(filter(lambda x : 100 <= x <=999, sonlar))
print(filtr)


#5-masala:
ismlar = ['olim', 'ali', 'vali', 'husan', 'hasan']

qoshish = list(map(lambda x: "Mr "+ x, ismlar))
print(qoshish)


#6-masala:
sonlar3 = [2, 5, 34, 22, 1, 23, 56]

filtr = list(map(lambda x : x * 10 ,filter(lambda x : x % 2==0, sonlar3)))

print(filtr)
