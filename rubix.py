from random import *
class rubiccube(object): # Klasse zum definieren und loesen eines Rubixcubes
    def __init__(self): # Definition der Groessen des Wuerfels        
        self.size=3
        self.cube= []# [[[Koordinate],[Typ],[Farben]],[Wuerfel2]]
        self.ecken=[1,3,7,9,19,21,25,27]
        self.mitte=[5,11,13,15,17,23]
        self.kanten=[]
        self.obenschicht=[1,2,3,10,11,12,19,20,21]
        self.untenschicht=[7,8,9,16,17,18,25,26,27]
        self.rechtsschicht=[3,6,9,12,15,18,21,24,27]
        self.linksschicht=[1,4,7,10,13,16,19,22,25]
        for x in range(1,27):
            if x%2==0 and x != 14: #Kanten an allen geraden Teilwuerfeln ausser dem Mittelpunkt.
                self.kanten.append(x)
        self.mittelpunkt=14
        self.oben="gelb"#oben
        self.links="rot"#links
        self.vorne="blau"#vorne
        self.rechts="lila"#rechts
        self.unten="gruen"#unten
        self.hinten="pink"#hinten
        self.farben={self.vorne, self.oben, self.links, self.rechts, self.unten, self.hinten}#Farben den jeweilgen Mitten zugeordnet
        self.farbe={self.oben,self.vorne, self.links, self.hinten, self.rechts, self.unten}#Farben sortiert
    def erstellen(self): # erstellen des Wuerfels in geloestem Zustand
        self.cube=[]
        for z in range (self.size): #In die Tiefe gehen
            for y in range (self.size): #In die Hoehe gehen
                for x in range(self.size): # In die Breite gehen
                    self.cube.append([[x,y,z]]) #Koordinaten der einzelnen 27 Teilwuerfel erstellen
                    if not (z==1 and y==1 and x==1):
                        self.cube[self.cube.index([[x,y,z]])].extend(self.faerben([x,y,z]))#Den Koordinaten Art und Farben zuordnen
    def faerben(self,position): #Den Typ einer Koordinate und dessen Farben ausfindig machen. Ausgabe: Typ, Farben
        oben=""
        links=""
        rechts=""
        typ=""
        platz=self.cube.index([position])+1#An wievielter Stelle steht die Koordinate (index)
        if platz in self.ecken:#Zuordnen des Types des Teilwuerfels zu den Positionen der oben definierten Plaetze
           typ="ecke"
        elif platz in self.kanten:
           typ="kante"
        elif platz in self.mitte:
           typ = "mitte"
        else:
           print("Angegebene Koordinate ungültig. Fehler in farben(). Koordinate aus erstellen()")# Fehlerausgabe
        """ecke=[oben,links,rechts]#Schematische Darstellung der jeweiligen Twilwuerfel
        kante=[oben,links]
        mitte=[oben]"""
        if position[1]==0:#Zuordnen der jeweiligen Farben je nach Position
                oben=self.oben
        elif position[1]==2:
                oben=self.unten
        if typ == "mitte":
                return([typ],[self.farben[self.mitte.index(platz)]])
        elif typ=="ecke":
            if platz == 1 or platz == 5:
                links=self.links
                rechts=self.vorne
            elif platz== 2 or platz == 6:
                links=self.vorne
                rechts=self.rechts
            elif platz == 3 or platz == 7:
                links=self.hinten
                rechts = self.links
            elif platz == 4 or platz == 8:
                links = self.rechts
                rechts= self.hinten 
            return ([typ],[oben,links,rechts])
        elif typ=="kante":
            if platz == 2 or platz == 8:
                links= self.vorne
            elif platz == 12 or platz == 18:
                links=self.rechts
            elif platz == 20 or platz == 26:
                links=self.hinten
            elif platz == 10 or platz == 16:
                links=self.links
            elif platz == 4:
                oben= self.links
                links=self.vorne
            elif platz== 6:
                oben=self.vorne
                links=self.rechts
            elif platz==22:
                oben=self.hinten
                links = self.links
            elif platz==24:
                oben = self.rechts
                links= self.hinten 
            return [[typ],[oben,links]]
        else:
            print("Fehler in self.farben(",typ,platz,position,")")#Fehlerausgabe

    def drehen(self,seite,richtung):#Drehen einer Schicht des Wuerfels
        
        #seite: oben:1, unten:2  -  rechts:3, links:4
        #richtung: rechts:1,  links:2   -   oben:3, unten:4
        #alle in Wuerfel tauschen um:
        #-rechts 1-7, 2-4, 3-1, 4-8, 5-5, 6-2, 7-9, 8-6, 9-3
        #- links = rechts rueckwaerts
        #- oben= rechts
        #- unten = links

        if seite==1:
            werte=self.obenschicht
        elif seite==2:
            werte=self.untenschicht
        elif seite==3:
            werte=self.rechtsschicht
        else:
            werte=self.linksschicht

        if richtung==1 or richtung==3:
            self.rechtstausch(werte)
        else:
            self.linkstausch(werte)

    def rechtstausch(self, werte):#Tauschen der Werte bei Rechtsdrehung
        ergebnis=[0,1,2,3,4,5,6,7,8,9]
        werte.insert(0,0)
        ergebnis[7]=werte[1]#Tauschschema angeben
        ergebnis[4]=werte[2]
        ergebnis[1]=werte[3]
        ergebnis[8]=werte[4]
        ergebnis[5]=werte[5]
        ergebnis[2]=werte[6]
        ergebnis[9]=werte[7]
        ergebnis[6]=werte[8]
        ergebnis[3]=werte[9]
        ergebnis.pop(0)
        for x in range(len(werte)):#Werte austauschen
            werte[x]= self.cube[werte[x]-1][2]
        self.aendern(ergebnis,werte)
        return self.cube[ergebnis]
    def linkstausch(self, werte):#Tauschen der Werte bei Linksdrehung
        ergebnis=[0,1,2,3,4,5,6,7,8,9]
        werte.insert(0,0)
        ergebnis[1]=werte[7]#Tauschschema angeben
        ergebnis[2]=werte[4]
        ergebnis[3]=werte[1]
        ergebnis[4]=werte[8]
        ergebnis[5]=werte[5]
        ergebnis[6]=werte[2]
        ergebnis[7]=werte[9]
        ergebnis[8]=werte[6]
        ergebnis[9]=werte[3]
        ergebnis.pop(0)
        for x in range(len(werte)):#Werte tauschen
            werte[x]= self.cube[werte[x]-1][2]
        self.aendern(ergebnis,werte)
        return self.cube[ergebnis]
    def verschieben(self,richtung):
        #Drehen des gesamten Wuerfels: 1-oben, 2-unten, 3-rechts, 4-links
        if richtung==1 or richtung ==2:
            mittenicht.extend(self.linksschicht+self.rechtsschicht)#obere und untere Schicht ermitteln
            for x in range(1,27):#obere und untere Schicht vom gesamten Wuerfel abziehen -> Mitte
                if x not in mittenicht:
                    mitte.append(x)
            if richtung ==1:
                self.rechtstausch(mitte)
                self.drehen(3,1)
                self.drehen(4,1)
            elif richtung==2:
                self.linkstausch(mitte)
                self.drehen(3,2)
                self.drehen(4,2)
        else:
            mittenicht.extend(self.obenschicht+self.untenschicht)#obere und untere Schicht ermitteln

        for x in range(1,27):#obere und untere Schicht vom gesamten Wuerfel abziehen -> Mitte
                if x not in mittenicht:
                    mitte.append(x)
        if richtung==3:
            self.rechtstausch(mitte)
            self.drehen(1,1)
            self.drehen(2,1)
        elif richtung==4:
            self.linkstausch(mitte)
            self.drehen(1,2)
            self.drehen(2,2)

    def loesen(self): #loesen der aktuellen Stellung
       start=self.cube#Konstellation speichern
       self.erstellen
       ziel=self.cube#Zielkonstellation erstellen
       self.suche(self.unten,self.kanten,1)#Schritt 1: Kreuz auf Boden erstellen
       self.suche(self.unten,self.ecken,2)#Schritt 2: Ts an der Seite erstellen
       for x in range(2,5):
           self.suche(self.farben[x],self.kanten,3)#Schritt3: 6er Bloecke erstellen
       self.suche(self.oben,self.kanten,4)#Schritt 4: Kreuz auf Decke erstellen
       self.suche(self.oben,self.kanten,5)#Schritt 5: Kreuz oben ausrichten
       self.suche(self.oben,self.ecken,6)#Schritt 6: Ecken richtig positionieren
       self.suche(self.oben,self.ecken,7)#Schritt 7: Ecken richtig ausrichten

    def suche(self,position,typ,schritt):#Zielposition ermitteln
        for x in range (len(start)):
           if position in start[x][2] and x+1 in typ:#Farben  und Typ pruefen
               for y in range(len(ziel)):
                   if ziel[y][2]==start[x][2]:#Zielposition ermitteln
                       zielp=y
                       self.bewege(schritt,start[x],ziel[zielp])
                       break

    def bewege(self,schritt,start,ziel):#Wuerfel von start zu ziel Position verschieben, je nach Schritt
        #seite: oben:1, unten:2  
        #-      rechts:3, links:4
        #richtung: rechts:1,4):2   oben:1, unten:2  
        #-                         rechts:3, links:4
        #-      oben:3, unten:4
        #start= self.cube.index(start)=[Teilwuerfel]

        if schritt==1:#Unten das Kreuz machen

            #self.drehen(bis wuerfel ueber ziel)
            #self.unten: unetn,links,rechts?
            #oben -> 
            dif = ziel[0]
            for x in range (3):
                dif[x]-=start[0][x]
            if dif[0]+dif[1]+dif[2]!=0:
                if dif[2]==0:
                    pos=True #Ecke unten
                else:
                    pos=False # Ecke oben
                if pos:#Ecke nach oben verschieben
                    start=self.bewegung(1)
                if self.betrag(dif[0])==self.betrag(dif[1]) and dif[0]!=0:#Von Ecke zur Ecke diagonal gegenueber
                    self.drehen(1,3)
                    self.drehen(1,3)
                elif dif[0]==0:
                    self.drehen(1,4)
                if start[0][1]==?:#vorne
                    if dif[0]==0 and dif[1]==3 or dif[0]==3 and dif[1]==0:
                        self.drehen(1,4)
                    elif dif[0]==-3 and dif[1]==0 or dif[0]==0 and dif[1]==1:
                        pass
                else:
                    self.drehen(1,1)

                """else:
                vornelinks
                0,1 links
                1,0 rechts
                vornerechts
                -1,0 links
                0,1 rechts
                hintenrechts
                -1,0 rechts
                0,-1 links
                hintenlinks
                1,0 links
                0,-1 rechts"""

             

            if self.cube[self.cube.index(start)][2][0]==self.unten:

                self.drehen(3,1)
                self.drehen(1,4)
                self.drehen(3,2)
                self.drehen(3,1)
                self.drehen(1,4)
                self.drehen()
            elif self.cube[self.cube.index(start)][2][1]==self.unten:
                pass
            else:
                pass
        elif schritt==2:#Unten die Ecken machen/Ts an der Seite
            if self.unten==ziel[2][2]:
                self.bewegung(1)
            
            elif self.unten==ziel[2][0]:
                self.drehen(3,1)
                self.drehen(1,4)
                self.drehen(1,4)
                self.drehen(3,2)
                self.drehen(1,3)
                self.bewegung(1)

            elif self.unten==ziel[2][1]:
                self.drehen(1,4)
                self.drehen(3,1)
                self.drehen(1,3)
                self.drehen(3,2)

        elif schritt==3:#kanten mitte fuellen:
            #zu weit gedreht self.drehen(1,3)
            if start[0][2]==0 and start[2][0]==ziel[2][0]:
                #bedingung:  position oben und farbe oben gleich farbe der mitte auf der seite gegenueber
                #wenn ziel links von start:
                if start[0][1]==2:
                    #blickwinkel: zielposition farbe rechts
                    while self.vorne!= ziel[2][2]:
                        self.verschieben(3)

                    self.drehen(4,1)
                    self.drehen(1,3)
                    self.drehen(4,2)
                    self.drehen(1,4)
                    self.verschieben(3)
                    self.bewegung(1)

            #wenn ziel rechts von start:
                if start[0][1]==3:
                    #blickwinkel: zielposition farbe links
                    while self.vorne!= ziel[2][1]:
                        self.verschieben(4)

                    self.bewegung(1)
                    self.drehen(1,3)
                    self.verschieben(4)
                    self.drehen(4,1)
                    self.drehen(1,3)
                    self.drehen(4,2)

        elif schritt==4:#Oben Kreuz machen, Eingabe 4 Kanten
            richtig=[]
            for x in start:
                if x[2][0]==self.oben:
                    richtig.append(1)
                else:
                    richtig.append(0)
                if sum(richtig,0)==4:
                    return "fertig"

            if sum(richtig,0)>1:#wenn oben nicht nichts:

                if richtig[0]==richtig[2] or richtig[1]==richtig[3] or sum(richtig,0)==3: #Wenn oben gerade
                    #blickwinkel: eine Kante links, andere rechts und self.rechts=rechts(links), unten=self.oben 
                    if richtig[0]==1:
                        while self.links!= start[0][2][1] or self.rechts!= start[0][2][1]:
                            self.verschieben(3)
                    elif richtig[1]==1:
                        while self.links!= start[1][2][1] or self.rechts!= start[1][2][1]:
                            self.verschieben(3)

                    dauer="1"

                else:#oben 3/5 Kreuz
                    dauer="2"
                    for x in range(2):
                        if richtig[x]==1 and richtig[x+1]==1:
                            while start[x][2][1]!=self.links:#blickwinkel: oben: kante links und oben: self.hinten= oben(links), uunten= self.oben
                                self.verschieben(3)
                            break
                    if richtig[3]==1 and richtig[0]==1:
                        while start[3][2][1]!=self.links:#blickwinkel: oben: kante links und oben: self.hinten= oben(links), uunten= self.oben
                            self.verschieben(3)
                    
            else: #oben nichts
                dauer="1n" 
            self.verschieben(1)
            self.drehen(2,3)
            self.verschieben(2)
            for x in range(int(dauer[0])):
                self.drehen(3,1)
                self.drehen(1,4)
                self.drehen(3,2)
            self.verschieben(1)
            self.drehen(2,4)
            self.verschieben(2)
            if dauer[1]=="n":
                self.bewege(schritt,start,ziel)
        elif schritt==5:#Oben Kreuz ausrichten, Eingabe: 4 kanten im Uhrzeigersinn beginnend mit vorne
            richtig=[]
            
            
            for x in start:
                if x[2][1]==self.farbe[x+1]:
                    richtig.append(1)
                else:
                    richtig.append(0)
            if sum(richtig,0)==0 or sum(richtig,0)==4:
                while sum(richtig,0)!=4:
                     self.verschieben(3)
                return "fertig"
            for x in range(3):
                        if richtig[x]==1 and richtig[x+1]==1:#2 kanten nebeneinander richtig:
                            while sum(richtig,0)!=1: #oben rechts drehen bis genau eine kante richtig
                                self.verschieben(3)
                        self.bewege(schritt, start, ziel)
            if richtig[0]==richtig[2] or richtig[1]==richtig[3] or sum(richtig,0)==3: #Wenn oben gerade 2x
                    #blickwinkel: eine Kante links, andere rechts und self.rechts=rechts(links), unten=self.oben 
                    if richtig[0]==1:
                        while self.links!= start[1][2][1] or self.rechts!= start[1][2][1]:#Gerade vom Betrachter weg ausrichtien
                            self.verschieben(3)
                    elif richtig[1]==1:
                        while self.links!= start[3][2][1] or self.rechts!= start[3][2][1]:#Gerade vom Betrachter weg ausrichtien
                            self.verschieben(3)
                    dauer="2"
            else:
                dauer="1"#genau eine Kante richtig 1x:

            for x in range (dauer):

            
                if start[0]==ziel[1]:#andere kanten nach rechts drehen: (oben uhrzeigersinn)
                    self.drehen(3,1)
                    self.drehen(1,4)
                    self.drehen(1,4)
                    self.drehen(3,2)
                    self.drehen(1,3)
                    self.drehen(3,1)
                    self.drehen(1,3)
                    self.drehen(3,2)
            
                if start[1]==ziel[0]:#andere kanten nach links drehen: (oben entgegen dem uhrzeigersinn)
                    self.drehen(3,1)
                    self.drehen(1,4)
                    self.drehen(3,2)
                    self.drehen(1,4)
                    self.drehen(3,1)
                    self.drehen(1,4)
                    self.drehen(1,4)
                    self.drehen(3,2)



        elif schritt==6:#Oben Ecken richtig anordnen


            eine ecke mit richtigen farben suchen:
                wenn nicht(1x) und dann nochmal suchen
            blickwinkel: vorne: richtige ecke nach rechts oben
            if start[x][2]in ziel[y][2]:

            self.drehen(1,4)
            self.drehen(3,1)
            self.drehen(1,3)
            self.drehen(4,1)
            self.drehen(1,4)
            self.drehen(3,2)
            self.drehen(1,3)
            self.drehen(4,2)

          
        elif schritt==7:#Oben Ecken richtig ausrichten
            richtige ecke suchen(wenn keine dann oben rechts)
            blickwinkel: oben=oben: richtige ecke unten rechts

            bis wuerfel fertig:
                solange ecke oben rechts richtig:
                vorne nach rechts drehen dass ecke unten rechts ist

                bis ecke oben rechts richtig ist:
                    self.drehen(1,4)
                    self.drehen(3,2)
                    self.drehen(1,3)
                    self.drehen(3,1)
                    wenn richtig break















    def bewegung(self,nummer):
        if nummer ==1:
             self.drehen(3,1)
             self.drehen(1,4)
             x=self.drehen(3,2)
             return x

    def betrag(self, wert):
        if wert==0:
            return 0
        wert=(wert*wert)**(1/2)
        return wert
    def mischen(self):#Zufaelliges verdrehen des Wuerfels
        self.steps=[]
        for x in range(20):#20 mal verdrehen
            seite=randint(1,2)#zufaellig welche seite/richtung
            richtung=randint(1,2)
            self.drehen(seite,richtung)
            self.steps.append(seite,richtung)#Speichern der gemachten Zuege

    def eingabe(self,farben,punkte):#Eingabe einer bestimmten Konstellation des Wuerfels
        self.oben=farben[0]#oben
        self.links=farben[1]#links
        self.vorne=farben[2]#vorne
        self.rechts=farben[3]#rechts
        self.unten=farben[4]#unten
        self.hinten=farben[5]#hinten
        self.aendern(indizes,farben)

    def aendern(self,index,farbe):#Aktualisieren der jeweiligen Teilwuerfel
        for x in range(len(index)):
            if x !=13:
                self.cube[index[x]-1][2]=farbe[x]

rubic= rubiccube() # Objekt rubic bzw. Rubixcube erschaffen
rubic.erstellen() #Rubixcube erschaffen
