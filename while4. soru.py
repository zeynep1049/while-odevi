calisan=50
yevmiye=40
aylik_mesai=0
haftalik_maas=630
aylik_maas=0
while aylik_mesai<=22:
    haftalik_mesai=int(input('Haftalık mesai:'))
    aylik_mesai=haftalik_mesai*4
    haftalik_maas=haftalik_maas+(haftalik_mesai*yevmiye*0.10)
    aylik_maas=aylik_maas+haftalik_maas*4
    print('Aylık Maaş:',aylik_maas)
else:
    print('Aylık mesai 22 saatten fazla olamaz')
