import tkinter as tk

class Tetris:
	def __init__(self, okno):
		self.igra = Igra(10, 10)

	def vmesnik(self, okno):
		prikaz = tk.Frame(okno)
		prikaz.grid(row=0, column=0)
		self.osvezi_prikaz()

		gumbi = tk.Frame(okno)
		

okno = th.Tk()
moj_program = Tetris(okno)
okno.mainloop()