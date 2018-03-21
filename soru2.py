CalismaSuresi2016=170
ToplamMusteriSayisi2016=50
CalismaSuresi2017=(CalismaSuresi2016 + 50)
ToplamMusteriSayisi2017=(ToplamMusteriSayisi2016 + 20)
def MusteriCalismaSuresi2016(CalismaSuresi2016,ToplamMusteriSayisi2016):
  MusteriCalismaSuresi2016=CalismaSuresi2016/ToplamMusteriSayisi2016
  return MusteriCalismaSuresi2016
def MusteriCalismaSuresi2017(CalismaSuresi2017,ToplamMusteriSayisi2017):
  MusteriCalismaSuresi2017=CalismaSuresi2017/ToplamMusteriSayisi2017
  return MusteriCalismaSuresi2017
farkHesabi=MusteriCalismaSuresi2016(CalismaSuresi2016,ToplamMusteriSayisi2016)-MusteriCalismaSuresi2017(CalismaSuresi2017,ToplamMusteriSayisi2017)
print ("2016-2017 yılları arasındaki müşteri sayısı farkı:",farkHesabi)
