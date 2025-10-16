class Passeggero:
    def __init__(self, id_passeggero, nome, cognome):
        self._id_passeggero = id_passeggero
        self._nome = nome
        self._cognome = cognome
        self._cabina_assegnata = None

    @property
    def id_passeggero(self):
        return self._id_passeggero
    @property
    def cabina_assegnata(self):
        return self._cabina_assegnata
    @cabina_assegnata.setter
    def cabina_assegnata(self, cabina_assegnata):
        self._cabina_assegnata = cabina_assegnata

    def __str__(self):
        return f"Passeggero {self._id_passeggero}, nome: {self._nome} {self._cognome}, cabina assegnata: {self._cabina_assegnata}"