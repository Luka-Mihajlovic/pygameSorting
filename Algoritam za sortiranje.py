import pygame as pg
import math, random
pg.init()

def main():
    #promenljive
    global sirina
    global visina
    (sirina, visina) = (1080, 540)
    global prozor
    prozor = pg.display.set_mode((sirina,visina))
    prozor.fill((255,255,255))

    global dugmesir
    global dugmevis
    (dugmesir, dugmevis) = (150, 75)

    (sirinasred, visinasred) = (int(sirina / 2), int(visina / 2))

    #dimenzije i podaci za bubble sort dugme
    global bubblecenter
    global bubblesirina
    global bubblevisina
    bubblecenter = (142, 104)
    bubblesirina = int(sirinasred / 8)
    bubblevisina = int(visinasred / 4)

    #dimenzije i podaci za bogosort dugme
    global bogocenter
    global bogosirina
    global bogovisina
    bogocenter = (sirinasred, 104)
    bogosirina = int(sirinasred)
    bogovisina = int(visinasred / 4)

    #dimenzije i podaci za slection sort dugme
    global selectioncenter
    global selectionsirina
    global selectionvisina
    selectioncenter = (966, 104)
    selectionsirina = int(sirinasred * 1.666)
    selectionvisina = int(visinasred / 4)

    #slova i unos textbox
    global font
    font = pg.font.Font(None,30)
    global unostekst
    unostekst = ''

    #crtanje
    pg.draw.rect(prozor,(50,50,200),(int(bubblesirina), int(bubblevisina), int(dugmesir) , int(dugmevis)))
    pg.draw.rect(prozor,(50,50,200),(int(bogosirina-dugmesir/1.6), int(bogovisina), int(dugmesir) , int(dugmevis)))
    pg.draw.rect(prozor,(50,50,200),(int(selectionsirina), int(selectionvisina), int(dugmesir) , int(dugmevis)))
    prozor.blit((font.render(("Broj elemenata:"), True, (0,0,0))),(25,475))
    prozor.blit((font.render(("Bubble sort"), True, (255,255,255))),(bubblecenter[0] - dugmesir / 2.5, bubblecenter[1] - dugmevis / 8))
    prozor.blit((font.render(("Bogosort"), True, (255,255,255))),(bogocenter[0] - dugmesir / 2.5, bogocenter[1] - dugmevis / 8))
    prozor.blit((font.render(("Selection sort"), True, (255,255,255))),(selectioncenter[0] - dugmesir / 2.5, selectioncenter[1] - dugmevis / 8))

main()

def retry(): #za ponovno pokretanje programa
    prozor.fill((255,255,255))
    main()

def provera(element): #provera da li je unet broj elemenata u redu, da nije prazan 
    global elementproveren
    try:
        elementproveren = int(element)
    except ValueError:
        elementproveren = random.randint(10,250)

def donevisualize():
    boja = (0,255,0)
    prozor.fill((255,255,255))
    sirinaelementa = int(sirina / brojelemenata)
    for i in range(0,len(lst),1): #crtanje sortiranih elemenata u zelenoj boji
        pg.time.wait(7)
        pozx = sirinaelementa * i
        pozy = 0
        pg.draw.rect(prozor,(boja),(pozx,pozy,sirinaelementa,lst[i]))
        pg.display.update()
    pg.time.wait(10000)
    retry()

def visualize():
    boja = (0,0,0)
    prozor.fill((255,255,255)) #cisti ekran
    sirinaelementa = int(sirina / brojelemenata)
    for i in range(0,len(lst),1): #crtanje
        if mark1 == i or mark2 == i:
            boja = (255,0,0)
        else:
            boja = (0,0,0)
        pozx = sirinaelementa * i
        pozy = 0
        pg.draw.rect(prozor,(boja),(pozx,pozy,sirinaelementa,lst[i]))
    pg.display.update()

def generate():
    #kreiranje liste
    global mark1
    global mark2
    (mark1, mark2) = (-1,-1)
    global brojelemenata
    brojelemenata = elementproveren
    global lst
    lst = []

    for i in range(0,brojelemenata,1):
        rand = random.randint(10,500) #random od 10 do 500
        lst.append(rand) #puni se lista

    print("ELEMENTI:")
    for i in range(0,brojelemenata,1):
        print(lst[i])
    visualize()
    pg.time.wait(1000)
    
def bubblesort():
    global mark2
    global mark1
    #bubble sort
    for loop1 in range(0, brojelemenata, 1):
        for loop2 in range(0,brojelemenata-1,1):
            if lst[loop2] > lst[loop2+1]:
                mark2 = loop2
                mark1 = loop2+1
                t = lst[loop2] #t = temporary da skladisti vrednost promenljive
                lst[loop2] = lst[loop2+1]
                lst[loop2+1] = t
                visualize()

def bogosort():
    #random mrdanje elemenata
    counter = 0
    global mark2
    global mark1
    #loop
    while counter < brojelemenata-1:
        counter = 0
        for i in range(brojelemenata):
        
            x = random.randint(0,(len(lst)-1))
            y = random.randint(0,(len(lst)-1))
            
            t = lst[x]
            t2 = lst[y]
            lst[x] = t2
            lst[y] = t

        for loop in range(0, brojelemenata-1, 1): #provera
            if lst[loop] < lst[loop+1]:
                counter += 1
                mark2 = loop
                mark1 = loop+1
                visualize()
            else:
                break #opet random ako nije dobar poredak
            if (counter == brojelemenata-1):
                donevisualize()

def selectionsort():
    global mark1
    global mark2
    mark2 = -1 #ne koristim
    for i in range(brojelemenata):
        x = lst[i]
        j = i - 1
        while j >= 0:
            if x < lst[j]: #pomeranje unazad
                lst[j+1] = lst[j]
                lst[j] = x
                j -= 1
                mark1 = j + 1
                visualize()
            else:
                break
               
#glavna funkcija za dugme:
def dugme():
    global unostekst
    global tekstrender
    tekstrender = font.render(unostekst, True, (0,0,0))
    prozor.blit(tekstrender,(25,500))
    element = unostekst
    
    event = pg.event.wait()
    if event.type == pg.KEYDOWN:
            unostekst += event.unicode
        
    if event.type == pg.MOUSEMOTION or event.type == pg.MOUSEBUTTONDOWN:
        pozmisa = pg.mouse.get_pos() #kada se klikne ili pomeri mis pronadje se pozicija
        
        if event.type == pg.MOUSEBUTTONDOWN:
            
            if ((pozmisa[0] < bubblecenter[0] + dugmesir / 2) and (pozmisa[0] > bubblecenter[0] - dugmesir / 2)) and ((pozmisa[1] < bubblecenter[1] + dugmevis / 2) and (pozmisa[1] > bubblecenter[1] - dugmevis / 2)):
                provera(element)
                generate()
                bubblesort()
                donevisualize()
                
            elif ((pozmisa[0] < bogocenter[0] + dugmesir / 2) and (pozmisa[0] > bogocenter[0] - dugmesir / 2)) and ((pozmisa[1] < bogocenter[1] + dugmevis / 2) and (pozmisa[1] > bogocenter[1] - dugmevis / 2)):
                provera(element)
                generate()
                bogosort()

            elif ((pozmisa[0] < selectioncenter[0] + dugmesir / 2) and (pozmisa[0] > selectioncenter[0] - dugmesir / 2)) and ((pozmisa[1] < selectioncenter[1] + dugmevis / 2) and (pozmisa[1] > selectioncenter[1] - dugmevis / 2)):
                provera(element)
                generate()
                selectionsort()
                donevisualize()

while True:
    pg.time.wait(31)
    pg.display.update()
    dugme()


