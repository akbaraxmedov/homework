harorat = float(input("Bugun ob-havo kanday: "))
if harorat < 0:
    print("sovuq")
elif 0 <= harorat <=20:
    print("salqin")
elif 21 <= harorat <=30:
    print("iliq")
else:
    print("issiq")

summa = float(input("Xarid summasini kiriting: "))
if summa < 50000:
    chegirma_foyizi = 0
    print("chegima 0%")
elif 50000 <= summa <+100000:
    chegirma_foyizi = 5
    print("chegirma 5%")
else:
    chegirma_foyizi = 10
    print("chegirma 10%")
yakuniy_narx =  summa * (1 - chegirma_foyizi / 100)
print(f"yakuniy_narx: {yakuniy_narx}")


login = input("liginingizni kiriting: ")
parol = float(input("parolingizni kiriting: "))
if login=='admin' and parol ==12345:
    print("Xush kelibsiz admin")
else:
    print("Login yoki parol xato!")

