#In verband met de huiswerkopgave van les 7. In punt 3 van les 7 moet je het dictionary-element aardbei kiezen, niet vanille (in de opgave staat het fout).

prijzen={
    "aardbei": "3",
    "vanille": "4",
    "chocolade": "5",
}

Aanbieding = int(prijzen["aardbei"])*0.8
reclame_tekst = f"Vandaag in de aanbieding: aardbei-ijs, 1 liter - slechts € {Aanbieding}"
reclame_tekst2 = reclame_tekst[:63]
reclame_tekst3 = reclame_tekst2.upper()
reclame_tekst4 = reclame_tekst3.split(" ")

for el in reclame_tekst4:
    if len(el)<4:
        print(el.lower())
    else:
        print(el)
