liste = [12,12,32,44,45, "dasd"]
for eleman in liste :
     print(eleman)


liste2 = list() #[]
kelime= "merhaba"
print(len(liste2))

kelimeliste = list(kelime)
print (kelimeliste)


kelime2="merhaba dünya"
"""
son karakter -1, len(kelime)-1
"""
print(kelime2[len(kelime2)-1])

meyveler = ["elma","armut","çilek","şeftali"]
print(meyveler[2])
print("----------------------------")

for meyve in meyveler:
     print(meyve)

print(meyveler[2:5])

"""[soru] ahmet poşete sevdiği meyvelerden ekleyip spor spor sonrasi yemek istiyor. daha sonra yanlıklışla sevmediği armut 
meyvesinde poşete yanlışlıkla kooyfuğunu görüyor. poşetten aemutu çıkarıp yerine koymak istiyor.
bu örneği listelerde gösteriniz.
"""

poset = ["armut","muz","çilek","üzüm"]
print(poset)
print("------------------------")
poset(0)="elma"
print(poset)

for i in enumerate(poset):
     if poset(i)=="armut":
          poset(i)="elma"

"""
del poset1
print(poset1)
"""
tumPoset.remove("elma")
print(tumPoset)