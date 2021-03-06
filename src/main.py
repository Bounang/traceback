#-*- coding:utf-8 -*-

import Image

im = Image.open("nathalie.jpg")

#on récupère les dimensions de l'image
w,h=im.size

#On éclate l'image en trois (rouge vert bleu)
r,g,b=im.split()

#on transforme l'image en liste
r=list(r.getdata())

#le message à  coder
c="Histoire d'un premier amour"

#on note la longueur de la chaine et on la transforme en binaire
u=len(c)
v=bin(len(c))[2:].rjust(8,"0")

#on transforme la chaine en une liste de 0 et de 1 
ascii=[bin(ord(x))[2:].rjust(8,"0") for x in c]

#transformation de la liste en chaine
a=''.join(ascii)

#on code la longueur de la liste dans les 8 premiers pixels rouges
for j in range(8):
    r[j]=2*int(r[j]//2)+int(v[j])

#on code la chaine dans les pixels suivants
for i in range(8*u):
    r[i+8]=2*int(r[i+8]//2)+int(a[i])

#on recrée l'image rouge 
nr = Image.new("L",(16*p,16*q))
nr = Image.new("L",(w,h))
nr.putdata(r)

#fusion des trois nouvelles images
imgnew = Image.merge('RGB',(nr,g,b)) 
imgnew.save("couverture.png") 