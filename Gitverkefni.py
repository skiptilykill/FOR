#Guðmundur jóns
#25.1.2017

#Dæmi 1

tala1 = int(input("Sláðu inn tölu: "))
tala2 = int(input("sláðu inn aðra tölu: "))

print("Tölurnar lagðar saman: ", tala1+tala2)
print("Tölurnar margfaldaðar: ", tala1*tala2)

#Dæmi 2

fn = input("Fornafn? ")
ef = input("Eftirnafn? ")
print(fn , ef)

#Dæmi 3

texti=input("Enter something: ")
c = 0
b = 0
for i in texti:
    if i.isupper():
        c += 1
for i in texti:
    if i.islower():
        b += 1
print("Hástafir", c)
print("Lágstafir", b)