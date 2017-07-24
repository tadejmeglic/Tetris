
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
