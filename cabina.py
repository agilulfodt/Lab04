class Cabina:
    def __init__(self, id_cabina, n_letti, ponte, prezzo_base):
        self._id_cabina = id_cabina
        self._n_letti = int(n_letti)
        self._ponte = int(ponte)
        self._prezzo_base = float(prezzo_base)

    def __str__(self):
       return f"Cabina {self._id_cabina}, numero letti: {self._n_letti}, ponte: {self._ponte}, prezzo base: {self._prezzo_base}"

class CabinaAnimali(Cabina):
    def __init__(self, id_cabina, n_letti, ponte, prezzo_base, animali):
        super().__init__(id_cabina, n_letti, ponte, prezzo_base)
        self._animali = animali

class CabinaDeluxe(Cabina):
    def __init__(self, id_cabina, n_letti, ponte, prezzo_base, stile):
        super().__init__(id_cabina, n_letti, ponte, prezzo_base)
        self._stile = stile