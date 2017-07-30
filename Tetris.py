import tkinter as tk
import logika

VELIKOST_POLJA = 10
ODMIK = 5

class Tetris:

	def __init__(self, okno):
		self.igra = logika.a
		self.okno = okno
		self.igralna_plosca = tk.Canvas(
			width=VELIKOST_POLJA * self.igra.sirina + 2 * ODMIK,
			height=VELIKOST_POLJA * self.igra.dolzina + 2 * ODMIK)
		self.igralna_plosca.pack()
		self.okno.bind('<Key>', self.pomen_tipke)
		self.hitrost = 5
		self.korak()



	def korak(self):
		self.igra.blok.premakni_dol()
		self.osvezi_prikaz()
		self.okno.after(int(1000 // self.hitrost), self.korak)
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
		pass
			


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




		

okno = tk.Tk()
moj_program = Tetris(okno)
okno.mainloop()