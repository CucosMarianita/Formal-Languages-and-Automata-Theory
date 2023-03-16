from bs4 import BeautifulSoup
import sys
import requests
import re
import lxml


def getHTMLdocument(url):
    response = requests.get(url)
    return response.text


url_to_scrape = "https://www.olx.ro/locuri-de-munca/"  # url initial din care putem sa cream paginile
urls_on_pages = [url_to_scrape]  # lista cu url-ul fiecarei pagini
for i in range(1):
    urls_on_pages.append(url_to_scrape + f"?page={i}")

print(urls_on_pages)


# for i in range(len(urls_on_pages)):
def htmlToSoup(link):
    print(link)
    html_document = getHTMLdocument(link)  # documentul html ca string
    # print(html_document)
    soup = BeautifulSoup(html_document, 'lxml')  # fisierul html ca soup
    # print(soup.prettify())
    return soup


lsLink = []  # contine toate linkurile care duc spre pagina proprie a unui anunt pentru a putea parsa descrierea

for url in urls_on_pages:
    soup = htmlToSoup(url)
    contine_link = soup.find_all('div', class_='space rel')  # o parte din html care contine linkul catre pagina anuntului
    # print(contine_link)
    for element in contine_link:
        newSoup = element
        link = newSoup.find_all('a')
        # print(type(link))
        for el in link:
            lsLink.append(el.get('href'))

lista_descriere = []  # titlul plus descrierea pentru fiecare anunt
x = 0
for linkDescriere in lsLink:
    # print(x)
    # x += 1
    # if x == 20:
    #     break
    soup = htmlToSoup(linkDescriere)
    # lista_descriere.append(soup)
    descriere = str(soup.find('div', class_='css-2t3g1w-Text'))
    titlu = str(soup.find('h1', class_='css-r9zjja-Text eu5v0x0'))
    lista_descriere.append((titlu, descriere))
# print(lista_descriere)
# print(lista_descriere[0])

# ----------------------------------------------------------------------------------


f = open("date.txt", "w", encoding="utf-8")

f.write("1.Tari:")
# germania = 0
germania = bulgaria = franta = italia = anglia = danemarca = belgia = olanda = spania = grecia = 0
for element in lista_descriere:
    if re.findall('(?i)germania', element[0]) or re.findall('(?i)germania', element[1]):
        germania += 1
    if re.findall('(?i)bulgaria', element[0]) or re.findall('(?i)bulgaria', element[1]):
        bulgaria += 1
    if re.findall('(?i)franta|fran.a|franța', element[0]) or re.findall('(?i)franta|franța|fran.a', element[1]):
        franta += 1
    if re.findall('(?i)italia', element[0]) or re.findall('(?i)italia', element[1]):
        italia += 1
    if re.findall('(?i)anglia', element[0]) or re.findall('(?i)anglia', element[1]):
        anglia += 1
    if re.findall('(?i)danemarca', element[0]) or re.findall('(?i)danemarca', element[1]):
        danemarca += 1
    if re.findall('(?i)belgia', element[0]) or re.findall('(?i)belgia', element[1]):
        belgia += 1
    if re.findall('(?i)olanda', element[0]) or re.findall('(?i)olanda', element[1]):
        olanda += 1
    if re.findall('(?i)spania', element[0]) or re.findall('(?i)spania', element[1]):
        spania += 1
    if re.findall('(?i)grecia', element[0]) or re.findall('(?i)grecia', element[1]):
        grecia += 1


if germania:
    f.write(f"\nGermania: {str(germania)}")
if belgia:
    f.write(f"\nBelgia: {str(belgia)}")
if bulgaria:
    f.write(f"\nBulgaria: {str(bulgaria)}")
if franta:
    f.write(f"\nFranta: {str(franta)}")
if italia:
    f.write(f"\nItalia: {str(italia)}")
if anglia:
    f.write(f"\nAnglia: {str(anglia)}")
if danemarca:
    f.write(f"\nDanemarca: {str(danemarca)}")
if olanda:
    f.write(f"\nOlanda: {str(olanda)}")
if spania:
    f.write(f"\nSpania: {str(spania)}")
if grecia:
    f.write(f"\nGrecia: {str(grecia)}")

f.write(f"\n---------------------------")
f.write(f"\n2.Nivel studii:")

necalificat = calificat = student = absolvent = 0
# incepator

for element in lista_descriere:
    if re.findall('(?i)necalifica[tț]|incepator|.ncep.tor', element[0]) or re.findall('(?i)necalifica[tț]|incepator|.ncep.tor', element[1]):
        necalificat += 1

    if re.findall('(?i)\scalifica[tț][a-z]*', element[0]) or re.findall('(?i)\scalifica[tț][a-z]*', element[1]):      #ca sa nu ia din ne-calificat
        calificat += 1

    if re.findall('(?i)studen[tț][a-z]*', element[0]) or re.findall('(?i)studen[tț][a-z]*', element[1]):
        student += 1

    if re.findall('(?i)absolven[tț][a-z]*', element[0]) or re.findall('(?i)absolven[tț][a-z]*', element[1]):
        absolvent += 1

if necalificat:
    f.write(f"\nNecalificat: {str(necalificat)}")
if calificat:
    f.write(f"\nCalificat: {str(calificat)}")
if student:
    f.write(f"\nStudent: {str(student)}")
if absolvent:
    f.write(f"\nAbsolvent: {str(absolvent)}")


f.write(f"\n---------------------------")
f.write(f"\n3.Profesie:")

profesii=[]
contor=[]

for element in lista_descriere:
    #angajeaza
    if re.findall('(?i)(?<=angajeaza )\s*[a-zA-Z]+', element[0]) :
        if re.findall('(?i)(?<=angajeaza )\s*[a-zA-Z]+', element[0]) not in profesii:
            profesii.append(re.findall('(?i)(?<=angajeaza )\s*[a-zA-Z]+', element[0]))
    if re.findall('(?i)(?<=angajeaza )\s*[a-zA-Z]+', element[1]):
        if re.findall('(?i)(?<=angajeaza )\s*[a-zA-Z]+', element[1]) not in profesii:
            profesii.append(re.findall('(?i)(?<=angajeaza )\s*[a-zA-Z]+', element[1]))

    # angajeaza ceva1 si ceva2
    # regex pt ceva2:
    pattern = re.compile('angajeaza\s+[a-zA-Z]+\s+si\s+([a-zA-Z]+)', re.I)
    if re.findall(pattern, element[0]):
        if re.findall(pattern, element[0]) not in profesii:
            profesii.append(re.findall(pattern, element[0]))
    if re.findall(pattern, element[1]):
        if re.findall(pattern, element[1]) not in profesii:
            profesii.append(re.findall(pattern, element[1]))
    # ceva1/ceva2
    pattern = re.compile('angajeaza\s+[a-zA-Z]+\s*[/,]\s*([a-zA-Z]+)', re.I)
    if re.findall(pattern, element[0]):
        if re.findall(pattern, element[0]) not in profesii:
            profesii.append(re.findall(pattern, element[0]))
    if re.findall(pattern, element[1]):
        if re.findall(pattern, element[1]) not in profesii:
            profesii.append(re.findall(pattern, element[1]))

    #angajam
    if re.findall('(?i)(?<=angajam )\s*[a-zA-Z]+', element[0]) :
        if re.findall('(?i)(?<=angajam )\s*[a-zA-Z]+', element[0]) not in profesii:
            profesii.append(re.findall('(?i)(?<=angajam )\s*[a-zA-Z]+', element[0]))
    if re.findall('(?i)(?<=angajam )\s*[a-zA-Z]+', element[1]):
        if re.findall('(?i)(?<=angajam )\s*[a-zA-Z]+', element[1]) not in profesii:
            profesii.append(re.findall('(?i)(?<=angajam )\s*[a-zA-Z]+', element[1]))

    pattern = re.compile('angajam\s+[a-zA-Z]+\s+si\s+([a-zA-Z]+)', re.I)
    if re.findall(pattern, element[0]):
        if re.findall(pattern, element[0]) not in profesii:
            profesii.append(re.findall(pattern, element[0]))
    if re.findall(pattern, element[1]):
        if re.findall(pattern, element[1]) not in profesii:
            profesii.append(re.findall(pattern, element[1]))
    pattern = re.compile('angajam\s+[a-zA-Z]+\s*[/,]\s*([a-zA-Z]+)', re.I)
    if re.findall(pattern, element[0]):
        if re.findall(pattern, element[0]) not in profesii:
            profesii.append(re.findall(pattern, element[0]))
    if re.findall(pattern, element[1]):
        if re.findall(pattern, element[1]) not in profesii:
            profesii.append(re.findall(pattern, element[1]))

    # angajez
    if re.findall('(?i)(?<=angajez )\s*[a-zA-Z]+', element[0]):
        if re.findall('(?i)(?<=angajez )\s*[a-zA-Z]+', element[0]) not in profesii:
            profesii.append(re.findall('(?i)(?<=angajez )\s*[a-zA-Z]+', element[0]))
    if re.findall('(?i)(?<=angajez )\s*[a-zA-Z]+', element[1]):
        if re.findall('(?i)(?<=angajez )\s*[a-zA-Z]+', element[1]) not in profesii:
            profesii.append(re.findall('(?i)(?<=angajez )\s*[a-zA-Z]+', element[1]))

    pattern = re.compile('angajez\s+[a-zA-Z]+\s+si\s+([a-zA-Z]+)', re.I)
    if re.findall(pattern, element[0]):
        if re.findall(pattern, element[0]) not in profesii:
            profesii.append(re.findall(pattern, element[0]))
    if re.findall(pattern, element[1]):
        if re.findall(pattern, element[1]) not in profesii:
            profesii.append(re.findall(pattern, element[1]))
    pattern = re.compile('angajez\s+[a-zA-Z]+\s*[/,]\s*([a-zA-Z]+)', re.I)
    if re.findall(pattern, element[0]):
        if re.findall(pattern, element[0]) not in profesii:
            profesii.append(re.findall(pattern, element[0]))
    if re.findall(pattern, element[1]):
        if re.findall(pattern, element[1]) not in profesii:
            profesii.append(re.findall(pattern, element[1]))

    # cauta
    if re.findall('(?i)(?:(?<=caut )|(?<=caut[aă] )|(?<=c[aă]ut[aă]m ))\s*[a-zA-Z]+', element[0]):
        if re.findall('(?i)(?:(?<=caut )|(?<=caut[aă] )|(?<=c[aă]ut[aă]m ))\s*[a-zA-Z]+', element[0]) not in profesii:
            profesii.append(re.findall('(?i)(?:(?<=caut )|(?<=caut[aă] )|(?<=c[aă]ut[aă]m ))\s*[a-zA-Z]+', element[0]))
    if re.findall('(?i)(?:(?<=caut )|(?<=caut[aă] )|(?<=c[aă]ut[aă]m ))\s*[a-zA-Z]+', element[1]):
        if re.findall('(?i)(?:(?<=caut )|(?<=caut[aă] )|(?<=c[aă]ut[aă]m ))\s*[a-zA-Z]+', element[1]) not in profesii:
            profesii.append(re.findall('(?i)(?:(?<=caut )|(?<=caut[aă] )|(?<=c[aă]ut[aă]m ))\s*[a-zA-Z]+', element[1]))

    if re.findall('(?i)(?:(?<=caut aj )|(?<=caut[aă] aj )|(?<=c[aă]ut[aă]m aj ))\s*[a-zA-Z]+', element[0]):
        if re.findall('(?i)(?:(?<=caut aj )|(?<=caut[aă] aj )|(?<=c[aă]ut[aă]m aj ))\s*[a-zA-Z]+', element[0]) not in profesii:
            profesii.append(re.findall('(?i)(?:(?<=caut aj )|(?<=caut[aă] aj )|(?<=c[aă]ut[aă]m aj ))\s*[a-zA-Z]+', element[0]))
    if re.findall('(?i)(?:(?<=caut aj )|(?<=caut[aă] aj )|(?<=c[aă]ut[aă]m aj ))\s*[a-zA-Z]+', element[1]):
        if re.findall('(?i)(?:(?<=caut aj )|(?<=caut[aă] aj )|(?<=c[aă]ut[aă]m aj ))\s*[a-zA-Z]+',element[1]) not in profesii:
            profesii.append(re.findall('(?i)(?:(?<=caut aj )|(?<=caut[aă] aj )|(?<=c[aă]ut[aă]m aj ))\s*[a-zA-Z]+', element[1]))

    if re.findall('(?i)(?:(?<=caut ajutor )|(?<=caut[aă] ajutor )|(?<=c[aă]ut[aă]m ajutor ))\s*[a-zA-Z]+', element[0]):
        if re.findall('(?i)(?:(?<=caut ajutor )|(?<=caut[aă] ajutor )|(?<=c[aă]ut[aă]m ajutor ))\s*[a-zA-Z]+',element[0]) not in profesii:
            profesii.append(re.findall('(?i)(?:(?<=caut ajutor )|(?<=caut[aă] ajutor )|(?<=c[aă]ut[aă]m ajutor ))\s*[a-zA-Z]+', element[0]))
    if re.findall('(?i)(?:(?<=caut ajutor )|(?<=caut[aă] ajutor )|(?<=c[aă]ut[aă]m ajutor ))\s*[a-zA-Z]+', element[1]):
        if re.findall('(?i)(?:(?<=caut ajutor )|(?<=caut[aă] ajutor )|(?<=c[aă]ut[aă]m ajutor ))\s*[a-zA-Z]+',element[1]) not in profesii:
            profesii.append(re.findall('(?i)(?:(?<=caut ajutor )|(?<=caut[aă] ajutor )|(?<=c[aă]ut[aă]m ajutor ))\s*[a-zA-Z]+', element[1]))

    pattern = re.compile('cauta\s+[a-zA-Z]+\s+si\s+([a-zA-Z]+)', re.I)
    if re.findall(pattern, element[0]):
        if re.findall(pattern, element[0]) not in profesii:
            profesii.append(re.findall(pattern, element[0]))
    if re.findall(pattern, element[1]):
        if re.findall(pattern, element[1]) not in profesii:
            profesii.append(re.findall(pattern, element[1]))
    pattern = re.compile('cauta\s+[a-zA-Z]+\s*[/,]\s*([a-zA-Z]+)', re.I)
    if re.findall(pattern, element[0]):
        if re.findall(pattern, element[0]) not in profesii:
            profesii.append(re.findall(pattern, element[0]))
    if re.findall(pattern, element[1]):
        if re.findall(pattern, element[1]) not in profesii:
            profesii.append(re.findall(pattern, element[1]))

#varianita cu aj/ajutor si la regexurile de mai sus
# sau (|) in expresiile cu compile in lookbehind

f.write(f"{profesii}")

# contorizare profesii








f.write(f"\n---------------------------")
f.write(f"\n4.Tip contract:")

determinata = nedeterminata = colaborare = internship = 0

for element in lista_descriere:
    if re.findall('(?i)nedeterminat[aă]', element[0]) or re.findall('(?i)nedeterminat[aă]', element[1]):
        nedeterminata += 1

    if re.findall('(?i)\sdeterminat[aă]', element[0]) or re.findall('(?i)\sdeterminat[aă]', element[1]):
        determinata += 1

    if re.findall('(?i)colaborare', element[0]) or re.findall('(?i)colaborare', element[1]):
        colaborare += 1

    if re.findall('(?i)internship', element[0]) or re.findall('(?i)internship', element[1]):
        internship += 1

f.write(f"\nPerioada nedeterminata: {nedeterminata}")
f.write(f"\nPerioada determinata: {determinata}")
f.write(f"\nColaborare: {colaborare}")
f.write(f"\nInternship: {internship}")


f.write(f"\n---------------------------")
f.write(f"'\n5.Program:")

full_time = part_time = flexibil = peste = 0

for element in lista_descriere:
    if re.findall('(?i)full time|fulltime|full_time|full-time|8\s*h|8\s*ore', element[0]) or re.findall('(?i)full time|fulltime|full_time|full-time|8\s*h|8\s*ore', element[1]):
        full_time += 1

    if re.findall('(?i)part time|part_time|part-time|parttime|4\s*h|4\s*ore', element[0]) or re.findall('(?i)part time|part_time|part-time|parttime|4\s*h|4\s*ore', element[1]):
        part_time += 1

    if re.findall('(?i)flexibil', element[0]) or re.findall('(?i)flexibil', element[1]):
        flexibil += 1

    if re.findall('(?i)9\s*h|9\s*ore|[0-8]{2}\s*h|[0-8]{2}\s*ore', element[0]) or re.findall('(?i)9\s*h|9\s*ore|[0-8]{2}\s*h|[0-8]{2}\s*ore', element[1]):
        peste += 1


f.write(f"\nFull-time: {full_time}")
f.write(f"\nPart-time: {part_time}")
f.write(f"\nFlexibil: {flexibil}")
f.write(f"\n>8h: {peste}")
# sys.stdout.flush()

