import model
import tkinter as tk
import os




class Prikaz:
    SIRINA_PLOSCE=2000
    VISINA_PLOSCE=2000
    
    def __init__(self, okno):
        self.zgoraj = tk.Frame(okno)
        self.zgoraj.pack()
        self.napis1 = tk.Label(self.zgoraj,text = '')
        self.napis1.pack()
        self.napis2 = tk.Label(self.zgoraj,text= '')
        self.napis2.pack()

        self.spodaj = tk.Frame(okno)
        self.spodaj.pack()

        self.sredina = tk.Frame(okno)
        self.sredina.pack()

        tk.Button(self.spodaj, text = 'Začni', command=self.zacni_igro).pack()

        self.platno = tk.Canvas(self.sredina, width=Prikaz.SIRINA_PLOSCE, height=Prikaz.VISINA_PLOSCE)
        self.platno.pack()

        self.slike = self.slike_kart()

        self.igra = model.Igra()

    def slike_kart(self):
        slike = dict()
        koncnice = {"♣️" : "kr", "♥️" : "sr", "♠️" : "pi", "♦️" : "ka"}
        for barva in koncnice:
            for vrednost in range(2,15):
                datoteka = os.path.join(os.path.dirname(__file__), 'karte', r"{}{}.gif".format(vrednost, koncnice[barva]))
                slike[(vrednost, barva)] = tk.PhotoImage(file=datoteka)
        return slike

    def narisi_karto(self, x, y, karta):
        self.platno.create_image(x, y, image=self.slike[(karta.vrednost, karta.barva)])

    def poteza(self):
        k1 = self.igra.a[self.igra.i]
        k2 = self.igra.b[self.igra.i]
        self.igra.i +=1
        self.narisi_karto(300,370,k1)
        self.narisi_karto(1100,370,k2)
        if self.igra.i < min(len(self.igra.a),len(self.igra.b)):
            self.platno.after(1000,self.poteza)
        else:
            self.napis1.config(text = 'Tvoj rezultat je ' + str(self.igra.tvoj_rezultat))

            self.napis2.config(text = 'Nasprotnikov rezultat je ' + str(self.igra.nasprotnikov_rezultat))

                
        
    def zacni_igro(self):
        self.igra.pozeni()
        self.poteza()




        
    
        


okno = tk.Tk()
karte = Prikaz(okno)

okno.mainloop()
