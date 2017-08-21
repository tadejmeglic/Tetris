import tkinter as tk
import logika
import sys
import os
import datetime
import winsound
#import pyglet

#music = pyglet.resource.media('Complete History Of The Soviet Union, Arranged To The Melody Of Tetris.mp3')
#music.play()
#pyglet.app.run()


VELIKOST_POLJA = 10
ODMIK = 5

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
		self.prikaz_tock.pack()
		self.prikaz_naslednjega_bloka = tk.Canvas(width=50, height=50)
		self.prikaz_naslednjega_bloka.grid(row = 0, column = 1)
		winsound.PlaySound('Complete_History_Of_The_Soviet_Union_Arranged_To_T.wav', winsound.SND_ALIAS | winsound.SND_ASYNC | winsound.SND_LOOP)
		self.korak()
		



	def korak(self):
		self.igra.postopoma_povecjaj_hitrost()
		self.igra.blok.premakni_dol()
		self.igra.blok_v_tla()
		self.igra.odstrani()
		self.osvezi_prikaz()
		if self.igra.konec_igre() == None:
			self.okno.after(int(1000 // self.igra.hitrost), self.korak)
		if self.igra.konec_igre() == True:
			with open('Scoreboard.txt', 'a') as dat:
				dat.write(str(self.igra.score) + '          ' +  str(datetime.datetime.now()) + '\n')
			self.igra_koncana()

	def igra_koncana(self):
		self.popup = tk.Toplevel()
		self.popup.title("Bo drugič boljše!")
		okvir_popup = tk.Label(self.popup, text='Tvoje število točk je: ' + str(self.igra.score) + ', a si vseeno žal izgubil :)', height = 5, width = 40).pack()
		gumb_popup1 = tk.Button(self.popup, text='Izhod', command = lambda: os._exit(0)).pack()



	







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
		elif event.keysym == 'Down':
			self.igra.blok.premakni_dol()
			self.osvezi_prikaz()
			


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
		self.prikaz_naslednjega_bloka.delete('all')
		for x, y in self.igra.prikaz_bloka:
			self.prikaz_naslednjega_bloka.create_rectangle(4 * ODMIK + VELIKOST_POLJA * x,
				4 * ODMIK + VELIKOST_POLJA * y,
				4 * ODMIK + VELIKOST_POLJA * x + VELIKOST_POLJA,
				4 * ODMIK + VELIKOST_POLJA * y + VELIKOST_POLJA)







		

okno = tk.Tk()
moj_program = Tetris(okno)
okno.mainloop()