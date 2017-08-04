import tkinter as tk
import logika
#import pyglet

#music = pyglet.resource.media('Complete History Of The Soviet Union, Arranged To The Melody Of Tetris.mp3')
#music.play()
#pyglet.app.run()


VELIKOST_POLJA = 10
ODMIK = 5
ZACETNA_HITROST = 2
KONCNA_HITROST = 1000

class Tetris:

	def __init__(self, okno):
		self.igra = logika.instance
		self.okno = okno
		self.igralna_plosca = tk.Canvas(
			width=VELIKOST_POLJA * self.igra.sirina + 2 * ODMIK,
			height=VELIKOST_POLJA * self.igra.dolzina + 2 * ODMIK)
		self.igralna_plosca.grid(row = 0, column = 0)	
		self.okno.bind('<Key>', self.pomen_tipke)
		prikaz = tk.Frame(self.okno)
		prikaz.grid(row = 1, column = 0)
		self.prikaz_tock = tk.Label(prikaz)
		self.korak()
		self.prikaz_tock.pack()



	def korak(self):
		self.postopoma_povecjaj_hitrost()
		self.igra.blok.premakni_dol()
		self.osvezi_prikaz()
		self.okno.after(int(1000 // self.hitrost), self.korak)
		print(self.hitrost)
		self.igra.blok_v_tla()
		self.igra.odstrani()

	def pomen_tipke(self, event):
		if event.keysym == 'Right':
			self.igra.blok.premakni_vodoravno(logika.DESNO)
			self.osvezi_prikaz()
		elif event.keysym == 'Left':
			self.igra.blok.premakni_vodoravno(logika.LEVO)
			self.osvezi_prikaz()
		elif event.keysym == 'Up':
			self.igra.blok.rotiraj()
			self.osvezi_prikaz()


	def postopoma_povecjaj_hitrost(self):
		self.hitrost = ((self.igra.score/100) ** (3/2)) + ZACETNA_HITROST
			


	def osvezi_prikaz(self):
		self.igralna_plosca.delete('all')
		self.igralna_plosca.create_rectangle(
			ODMIK,
			ODMIK,
			int(self.igralna_plosca['width']) - ODMIK,
			int(self.igralna_plosca['height']) - ODMIK)
		for x, y in self.igra.blok.tocke:
			self.igralna_plosca.create_rectangle(
				ODMIK + VELIKOST_POLJA * x,
				ODMIK + VELIKOST_POLJA * y,
				ODMIK + VELIKOST_POLJA * x + VELIKOST_POLJA,
				ODMIK + VELIKOST_POLJA * y + VELIKOST_POLJA)
		for x, y in self.igra.povrsina:
			self.igralna_plosca.create_rectangle(
				ODMIK + VELIKOST_POLJA * x,
				ODMIK + VELIKOST_POLJA * y,
				ODMIK + VELIKOST_POLJA * x + VELIKOST_POLJA,
				ODMIK + VELIKOST_POLJA * y + VELIKOST_POLJA, fill='black')
		self.prikaz_tock['text'] = str(self.igra.score)







		

okno = tk.Tk()
moj_program = Tetris(okno)
okno.mainloop()