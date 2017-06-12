import random

koncnice = {"♣️" : "kr", "♥️" : "sr", "♠️" : "pi", "♦️" : "ka"}

def nov_kup_kart():
    kup = []
    for barva in ["♣️", "♥️", "♠️", "♦️"]:
        for i in range(2,15):
            kup += [Karta(i, barva)]
    random.shuffle(kup)
    return kup

def razdeli():
    x = nov_kup_kart()
    n = len(x)//2 + 1
    return [x[:n] , x[n:]]

class Karta:
    def __init__(self, vrednost, barva):
        self.vrednost = vrednost
        self.barva = barva

    def __lt__(self, other):
        if self.vrednost < other.vrednost:
            return True
        elif self.vrednost > other.vrednost:
            return False
        elif self.vrednost == self.vrednost:
            return None

    def __repr__(self):
        return 'Karta({},{})'.format(self.vrednost, self.barva)

class Igra:
    def __init__(self):
        pass
    def pozeni(self):
        self.a, self.b = razdeli()
        self.i = 0
        self.tvoj_rezultat = 0
        self.nasprotnikov_rezultat = 0


        for k1, k2 in zip(self.a, self.b):
            print('Tvoja karta je ', k1)
            print('Nasprotnikova karta je ', k2)

            if k1 > k2:
                self.tvoj_rezultat += 1

                with open('datoteka.txt','w') as datoteka:
                    print(self.tvoj_rezultat, self.nasprotnikov_rezultat, file = datoteka)

                
            else:
                self.nasprotnikov_rezultat += 1
                with open('datoteka.txt','w') as datoteka:
                    print(self.tvoj_rezultat, self.nasprotnikov_rezultat, file = datoteka)

            print('Tvoje število točk je ', self.tvoj_rezultat, '.')

                

            
        if self.tvoj_rezultat > self.nasprotnikov_rezultat:
            print('Ti si zmagovalec')


        elif self.tvoj_rezultat == self.nasprotnikov_rezultat:
            print('Rezultat je izenačen')


        else:
            print('Ti si poraženec')
















        
        
    
    
    
        
        


    







    
    
    

        
        
        
        
        

        
        
        
