class Cabina:
    def __init__(self, id_cabina, n_letti, ponte, prezzo_base):
        self._id_cabina = id_cabina
        self._n_letti = int(n_letti)
        self._ponte = int(ponte)
        self._prezzo_base = float(prezzo_base)
        self._passeggeri_assegnati = []
        self.disponibile = True

    @property
    def id_cabina(self):
        return self._id_cabina

    def prezzo_finale(self):
        return self._prezzo_base

    def add_passeggero(self, passeggero):
        if len(self._passeggeri_assegnati) < self._n_letti:
            self._passeggeri_assegnati.append(passeggero)
            if len(self._passeggeri_assegnati) == self._n_letti:
                self.disponibile = False

        else: #in questo else il programma non dovrebbe entrare mai
            raise Exception("Errore durante l'assegnazione del passeggero alla cabina")

    def __eq__(self, other):
        if isinstance(other, Cabina):
            return self._id_cabina == other._id_cabina

    def __lt__(self, other):
        if isinstance(other, Cabina):
            return self.prezzo_finale() < other.prezzo_finale()
    def __le__(self, other):
        if isinstance(other, Cabina):
            return self.prezzo_finale() <= other.prezzo_finale()

    def __str__(self):
       return f"Cabina {self._id_cabina}, numero letti: {self._n_letti}, ponte: {self._ponte}, prezzo: {self.prezzo_finale()}"

class CabinaAnimali(Cabina):
    def __init__(self, id_cabina, n_letti, ponte, prezzo_base, animali):
        super().__init__(id_cabina, n_letti, ponte, prezzo_base)
        self._animali = float(animali)

    def prezzo_finale(self):
        return self._prezzo_base * (1 + 0.10 * self._animali)

class CabinaDeluxe(Cabina):
    def __init__(self, id_cabina, n_letti, ponte, prezzo_base, stile):
        super().__init__(id_cabina, n_letti, ponte, prezzo_base)
        self._stile = stile

    def prezzo_finale(self):
        return self._prezzo_base * 1.20