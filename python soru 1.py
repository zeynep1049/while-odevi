def KatmaDegerCiro(ToplamSatisMiktari,HammadeMaliyeti,BakimOnarimMaliyeti,SevkiyatMiktari,SatinAlinanHizmet):
	global KatmaDegerCiro
	KatmaDegerCiro=ToplamSatisMiktari-(HammadeMaliyeti+BakimOnarimMaliyeti+SevkiyatMiktari+SatinAlinanHizmet)
	return KatmaDegerCiro
a = int(input("Toplam satış giriniz:"))
b = int(input("Hammadde maliyetini giriniz:"))
c = int(input("Bakım onarım giriniz:"))
d = int(input("Sevkiyat giriniz:"))
e = int(input("Satın alınan hizmet giriniz:"))
f=KatmaDegerCiro(a,b,c,d,e)
if(KatmaDegerCiro>=1000):
    print("İşletme katma değer cirosu yüksektir.")
elif(KatmaDegerCiro>=500 and KatmaDegerCiro<=999):
    print("İşletme katma değer cirosu normaldir.")
else:
    print("İşletme katma değer cirosu düşüktür.")
