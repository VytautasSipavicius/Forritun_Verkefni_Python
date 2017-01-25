#25.01.2017
#Vytautas Sipavicius
#Lausn við Git verkefni

#Dæmi 1
#Búa til tvær breytur sem taka inn tölur frá notenda
tala1_1 = int(input("Sláðu inn tölu "))
tala1_2 = int(input("Sláðu inn aðra tölu "))
#Reikna og prenta út margfeldi og summu talnanna
print("Summa talnnan er:", tala1_1 + tala1_2)
print("Margfeldi talnnan er:", tala1_1 * tala1_2)

#Dæmi 2
#Búa til tvær breytur sem taka inn fornafn og eftirnafn
fornafn = input("Sláðu inn Fornafnið þitt ")
efirnafn = input("Sláðu inn Eftirnafnið þitt ")
#prenta út nafnið með halló
print("Halló",fornafn, efirnafn)

#Dæmi 3
#Búa til breytu fyrir þar sem notandinn slær inn texta
texti = input("Sláðu inn texta ")
#Búa til 3 breytur sem munu telja
hastafur = 0
lagstafur = 0
lageftirha = 0
#For lykkja sem keyrir í gegnum allan strenginn
for stak in range(len(texti)):
    #Tjekka hvort Stakið sé stafur og ef svo hækka lagstafur um 1
    if texti[stak].isalpha():
        lagstafur = lagstafur + 1
        #Tjekka hvort stafurinn sé hástafur og ef svo þá lækka lagstafur um 1 og hækka hastafur um 1
        if texti[stak].isupper():
            lagstafur = lagstafur - 1
            hastafur = hastafur + 1
            #tjekka hvort við séum ekki kominn í síðasta stakið í strengnum
            if stak != (len(texti) - 1):
                #tjekka hvort næsta stak sé lítill stafur og ef svo hækka teljarann fyrir það um 1
                if texti[stak + 1].islower():
                    lageftirha = lageftirha + 1
#Prenta allt út með texta
print("Í þessum texta eru",hastafur,"hástafir",lagstafur,"lágstafir og",lageftirha, "lágstafir koma strax á eftir hástaf")
