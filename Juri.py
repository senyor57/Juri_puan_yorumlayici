juripuanlist = []
def jurisor():

    sayac = 1
    while sayac < 6:

        juripuanlar = int(input(" {}. juri lütfen puanınızı giriniz ".format(sayac)))
        juripuanlist.append(juripuanlar)
        sayac += 1

def ortalamahesapla(defaultliste):

    top = 0
    elemansayi = len(defaultliste)
    for i in juripuanlist:
        top = i + top
    return top / elemansayi








def yorumlar():
    if ortalama >= 3.5 and ortalama <= 5:
        print("Geçemediniz biraz daha çalışınız ")


    elif ortalama >=1 and ortalama <=3 :
        print("juri sizi hiç beğenmemiş")

    elif ortalama > 5 and ortalama <=7:
        print("Geçtiniz başarılar...")

    elif ortalama > 7 and ortalama <=9:
        print("Muhteşemdiniz juri hayran kaldı...","ortalamanız : {}".format(ortalama))



jurisor()
ortalama=ortalamahesapla(juripuanlist)
yorumlar()