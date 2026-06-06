def baholaar(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()}ning bahosini kiirting: ")
        baholar[ism]=baho
    return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = baholar(talabalar[:])
# print(talabalar)
def katta_harf(matnlar):
    for i in range(len(matnlar)):
        matnlar[i] = matnlar[i].title()


ismlar = ['ali', 'vali', 'hasan', 'husan']
katta_harf(ismlar)
print(ismlar)


talabalar = ['ali', 'vali', 'hasan', 'husan']
def baholar(ismlar):
    baholar = {}
    for ism in ismlar:
        baho = input(f"Talaba {ism.title()}ning bahossini kiirting: ")
        baholar[ism] = baho
    return baholar

baholar = baholar(talabalar)
print(talabalar)


def summa(*sonlar):
    yigindi = 0
    for son in sonlar:
        yigindi += son
    return yigindi

print(summa(1,2,5,-6,4,0))
print(summa(1,2,3,4,5))

# def summa(*sonlar):


def summa(x,y, sonlar):
    return x+y+sum(sonlar)
print(summa(2,8,3,6,5,1))


print(baholar)

def avto_info(kompaniya, model, **malumotlar):
    malumotlar['kompaniya'] = kompaniya
    malumotlar['model'] = model
    return malumotlar

avto1 = avto_info("GM", 'malibu', rang='qora, yil=2020')
avto2 = avto_info("kia", 'K5', rang='qizil, narh=35000')
print(avto1)
print(avto2)



