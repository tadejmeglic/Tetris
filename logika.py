import random
DESNO, DOL, LEVO = "desno", "dol", "levo"

Bloki = [[(-1, 0), (0, 0), (1, 0), (2, 0)], [(-1, 0), (-1, 1), (0, 1), (1, 1)], [(1, 0), (-1, 1),
(0, 1), (1, 1)], [(0, 0), (0, 1), (1, 0), (1, 1)], [(0, 0), (0, 1), (1, 0), (-1, 1)], [(0, 0), (0,
1), (1, 1), (-1, 1)], [(0, 0), (-1, 0), (0, 1), (1, 1)]]

class Blok:
	def __init__(self, tocke):
		self.tocke = tocke

	def __repr__(self):
		return 'Blok({})'.format(self.tocke)

	def premakni_dol(self):
		if Igra.blok_v_tla(a) == False:
			if Igra.blok_v_blok_dol(a) == False:
				for i in range(len(self.tocke)):
					self.tocke[i] = (self.tocke[i][0], self.tocke[i][1] + 1)
				return self.tocke
			else:
				a.povrsina += self.tocke
				Igra.pojav_bloka(a)
		else:
			Igra.blok_v_tla(a)

	def premakni_dol_brez_ovire_test(self):
		# Metoda, ki preveri, kakšne bodo koordinate točk bloka po premiku. Ignorira tla in ostale bloke.
		s=[]
		for i in range(len(self.tocke)):
			x, y = self.tocke[i][0], self.tocke[i][1]
			y+=1
			s.append((x, y))
		return s

	def premakni_vodoravno(self, smer):
		if smer == DESNO:
			if Igra.blok_v_blok_desno(a) == False:
				for i in range(len(self.tocke)):
					x, y = self.tocke[i][0], self.tocke[i][1]
					if x == a.sirina - 1:
						return
					else:
						continue
				for i in range(len(self.tocke)):
					self.tocke[i] = (self.tocke[i][0] + 1, self.tocke[i][1])
				return self.tocke
		if smer == LEVO:
			if Igra.blok_v_blok_levo(a) == False:
				for i in range(len(self.tocke)):
					x, y = self.tocke[i][0], self.tocke[i][1]
					if x == 0:
						return
					else:
						continue
				for i in range(len(self.tocke)):
					self.tocke[i] = (self.tocke[i][0] - 1, self.tocke[i][1])
				return self.tocke

	def premakni_vodoravno_brez_ovire(self, smer):
		# Podobno kot za premik dol.
		if smer == DESNO:
			v_1 = []
			for i in range(len(self.tocke)):
				x, y = self.tocke[i][0], self.tocke[i][1]
				x+=1
				v_1.append((x, y))
			return v_1
		elif smer == LEVO:
			v_2 = []
			for i in range(len(self.tocke)):
				x, y = self.tocke[i][0], self.tocke[i][1]
				x-=1
				v_2.append((x, y))
			return v_2

	def centralna_kocka(self):
		x, y = 0, 0
		for i in range(len(self.tocke)):
			x+=int(self.tocke[i][0])
			y+=int(self.tocke[i][1])
		return (round(x / len(self.tocke)), round(y / len(self.tocke)))

	def rotiraj(self):
		centrala = self.centralna_kocka()
		tocke_okrog_izhodisca = []
		obrnjene_tocke = []
		# Sprva poiščemo točko, ki je centralna, torej okoli katere se bo blok zavrtel. Nato blok premaknemo na izhodišče s centralno točko na koordinati (0, 0), nakar
		# blok obrnemo s pomočjo matrike, a ker je za kot 90°, na srečo ni potrebno uporabit matrik, le dejstvo, da je
		# treba zamenjati koordinati ter obrniti predznak pri prvi. Self.tocke, tocke_okrog_izgodisca in obrnjene_tocke
		# so enako dolgi seznami, takšen napis je le za lažji pregled.
		for i in range(len(self.tocke)):
			tocke_okrog_izhodisca.append((int(self.tocke[i][0]) - centrala[0], int(self.tocke[i][1]) - centrala[1]))
		for i in range(len(tocke_okrog_izhodisca)):
			obrnjene_tocke.append((-tocke_okrog_izhodisca[i][1],tocke_okrog_izhodisca[i][0]))
		for i in range(len(obrnjene_tocke)):
			self.tocke[i] = (int(obrnjene_tocke[i][0]) + centrala[0], int(obrnjene_tocke[i][1]) + centrala[1])
		return self.tocke












class Igra:

	def __init__(self, sirina, dolzina):
		self.sirina = sirina
		self.dolzina = dolzina
		self.povrsina = []

	def pojav_bloka(self):
		dolocen_blok = random.choice(Bloki)
		s=[]
		# Določen blok spravimo na sredino in na vrh igralne površine
		for i in range(len(dolocen_blok)):
			x, y = dolocen_blok[i][0], dolocen_blok[i][1]
			print(x, int(self.sirina))
			x+= int(self.sirina) // 2
			s.append((x, y))
		self.blok = Blok(s)

	def blok_v_steno(self):
		for x, y in self.blok.tocke:
			if not (0 <= x < self.sirina):
				return False

	def blok_v_tla(self):
		a = 0
		for x, y in self.blok.tocke:
			print((x, y))
			if not (0 <= y < self.dolzina - 1):
				self.povrsina += (self.blok.tocke)
				self.pojav_bloka()
				a = 1
				break
			else:
				a = 0
		if a == 0:
			return False
		else:
			return True

	# Preverimo, če se premikajoči se blok v naslednji potezi zaleti v že obstoječe bloke.

	def blok_v_blok_dol(self):
		return not len(self.blok.premakni_dol_brez_ovire_test() + self.povrsina) == len(set(self.blok.premakni_dol_brez_ovire_test() + self.povrsina))

	def blok_v_blok_desno(self):
		return not len(self.blok.premakni_vodoravno_brez_ovire(DESNO) + self.povrsina) == len(set(self.blok.premakni_vodoravno_brez_ovire(DESNO) + self.povrsina))

	def blok_v_blok_levo(self):
		return not len(self.blok.premakni_vodoravno_brez_ovire(LEVO) + self.povrsina) == len(set(self.blok.premakni_vodoravno_brez_ovire(LEVO) + self.povrsina))



a = Igra(10, 10)
a.pojav_bloka()




