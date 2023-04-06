from algemene_functies import mijn_functie_2

def aanbieding_1(smaak,prijs,korting):
    smaak_1 = smaak
    prijs_1 = prijs
    korting_1 = prijs * (1-korting)
    print(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak_1}, van {prijs_1} voor {korting_1}.")

aanbieding_1("aardbei",4,0.1)

def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    bedrag = totaal * btw
    print(f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden.")

inkomsten_totaal([220, 430, 125, 160, 205, 90, 345],0.09)
    
def laag_en_hoog(mijn_lijst):
    print([max(mijn_lijst),min(mijn_lijst)])

laag_en_hoog([220, 430, 125, 160, 205, 90, 345])

def gemiddelde(mijn_lijst):
    lengte = len(mijn_lijst)
    totaal = sum(mijn_lijst)
    bedrag = totaal / lengte
    print(f"De gemiddelde inkomsten deze week zijn {bedrag} euro.")

gemiddelde([220, 430, 125, 160, 205, 90, 345])

def meervoudig(invoer_lijst):
    lijst = laag_en_hoog(invoer_lijst)
    
meervoudig([10,5,3,2,1,2,9])

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer