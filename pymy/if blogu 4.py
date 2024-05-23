isim=input('isminiz: ')
yas=int(input('yas: '))
egitimdurumu=input('egitim: ')
if (yas>=18):
    if (egitimdurumu=='lise' or egitimdurumu=='universite'):
        print(f'{isim} ehliyet Alabilrsin')
    else:
        print(f'{isim} ehliyet alamazsin')
else:
    print(f'{isim} ehliyet yas tutmuyor')
