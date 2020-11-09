lön = 0.01 #Startlön
ggr = 0 #antal gånger man dubblar sin lön
dag = 1 #Antal dagar man ökat sin lön
tot = 0 #vad man tjänat ihop totalt

print ('dag 0 har man 0 kr') #skriver att man har 0 kr när man börjar

while tot < 10000000: #en whileloop
    print(f'dag {dag:.0f} har man totalt fått {lön:.2f} kr') #Skriver vilken had det är och hur mycket lön man får den dagen
    tot = tot + lön #plussar de sparade pengarna med din nya löninkomsten
    lön = lön + lön #Uttryck för tt dubbla din löninkomst varje dag
    ggr = ggr + 1 #visar hur många gånger man har fått lön
    dag = dag + 1 #lägger till en dag varje gång loopen görs ett varv
    print (f'Totalt tjänat {tot:.2f} kr') #skriver ut hur mycket man tjänat totalt

print(f'{ggr} dagar till {tot} kr sparade pengar') #skriver antal dagar det tog att spara ihop 10 miljoner.
#