toplam=0
while True:
    print('Bir sayı giriniz, Çıkış için 0(sıfır)')
    girilen=int(input("Sayı:"))
    if(girilen!=0):
        a=girilen%3
        toplam=toplam+a
        print("Toplam=",toplam)
    else:
        print("çıkış yapıldı")
        break
        
    
