
# 1

val = 0
metin = "bir sayı girin  "+"( "+"cıkmak icin e ya da E"+" ) : "

while True:

    val = input(metin)
    
    if (val == 'e') or (val == 'E'):
        break
    else:
        val = int(val)
        
    if val%2 == 0:
        print("{} sayısı cifttir".format(val))
    else:
        print("{} sayısı tektir".format(val))        
        

# 2

metin = "cıkmak icin e ya da E , devam etmek icin c ya da C : "

while True:

    liste = [0,0,0,0,0]
    print("5 adet sayi girin")
    
    for x in range(5):
        liste[x] = int(input("sayi girin : "))
    
    
    for x in range(5):
        val = 0
        y = 2
        while y < liste[x]:
            if liste[x]%y == 0:
                val += 1
            y += 1
            
        if val == 0:
            print("{} sayısı asal sayidir".format(liste[x]))
        else:
            print("{} sayısı asal sayi degildir".format(liste[x]))
        
    
    deger = input(metin)
    if (deger == 'e') or (deger == 'E'):
        break
    elif (deger == 'c') or (deger == 'C'):
        pass
    else:
        print("yanlıs deger girdiniz islem devam ediyor")
  

  
# 3

def TemizVeri():
    ilk_string ="Ah5me4t"
    ikinci_string = "M9eHm4eT"
    ucuncu_string ="Ha3K5a1n"
 
    liste = ['','','']
    
    metin = list(ilk_string)
    sayi = ''
    a = 0
    
    while a < len(metin):
        if metin[a].isalpha():
            sayi = sayi + metin[a]
        a += 1

    liste[0] = sayi
    
    
    metin = list(ikinci_string)
    sayi = ''
    a = 0
    
    while a < len(metin):
        if metin[a].isalpha():
            sayi = sayi + metin[a]
        a += 1

    liste[1] = sayi
    
    metin = list(ucuncu_string)
    sayi = ''
    a = 0
    
    while a < len(metin):
        if metin[a].isalpha():
            sayi = sayi + metin[a]
        a += 1
 
    liste[2] = sayi
    
    Birlesmis_deger = "-".join(liste)
 
    return Birlesmis_deger
 
 
istenen = TemizVeri()
print(istenen)



