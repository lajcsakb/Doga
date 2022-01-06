#Kérj be 2 számot és döntsd el, hogy melyik a nagyobb!

elso=input('Add meg az első számot!')
elso=int(elso)

masodik=input('Add meg a második számot!')
masodik=int(masodik)

if elso>masodik:
      print('A nagyobb érték:',elso)
elif elso<masodik:
      print('A nagyobb érték:',masodik)
else:print('A 2 szám egyenlő')

