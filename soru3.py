def ilk6ay(yazilimGelirleri,finansmanGelirleri,urunSatisGelirleri,calisanMasraflari,kiraGiderleri,donanimMaliyeti):
	ilk6aygeliri=yazilimGelirleri+finansmanGelirleri+urunSatisGelirleri
	ilk6aygideri=calisanMasraflari+kiraGiderleri+donanimMaliyeti
	global ilk6aykar
	ilk6aykar=ilk6aygeliri - ilk6aygideri
	return ilk6aykar
x=int(input("İlk 6 ayın yazılım gelirlerini giriniz:"))
y=int(input("İlk 6 ayın finansman gelirlerini giriniz:"))
z=int(input("İlk 6 ayın ürün satış gelirlerini giriniz:"))
p=int(input("İlk 6 ayın çalışan masraflarını giriniz:"))
r=int(input("İlk 6 ayın kira giderlerini giriniz:"))
t=int(input("İlk 6 ayın donanım giderlerini giriniz:"))
ilk6ayhesabi=ilk6ay(x,y,z,p,r,t)
print("İlk 6 ayın kar sonucu:",ilk6aykar)
def son6ay(yazilimGelirleri,finansmanGelirleri,urunSatisGelirleri,calisanMasraflari,kiraGiderleri,donanimMaliyeti):
	son6aygeliri=yazilimGelirleri+finansmanGelirleri+urunSatisGelirleri
	son6aygideri=calisanMasraflari+kiraGiderleri+donanimMaliyeti
	global son6aykar
	son6aykar=son6aygeliri - son6aygideri
	return son6aykar
a=int(input("Son 6 ayın yazılım gelirlerini giriniz:"))
b=int(input("Son 6 ayın finansman gelirlerini giriniz:"))
c=int(input("Son 6 ayın ürün satış gelirlerini giriniz:"))
d=int(input("Son 6 ayın çalışan masraflarını giriniz:"))
e=int(input("Son 6 ayın kira giderlerini giriniz:"))
f=int(input("Son 6 ayın donanım giderlerini giriniz:"))
son6ayhesabi=son6ay(a,b,c,d,e,f)
print("Son 6 ayın kar sonucu:",son6aykar)
yillikKarlilik=son6aykar-ilk6aykar
if(yillikKarlilik>=5000):
	print("İşletme yüksek kar yapmıştır.")
elif(yillikKarlilik>=1000):
	print("İşletme normal kar yapmıştır.")
else:
	print("İşletme yeterli kar sağlamamıştır.")
