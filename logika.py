import random

Bloki = [[(-1, 0), (0, 0), (1, 0), (2, 0)], [(-1, 0), (-1, 1), (0, 1), (1, 1)], [(1, 0), (-1, 1),
(0, 1), (1, 1)], [(0, 0), (0, 1), (1, 0), (1, 1)], [(0, 0), (0, 1), (1, 0), (-1, 1)], [(0, 0), (0,
1), (1, 1), (-1, 1)], [(0, 0), (-1, 0), (0, 1), (1, 1)]]

class Lik:
	def __init__(self, tocke):
		self.tocke = tocke

	def __repr__(self):
		return 'Lik({})'.format(self.tocke)

	def premakni(self):
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
		dolocen_lik = random.choice(Bloki)
		s=[]
		for i in range(len(dolocen_lik)):
			x, y = dolocen_lik[i][0], dolocen_lik[i][1]
			print(x, int(self.sirina))
			x+= int(self.sirina) // 2
			s.append((x, y))
		self.lik = Lik(s)


