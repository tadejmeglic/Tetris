import random

Bloki = [[(-1, 0), (0, 0), (1, 0), (2, 0)], [(-1, 0), (-1, 1), (0, 1), (1, 1)], [(1, 0), (-1, 1),
(0, 1), (1, 1)], [(0, 0), (0, 1), (1, 0), (1, 1)], [(0, 0), (0, 1), (1, 0), (-1, 1)], [(0, 0), (0,
1), (1, 1), (-1, 1)], [(0, 0), (-1, 0), (0, 1), (1, 1)]]

class Blok:
	def __init__(self, tocke):
		self.tocke = tocke

	def __repr__(self):
		return 'Blok({})'.format(self.tocke)

	def premakni(self):
		if Igra.blok_v_tla(a) == False:
			if Igra.blok_v_blok(a) == False:
				for i in range(len(self.tocke)):
					self.tocke[i] = (self.tocke[i][0], self.tocke[i][1] + 1)
				return self.tocke
			else:
				a.povrsina += self.tocke
				Igra.pojav_bloka(a)
		else:
			Igra.blok_v_tla(a)

	def premakni_brez_ovire_test(self):
		s=[]
		for i in range(len(self.tocke)):
			x, y = self.tocke[i][0], self.tocke[i][1]
			y+=1
			s.append((x, y))
		return s


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

	def blok_v_blok(self):
		return not len(self.blok.premakni_brez_ovire_test() + self.povrsina) == len(set(self.blok.premakni_brez_ovire_test() + self.povrsina))



a = Igra(10, 10)
a.pojav_bloka()




