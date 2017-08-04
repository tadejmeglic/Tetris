import random
DESNO, DOL, LEVO = "desno", "dol", "levo"

#Bloki = [[(-1, 0), (0, 0), (1, 0), (2, 0)], [(-1, 0), (-1, 1), (0, 1), (1, 1)], [(1, 0), (-1, 1),
#(0, 1), (1, 1)], [(0, 0), (0, 1), (1, 0), (1, 1)], [(0, 0), (0, 1), (1, 0), (-1, 1)], [(0, 0), (0,
#1), (1, 1), (-1, 1)], [(0, 0), (-1, 0), (0, 1), (1, 1)]]

Bloki = [[(-1, 0), (0, 0), (1, 0), (2, 0)]]













class Igra:

	def __init__(self, sirina, dolzina):
		self.sirina = sirina
		self.dolzina = dolzina
		self.povrsina = []
		self.pojav_bloka()
		self.score = 0

	def pojav_bloka(self):
		dolocen_blok = random.choice(Bloki)
		s=[]
		# Določen blok spravimo na sredino in na vrh igralne površine
		for i in range(len(dolocen_blok)):
			x, y = dolocen_blok[i][0], dolocen_blok[i][1]
			x+= int(self.sirina) // 2
			s.append((x, y))
		self.blok = Blok(s)

	def blok_v_steno(self):
		for x, y in self.blok.tocke:
			if not (0 <= x < self.sirina):
				return True

	def blok_v_tla(self):
		a = 0
		for x, y in self.blok.tocke:
			if not y < self.dolzina - 1:
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

	def odstrani(self):
		# t označuje število odstranjenih vrstic naenkrat in exsponentno poveča pridobljene točke
		t=0
		for y in range(self.dolzina):
			k=0
			for x in range(self.sirina):
				if (x, y) in self.povrsina:
					k+=1
				if k == self.sirina:
					t+=1
					for x in range(self.sirina):
						self.povrsina.remove((x, y))
						k=0
					m = []
					for i in self.povrsina:
						if i[1] < y:
							i=(i[0], i[1] + 1)
							m.append(i)
						elif i[1] > y:
							m.append(i)
					self.povrsina = m
		self.score +=int(9 ** (t / 2)) - 1











	# Preverimo, če se premikajoči se blok v naslednji potezi zaleti v že obstoječe bloke ali steno.

	def blok_v_steno_rotiranje(self):
		for i in self.blok.rotiraj_brez_ovire():
			if 0 <= i[0] < self.sirina:
				return False

	def blok_v_blok_dol(self):
		return not len(self.blok.premakni_dol_brez_ovire_test() + self.povrsina) == len(set(self.blok.premakni_dol_brez_ovire_test() + self.povrsina))

	def blok_v_blok_desno(self):
		return not len(self.blok.premakni_vodoravno_brez_ovire(DESNO) + self.povrsina) == len(set(self.blok.premakni_vodoravno_brez_ovire(DESNO) + self.povrsina))

	def blok_v_blok_levo(self):
		return not len(self.blok.premakni_vodoravno_brez_ovire(LEVO) + self.povrsina) == len(set(self.blok.premakni_vodoravno_brez_ovire(LEVO) + self.povrsina))

	def blok_v_blok_rotiranje(self):
		return not len(self.blok.rotiraj_brez_ovire() + self.povrsina) == len(set(self.blok.rotiraj_brez_ovire() + self.povrsina))

class Blok(Igra):
	def __init__(self, tocke):
		self.tocke = tocke

	def __repr__(self):
		return 'Blok({})'.format(self.tocke)

	def premakni_dol(self):
		if Igra.blok_v_tla(instance) == False:
			if Igra.blok_v_blok_dol(instance) == False:
				for i in range(len(self.tocke)):
					self.tocke[i] = (self.tocke[i][0], self.tocke[i][1] + 1)
			else:
				instance.povrsina += self.tocke
				Igra.pojav_bloka(instance)
		else:
			Igra.blok_v_tla(instance)

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
			if Igra.blok_v_blok_desno(instance) == False:
				for i in range(len(self.tocke)):
					x, y = self.tocke[i][0], self.tocke[i][1]
					if x == instance.sirina - 1:
						return None
					else:
						continue
				for i in range(len(self.tocke)):
					self.tocke[i] = (self.tocke[i][0] + 1, self.tocke[i][1])
				return self.tocke
		if smer == LEVO:
			if Igra.blok_v_blok_levo(instance) == False:
				for i in range(len(self.tocke)):
					x, y = self.tocke[i][0], self.tocke[i][1]
					if x == 0:
						return None
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
		if Igra.blok_v_blok_rotiranje(instance) == False:
			for i in range(len(self.tocke)):
				tocke_okrog_izhodisca.append((int(self.tocke[i][0]) - centrala[0], int(self.tocke[i][1]) - centrala[1]))
			for i in range(len(tocke_okrog_izhodisca)):
				obrnjene_tocke.append((-tocke_okrog_izhodisca[i][1],tocke_okrog_izhodisca[i][0]))
			for i in range(len(obrnjene_tocke)):
				self.tocke[i] = (int(obrnjene_tocke[i][0]) + centrala[0], int(obrnjene_tocke[i][1]) + centrala[1])
			if Igra.blok_v_steno(instance) == True:
				self.popravi_blok_po_rotaciji()
		elif Igra.blok_v_steno_rotiranje(instance) == False:
			for a in self.rotiraj_brez_ovire():
				if a[0] - 1 < 0 or a[0] + 1 >= instance.sirina:
					return
				for x, y in instance.povrsina:
					if (a[0] + 1, y) == (x, y) or (a[0] - 1, y) == (x, y):
						return
			if set(self.rotiraj_brez_ovire()).intersection(instance.povrsina) != {}:
				if set(self.rotiraj_brez_ovire()).intersection(instance.povrsina).pop()[0] > centrala[0]:
					print(set(self.rotiraj_brez_ovire()).intersection(instance.povrsina), 'bo slo v levo')
					self.premakni_vodoravno(LEVO)
					self.rotiraj()
				elif set(self.rotiraj_brez_ovire()).intersection(instance.povrsina).pop()[0] < centrala[0]:
					print(set(self.rotiraj_brez_ovire()).intersection(instance.povrsina), 'bo slo v desno')
					self.premakni_vodoravno(DESNO)
					self.rotiraj()
		return self.tocke

	def rotiraj_nazaj(self):
		# dejansko ni namenjeno igri, temveč da blok obrne nazaj, če se le ta po rotaciji in premiku prekriva z blokom ali steno, kar povzroči rekurzijo
		centrala = self.centralna_kocka()
		tocke_okrog_izhodisca = []
		obrnjene_tocke = []
		for i in range(len(self.tocke)):
			tocke_okrog_izhodisca.append((int(self.tocke[i][0]) - centrala[0], int(self.tocke[i][1]) - centrala[1]))
		for i in range(len(tocke_okrog_izhodisca)):
			obrnjene_tocke.append((tocke_okrog_izhodisca[i][1],-tocke_okrog_izhodisca[i][0]))
		for i in range(len(obrnjene_tocke)):
			self.tocke[i] = (int(obrnjene_tocke[i][0]) + centrala[0], int(obrnjene_tocke[i][1]) + centrala[1])

	def popravi_blok_po_rotaciji(self):
		if Igra.blok_v_steno(instance) == True:
			for i in self.tocke:
				if i[0] < 0:
					if self.premakni_vodoravno(DESNO) != None:
						print('sem premaknil desno')
						break
					else:
						self.premakni_vodoravno(LEVO)
						self.rotiraj_nazaj()
						print('sem rotiral nazaj')
						break
				elif i[0] > instance.sirina - 1:
					if self.premakni_vodoravno(LEVO) != None:
						print('sem premaknil levo')
						break
					else:
						self.premakni_vodoravno(DESNO)
						self.rotiraj_nazaj()
						break
				elif i[1] < 0:
					self.premakni_dol()
					break
			self.popravi_blok_po_rotaciji()

	def rotiraj_brez_ovire(self):
		centrala = self.centralna_kocka()
		s=[]
		tocke_okrog_izhodisca = []
		obrnjene_tocke = []
		for i in range(len(self.tocke)):
			tocke_okrog_izhodisca.append((int(self.tocke[i][0]) - centrala[0], int(self.tocke[i][1]) - centrala[1]))
		for i in range(len(tocke_okrog_izhodisca)):
			obrnjene_tocke.append((-tocke_okrog_izhodisca[i][1],tocke_okrog_izhodisca[i][0]))
		for i in range(len(obrnjene_tocke)):
			s.append((int(obrnjene_tocke[i][0]) + centrala[0], int(obrnjene_tocke[i][1]) + centrala[1]))
		return s

instance = Igra(10, 20)
instance.pojav_bloka()




